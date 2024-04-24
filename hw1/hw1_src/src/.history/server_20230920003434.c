/*******************************************************************************
 * Simple FIFO Order Server Implementation
 *
 * Description:
 *     A server implementation designed to process client requests in First In,
 *     First Out (FIFO) order. The server binds to the specified port number
 *     provided as a parameter upon launch.
 *
 * Usage:
 *     <build directory>/server <port_number>
 *
 * Parameters:
 *     port_number - The port number to bind the server to.
 *
 * Author:
 *     Renato Mancuso
 *
 * Affiliation:
 *     Boston University
 *
 * Creation Date:
 *     September 10, 2023
 *
 * Notes:
 *     Ensure to have proper permissions and available port before running the
 *     server. The server relies on a FIFO mechanism to handle requests, thus
 *     guaranteeing the order of processing. For debugging or more details, refer
 *     to the accompanying documentation and logs.
 *
 *******************************************************************************/

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

/* Include struct definitions and other libraries that need to be
 * included by both client and server */
#include "common.h"

#define BACKLOG_COUNT 100
#define USAGE_STRING              \
	"Missing parameter. Exiting.\n" \
	"Usage: %s <port_number>\n"

#define REQUEST_SIZE sizeof(uint64_t) + sizeof(struct timespec) * 2

/* Main function to handle connection with the client. This function
 * takes in input conn_socket and returns only when the connection
 * with the client is interrupted. */
static void handle_connection(int conn_socket)
{
	char buffer[REQUEST_SIZE] = {0};
	while (1)
	{
		ssize_t bytes_rcv = read(conn_socket, buffer, REQUEST_SIZE);
		uint64_t reqID;
		struct timespec req_sent, req_len, receipt, completion;
		if (bytes_rcv <= 0)
		{
			break;
		}

		if (bytes_rcv != REQUEST_SIZE)
		{
			printf("Incorrect request size.");
			break;
		}

		memcpy(&reqID, buffer, sizeof(uint64_t));
		memcpy(&req_sent, buffer + sizeof(uint64_t), sizeof(struct timespec));
		memcpy(&req_len, buffer + sizeof(uint64_t) + sizeof(struct timespec), sizeof(struct timespec));

		clock_gettime(CLOCK_MONOTONIC, &receipt);
		get_elapsed_busywait(1, 0);
		clock_gettime(CLOCK_MONOTONIC, &completion);

		send(conn_socket, &reqID, sizeof(uint64_t), 0);
		printf("message sent");
	}
}

/* char buffer[4096] = {0};
	int valread;
	while ((valread = read(conn_socket, buffer, 1024)) > 0)
	{
		printf("Message from Client: %s\n", buffer);
		get_elapsed_busywait(3, 10000);
		send(conn_socket, "message from server", strlen("message from server"), 0);
		printf("message sent");
	}
	if (valread < 0)
	{
		perror("read");
	}
*/

/* Template implementation of the main function for the FIFO
 * server. The server must accept in input a command line parameter
 * with the <port number> to bind the server to. */
int main(int argc, char **argv)
{
	int sockfd, retval, accepted, optval;
	in_port_t socket_port;
	struct sockaddr_in addr, client;
	struct in_addr any_address;
	socklen_t client_len;

	/* Get port to bind our socket to */
	if (argc > 1)
	{
		socket_port = strtol(argv[1], NULL, 10);
		printf("INFO: setting server port as: %d\n", socket_port);
	}
	else
	{
		ERROR_INFO();
		fprintf(stderr, USAGE_STRING, argv[0]);
		return EXIT_FAILURE;
	}

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

	/* Ready to handle the new connection with the client. */
	handle_connection(accepted);

	close(sockfd);
	return EXIT_SUCCESS;
}
