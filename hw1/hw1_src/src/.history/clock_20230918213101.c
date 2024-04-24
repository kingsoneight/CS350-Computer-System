/*******************************************************************************
 * CPU Clock Measurement Using RDTSC
 *
 * Description:
 *     This C file provides functions to compute and measure the CPU clock using
 *     the `rdtsc` instruction. The `rdtsc` instruction returns the Time Stamp
 *     Counter, which can be used to measure CPU clock cycles.
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
 *     Ensure that the platform supports the `rdtsc` instruction before using
 *     these functions. Depending on the CPU architecture and power-saving
 *     modes, the results might vary. Always refer to the CPU's official
 *     documentation for accurate interpretations.
 *
 *******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

#include "timelib.h"

int main(int argc, char **argv)
{
	if (argc != 4)
	{
		printf("Wrong number of arguments");
		return 1;
	}

	long sec = strtol(argv[1], NULL, 10);
	long nsec = strtol(argv[2], NULL, 10);
	char mode = argv[3][0];
	uint64_t passed_cycles;
	double speed;
	char *mode_str[20];

	if (mode == 's')
	{
		passed_cycles = get_elapsed_sleep(sec, nsec);
		strcpy(mode_str, "SLEEP");
	}
	else if (mode == 'b')
	{
		passed_cycles = get_elapsed_busywait(sec, nsec);
		strcpy(mode_str, "BUSYWAIT");
	}
	speed = (double)passed_cycles / ((double)(sec * 1e9 + nsec) / 1000);

	printf("WaitMethod: %s\nWaitTime: %d %d\nClocksElapsed: %d\nClockSpeed: %f", mode_str, sec, nsec, passed_cycles, speed);

	return EXIT_SUCCESS;
}
