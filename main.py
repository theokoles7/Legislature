"""Drive application."""

import csv, traceback

from components import Scheduler, Task
from utils  import ARGS, BANNER, LOGGER

if __name__ == '__main__':

    try:
        # Log the app banner
        LOGGER.info(BANNER)

        # Log the policy configuration for this run
        LOGGER.info(f"""Scheduling Policies:
        1. {ARGS.primary_policy}
        2. {ARGS.secondary_policy}
        3. {ARGS.tertiary_policy}""")

        # Initialize scheduler
        scheduler:  Scheduler = Scheduler(ARGS.primary_policy, ARGS.secondary_policy, ARGS.tertiary_policy)
        
        # Open job list file
        with open(f"conf/job_lists/job_list_{ARGS.job_list}.csv", "r") as file_in:
            
            # Initialize job list from file, without header
            job_list = list(csv.reader(file_in))[1:]
            
            # Initialize program counter
            pc = 0
            
            # Parse through job list
            while pc <= int(job_list[-1][0]):
                
                # Grab jobs that correspond to the current program counter value
                new_jobs = list(filter(lambda job: int(job[0]) == pc, job_list))
                
                # If there are new jobs
                if len(new_jobs) > 0:
                    
                    # Submit those jobs to the scheduler
                    LOGGER.info(f"Submitting new job(s) @ pc = {pc}: {new_jobs}")
                    scheduler.submit_task([Task(task[0], task[1], task[2]) for task in new_jobs])
                
                # Increment the program counter
                pc += 1

    # Gracefully handle keyboard interrupts
    except KeyboardInterrupt:

        LOGGER.critical("Keyboard interrupt detected")

    # Report other errors
    except Exception as e:

        # Log error
        LOGGER.error(f"An error occurred: {e}")

        # Log stacktrace
        traceback.print_exc(file = open(LOGGER.handlers[1].baseFilename, "a"))

    finally:
        # Report graceful exit
        LOGGER.info("Exiting...")