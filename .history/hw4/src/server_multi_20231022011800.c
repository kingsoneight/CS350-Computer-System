/*******************************************************************************
 * Multi-Threaded FIFO Server Implementation w/ Queue Limit
 *
 * Description:
 *     A server implementation designed to process client requests in First In,
 *     First Out (FIFO) order. The server binds to the specified port number
 *     provided as a parameter upon launch. It launches multiple threads to
 *     process incoming requests and allows to specify a maximum queue size.
 *
 * Usage:
 *     <build directory>/server -q <queue_size> -w <workers> <port_number>
 *
 * Parameters:
 *     port_number - The port number to bind the server to.
 *     queue_size  - The maximum number of queued requests
 *     workers     - The number of workers to start to process requests
 *
 * Author:
 *     Renato Mancuso
 *
 * Affiliation:
 *     Boston University
 *
 * Creation Date:
 *     September 29, 2023
 *
 * Notes:
 *     Ensure to have proper permissions and available port before running the
 *     server. The server relies on a FIFO mechanism to handle requests, thus
 *     guaranteeing the order of processing. If the queue is full at the time a
 *     new request is received, the request is rejected with a negative ack.
 *
 *******************************************************************************/

#define _GNU_SOURCE
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <sched.h>
#include <signal.h>

/* Needed for wait(...) */
#include <sys/types.h>
#include <sys/wait.h>

/* Needed for semaphores */
#include <semaphore.h>

/* Include struct definitions and other libraries that need to be
 * included by both client and server */
#include "common.h"

#define BACKLOG_COUNT 100
#define USAGE_STRING              \
	"Missing parameter. Exiting.\n" \
	"Usage: %s -q <queue size> -w <number of threads> <port_number>\n"

/* 4KB of stack for the worker thread */
#define STACK_SIZE (4096)

/* Mutex needed to protect the threaded printf. DO NOT TOUCH */
sem_t *printf_mutex;

/* Synchronized printf for multi-threaded operation */
#define sync_printf(...)    \
	do                        \
	{                         \
		sem_wait(printf_mutex); \
		printf(__VA_ARGS__);    \
		sem_post(printf_mutex); \
	} while (0)

/* START - Variables needed to protect the shared queue. DO NOT TOUCH */
sem_t *queue_mutex;
sem_t *queue_notify;
/* END - Variables needed to protect the shared queue. DO NOT TOUCH */

struct request_meta
{
	struct request request;
	struct timespec recei;
	volatile int invalid;
};

/* New resp struct containing rejected field */
struct response_meta
{
	uint64_t req_id;
	uint8_t rejected;
};

struct queue
{
	int front;
	int rear;
	size_t size;
	struct request_meta *mes_queue;
};
/* Helper function to perform queue initialization */
struct queue *queue_init(size_t queue_size)
{
	struct queue *the_queue = (struct queue *)malloc(sizeof(struct queue));
	if (the_queue == NULL)
	{
		perror("Failed to allocate memory for queue");
		exit(EXIT_FAILURE);
	}
	the_queue->front = -1;
	the_queue->rear = -1;
	the_queue->size = queue_size;
	the_queue->mes_queue = (struct request_meta *)malloc(sizeof(struct request_meta) * queue_size);
	if (the_queue->mes_queue == NULL)
	{
		perror("Failed to allocate memory for queue data");
		free(the_queue);
		exit(EXIT_FAILURE);
	}

	return the_queue;
}

/* Methods to check if queue is empty or full*/
int isFull(struct queue q)
{
	if ((q.front == q.rear + 1) || (q.front == 0 && q.rear == q.size - 1))
		return 1;
	return 0;
}

int isEmpty(struct queue q)
{
	if (q.front == -1)
	{
		return 1;
	}
	return 0;
}

struct connection_params
{
	int queue_size;
	int num_worker;
};

struct worker_params
{
	struct queue *the_queue;
	int conn_socket;
	int worker_done;
	int thread_id;
};

/* Add a new request <request> to the shared queue <the_queue> */
int add_to_queue(struct request_meta to_add, struct queue *the_queue)
{
	int retval = 0;
	/* QUEUE PROTECTION INTRO START --- DO NOT TOUCH */
	sem_wait(queue_mutex);
	/* QUEUE PROTECTION INTRO END --- DO NOT TOUCH */

	/* WRITE YOUR CODE HERE! */
	/* MAKE SURE NOT TO RETURN WITHOUT GOING THROUGH THE OUTRO CODE! */

	/* Make sure that the queue is not full */
	if (isFull(*the_queue))
	{
		/* What to do in case of a full queue */
		retval = -1;
		/* DO NOT RETURN DIRECTLY HERE. The
		 * sem_post(queue_mutex) below MUST happen. */
	}
	else
	{
		/* If all good, add the item in the queue */
		/* IMPLEMENT ME !!*/
		if (the_queue->front == -1)
			the_queue->front = 0;
		the_queue->rear = (the_queue->rear + 1) % the_queue->size;
		the_queue->mes_queue[the_queue->rear] = to_add;

		/* QUEUE SIGNALING FOR CONSUMER --- DO NOT TOUCH */
		sem_post(queue_notify);
	}

	/* QUEUE PROTECTION OUTRO START --- DO NOT TOUCH */
	sem_post(queue_mutex);
	/* QUEUE PROTECTION OUTRO END --- DO NOT TOUCH */
	return retval;
}

