/*******************************************************************************
 * Time Functions Library (implementation)
 *
 * Description:
 *     A library to handle various time-related functions and operations.
 *
 * Author:
 *     Renato Mancuso <rmancuso@bu.edu>
 *
 * Affiliation:
 *     Boston University
 *
 * Creation Date:
 *     September 10, 2023
 *
 * Notes:
 *     Ensure to link against the necessary dependencies when compiling and
 *     using this library. Modifications or improvements are welcome. Please
 *     refer to the accompanying documentation for detailed usage instructions.
 *
 *******************************************************************************/

#include "timelib.h"

/* Return the number of clock cycles elapsed when waiting for
 * wait_time seconds using sleeping functions */
uint64_t get_elapsed_sleep(long sec, long nsec)
{

	/* initialize variable clock and timespec structs for nanosleep*/
	uint64_t clock1;
	uint64_t clock2;
	struct timespec req, rem;
	req.tv_sec = sec;
	req.tv_nsec = nsec;

	get_clocks(clock1);
	nanosleep(&req, &rem);
	get_clocks(clock2);

	return clock2 - clock1;
}