/* Add a new request <request> to the shared queue <the_queue> */
struct request_meta get_from_queue(struct queue *the_queue)
{
	struct request_meta retval;
	/* QUEUE PROTECTION INTRO START --- DO NOT TOUCH */
	sem_wait(queue_notify);
	sem_wait(queue_mutex);
	/* QUEUE PROTECTION INTRO END --- DO NOT TOUCH */

	/* WRITE YOUR CODE HERE! */
	/* MAKE SURE NOT TO RETURN WITHOUT GOING THROUGH THE OUTRO CODE! */

	/* check if it's empty queue (necessary in multithreading)*/
	if (isEmpty(*the_queue))
	{
		retval.invalid = 1;
		sem_post(queue_mutex);
		return retval;
	}
	retval.request = the_queue->mes_queue[the_queue->front].request;
	retval.recei = the_queue->mes_queue[the_queue->front].recei;

	if (the_queue->front == the_queue->rear)
	{
		the_queue->front = -1;
		the_queue->rear = -1;
	}
	else
	{
		the_queue->front = (the_queue->front + 1) % the_queue->size;
	}
	/* QUEUE PROTECTION OUTRO START --- DO NOT TOUCH */
	sem_post(queue_mutex);
	/* QUEUE PROTECTION OUTRO END --- DO NOT TOUCH */
	return retval;
}

void dump_queue_status(struct queue *the_queue)
{

	int i = the_queue->front;

	/* QUEUE PROTECTION INTRO START --- DO NOT TOUCH */
	sem_wait(queue_mutex);
	/* QUEUE PROTECTION INTRO END --- DO NOT TOUCH */

	/* WRITE YOUR CODE HERE! */
	/* MAKE SURE NOT TO RETURN WITHOUT GOING THROUGH THE OUTRO CODE! */
	if (the_queue->front == -1)
	{
		sync_printf("Q:[]\n");
	}
	else
	{
		sync_printf("Q:[");

		while (1)
		{
			sync_printf("R%llu", the_queue->mes_queue[i].request.req_id);

			if (i == the_queue->rear)
			{
				break;
			}

			if (i != the_queue->rear)
			{
				sync_printf(",");
			}

			i = (i + 1) % the_queue->size;
		}
		sync_printf("]\n");
	}

	/* QUEUE PROTECTION OUTRO START --- DO NOT TOUCH */
	sem_post(queue_mutex);
	/* QUEUE PROTECTION OUTRO END --- DO NOT TOUCH */
}

/* Main logic of the worker thread */
int worker_main(struct worker_params *params)
{
	struct request rq;
	struct timespec now;
	struct timespec receipt, start;
	struct timespec completion;
	struct request_meta msg;
	struct response_meta rp_meta;

	sync_printf("threadID is: %d\n", params->thread_id);
	/* Print the first alive message. */
	clock_gettime(CLOCK_MONOTONIC, &now);
	sync_printf("[#WORKER#] %lf Worker Thread Alive!\n", TSPEC_TO_DOUBLE(now));

	/* Okay, now execute the main logic. */
	while (!params->worker_done)
	{
		/* IMPLEMENT ME !! Main worker logic. */
		while (isEmpty(*(params->the_queue)) == 0)
		{

			msg = get_from_queue(params->the_queue);
			/* msg may be blocked on lock when other threads are processing. So it can go into the isEmpty() loop and get_from_queue even if it's empty. I modified get_f_q to check for emptiness.*/
			if (msg.invalid == 1)
			{
				break;
			}
			/* Read msg (request_meta) into variables, prepare rp_meta for sending back to client*/
			rq = msg.request;
			receipt = msg.recei;
			rp_meta.req_id = rq.req_id;
			rp_meta.rejected = 0;

			clock_gettime(CLOCK_MONOTONIC, &start);

			get_elapsed_busywait(rq.req_length.tv_sec, rq.req_length.tv_nsec);

			clock_gettime(CLOCK_MONOTONIC, &completion);

			if (send(params->conn_socket, &rp_meta, sizeof(struct response_meta), 0) == -1)
			{
				sync_printf("failed to send to client.\n");
			}
			/* convert all the timespec to double*/
			double sent_timestamp = (double)rq.req_timestamp.tv_sec + ((double)rq.req_timestamp.tv_nsec) / 1e9;
			double request_length = (double)rq.req_length.tv_sec + ((double)rq.req_length.tv_nsec) / 1e9;
			double receipt_timestamp = (double)receipt.tv_sec + ((double)receipt.tv_nsec) / 1e9;
			double start_timestamp = (double)start.tv_sec + ((double)start.tv_nsec) / 1e9;
			double completion_timestamp = (double)completion.tv_sec + ((double)completion.tv_nsec) / 1e9;

			sync_printf("T%d R%llu:%0.6f,%0.6f,%0.6f,%0.6f,%0.6f\n", params->thread_id, rq.req_id, sent_timestamp,
									request_length, receipt_timestamp, start_timestamp, completion_timestamp);

			dump_queue_status(params->the_queue);
			fflush(stdout);
		}
	}

	return EXIT_SUCCESS;
}

/* This function will start the worker thread wrapping around the
 * clone() system call*/
int start_worker(void *params, void *worker_stack)
{
	return clone(worker_main, worker_stack + STACK_SIZE, CLONE_THREAD | CLONE_VM | CLONE_SIGHAND | CLONE_FS | CLONE_FILES | CLONE_SYSVSEM, params);
}

/* Main function to handle connection with the client. This function
 * takes in input conn_socket and returns only when the connection
 * with the client is interrupted. */
void handle_connection(int conn_socket, struct connection_params conn_params)
{
	struct request_meta *req;
	struct queue *the_queue;
	size_t in_bytes;
	struct response_meta rp_meta;
	the_queue = queue_init(conn_params.queue_size);

	/* array storing pointers to each worker stack */
	void *stack_array[conn_params.num_worker];
	/* array storing pointers to each worker param */
	struct worker_params *param_array[conn_params.num_worker];

	for (int i = 0; i < conn_params.num_worker; i++)
	{
		void *worker_stack = malloc(STACK_SIZE);
		stack_array[i] = worker_stack;
		/* set up fields in worker_params for thread creation*/
		struct worker_params *worker_params = (struct worker_params *)malloc(sizeof(struct worker_params));
		worker_params->the_queue = the_queue;
		worker_params->conn_socket = conn_socket;
		worker_params->worker_done = 0;
		worker_params->thread_id = i;
		param_array[i] = worker_params;

		start_worker(worker_params, worker_stack);
	}

	/* IMPLEMENT ME!! Write a loop to start and initialize all the
	 * worker threads ! */

	/* We are ready to proceed with the rest of the request
	 * handling logic. */

	req = (struct request_meta *)malloc(sizeof(struct request_meta));

	do
	{
		struct timespec receipt, reject;

		in_bytes = read(conn_socket, &(req->request), sizeof(struct request));
		clock_gettime(CLOCK_MONOTONIC, &receipt);
		req->recei = receipt;

		if (isFull(*(the_queue)))
		{
			/* get reject timestamp and set up the response back to client*/
			clock_gettime(CLOCK_MONOTONIC, &reject);
			rp_meta.rejected = 1;
			rp_meta.req_id = req->request.req_id;

			sync_printf("X%llu:%lf,%lf,%lf\n", req->request.req_id, TSPEC_TO_DOUBLE(req->request.req_timestamp), TSPEC_TO_DOUBLE(req->request.req_length), TSPEC_TO_DOUBLE(reject));
			send(conn_socket, &rp_meta, sizeof(struct response_meta), 0) != -1;
			fflush(stdout);
		}
		else
		{
			if (in_bytes > 0)
			{
				add_to_queue(*req, the_queue);
				printf("request %llu is added to the queue\n", req->request.req_id);
			}
			if (in_bytes == 0)
			{
				sync_printf("Connection closed gracefully.");
				break;
			}
			else if (in_bytes == -1)
			{
				sync_printf("Error: connection closed.");
				break;
			}
		}
	} while (in_bytes > 0);

	/* IMPLEMENT ME!! Write a loop to gracefully terminate all the
	 * worker threads ! */

	/* Ask the worker thead to terminate */
	printf("INFO: Asserting termination flag for worker thread...\n");

	/* PERFORM ORDERLY DEALLOCATION AND OUTRO HERE */
	for (int i = 0; i < conn_params.num_worker; i++)
	{
		param_array[i]->worker_done = 1;
	}
	/* Just in case the thread is stuck on the notify semaphore,
	 * wake it up */
	sem_post(queue_notify);
	/* Wait for orderly termination of the worker thread */

	pid_t ret = waitpid(-1, NULL, 0);
	if (ret == -1)
	{
		perror("waitpid error");
	}
	for (int i = 0; i < conn_params.num_worker; i++)
	{
		free(stack_array[i]);
	}
	for (int i = 0; i < conn_params.num_worker; i++)
	{
		free(param_array[i]);
	}
	free(the_queue);
	free(req);
	shutdown(conn_socket, SHUT_RDWR);
	close(conn_socket);
	printf("INFO: Client disconnected.\n");
}

/* Template implementation of the main function for the FIFO
 * server. The server must accept in input a command line parameter
 * with the <port number> to bind the server to. */
int main(int argc, char **argv)
{
	int sockfd, retval, accepted, optval, opt;
	in_port_t socket_port;
	struct sockaddr_in addr, client;
	struct in_addr any_address;
	socklen_t client_len;

	struct connection_params conn_params;

	/* Parse all the command line arguments */
	/* IMPLEMENT ME!! */
	/* PARSE THE COMMANDS LINE: */
	/* 1. Detect the -q parameter and set aside the queue size in conn_params */

	/* 2. Detect the -w parameter and set aside the number of threads to launch */
	conn_params.queue_size = -1; // Initialize with an invalid value
	conn_params.num_worker = -1; // Initialize with an invalid value
	optind = 1;									 // Ensure we start from the first argument

	while ((opt = getopt(argc, argv, "q:w:")) != -1)
	{
		switch (opt)
		{
		case 'q':
			conn_params.queue_size = atoi(optarg);
			break;
		case 'w':
			conn_params.num_worker = atoi(optarg);
			break;
		case '?':
		default:
			fprintf(stderr, "Usage: %s [-q queue_size] [-w num_worker]\n", argv[0]);
			exit(EXIT_FAILURE);
		}
	}
	/* 3. Detect the port number to bind the server socket to (see HW1 and HW2) */
	socket_port = strtol(argv[5], NULL, 10);

	/* Now onward to create the right type of socket */
	sockfd = socket(AF_INET, SOCK_STREAM, 0);

	if (sockfd < 0)
	{
		ERROR_INFO();
		perror("Unable to create socket");
		return EXIT_FAILURE;
	}

	/* Before moving forward, set socket to reuse address */
	optval = 1;
	setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, (void *)&optval, sizeof(optval));

	/* Convert INADDR_ANY into network byte order */
	any_address.s_addr = htonl(INADDR_ANY);

	/* Time to bind the socket to the right port  */
	addr.sin_family = AF_INET;
	addr.sin_port = htons(socket_port);
	addr.sin_addr = any_address;

	/* Attempt to bind the socket with the given parameters */
	retval = bind(sockfd, (struct sockaddr *)&addr, sizeof(struct sockaddr_in));

	if (retval < 0)
	{
		ERROR_INFO();
		perror("Unable to bind socket");
		return EXIT_FAILURE;
	}

	/* Let us now proceed to set the server to listen on the selected port */
	retval = listen(sockfd, BACKLOG_COUNT);

	if (retval < 0)
	{
		ERROR_INFO();
		perror("Unable to listen on socket");
		return EXIT_FAILURE;
	}

	/* Ready to accept connections! */
	printf("INFO: Waiting for incoming connection...\n");
	client_len = sizeof(struct sockaddr_in);
	accepted = accept(sockfd, (struct sockaddr *)&client, &client_len);

	if (accepted == -1)
	{
		ERROR_INFO();
		perror("Unable to accept connections");
		return EXIT_FAILURE;
	}

	/* Initilize threaded printf mutex */
	printf_mutex = (sem_t *)malloc(sizeof(sem_t));
	retval = sem_init(printf_mutex, 0, 1);
	if (retval < 0)
	{
		ERROR_INFO();
		perror("Unable to initialize printf mutex");
		return EXIT_FAILURE;
	}

	/* Initialize queue protection variables. DO NOT TOUCH. */
	queue_mutex = (sem_t *)malloc(sizeof(sem_t));
	queue_notify = (sem_t *)malloc(sizeof(sem_t));
	retval = sem_init(queue_mutex, 0, 1);
	if (retval < 0)
	{
		ERROR_INFO();
		perror("Unable to initialize queue mutex");
		return EXIT_FAILURE;
	}
	retval = sem_init(queue_notify, 0, 0);
	if (retval < 0)
	{
		ERROR_INFO();
		perror("Unable to initialize queue notify");
		return EXIT_FAILURE;
	}
	/* DONE - Initialize queue protection variables */

	/* Ready to handle the new connection with the client. */
	handle_connection(accepted, conn_params);

	free(queue_mutex);
	free(queue_notify);

	close(sockfd);
	return EXIT_SUCCESS;
}
