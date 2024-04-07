"""Drive application."""

import csv, traceback

# from components import Scheduler
from utils  import ARGS, BANNER, LOGGER

if __name__ == '__main__':

    try:

        LOGGER.info(BANNER)

        LOGGER.info(f"""Scheduling Policies:
        1. {ARGS.primary_policy}
        2. {ARGS.secondary_policy}
        3. {ARGS.tertiary_policy}""")

        # scheduler:  Scheduler = Scheduler(ARGS.primary_policy, ARGS.secondary_policy, ARGS.tertiary_policy, ARGS.queues, ARGS.cores, f"conf/job_lists/job_list_{ARGS.job_list}.csv")

        with open(f"conf/job_lists/job_list_{ARGS.job_list}.csv",                    "r",             encoding="utf-8")     as job_list, \
             open(f"{ARGS.output_path}/FCFS/processed_job_list_{ARGS.job_list}.csv", "w", newline="", encoding="utf=-8")    as results:
            
            reader = csv.DictReader(job_list)
            writer = csv.writer(results)
            
            writer.writerow(["PROCESS ID", "ARRIVAL TIME", "BURST TIME", "PRIORITY", "START TIME", "END TIME", "WAIT TIME"])
            
            id = 1
            time = 0
            
            jct = 0
            
            for row in reader:
                
                if time >= int(row["ARRIVAL TIME"]):
                
                    start_time = time
                    
                    for i in range(int(row["BURST TIME"])):
                        
                        time += 1
                        
                    end_time = time
                    
                    writer.writerow([id, row["ARRIVAL TIME"], row["BURST TIME"], row["PRIORITY"], start_time, end_time, (end_time - int(row["ARRIVAL TIME"]) - int(row["BURST TIME"]))])
                    
                    jct += (end_time - int(row["ARRIVAL TIME"]) - int(row["BURST TIME"]))
                    
                    id += 1
                    
                else: time += 1
                
            writer.writerow([ "AVERAGE JCT", "", "", "", "", "", round(jct / id, 2)])

    except KeyboardInterrupt:

        LOGGER.critical("Keyboard interrupt detected")

    except Exception as e:

        LOGGER.error(f"An error occurred: {e}")

        traceback.print_exc()

    finally:

        LOGGER.info("Exiting...")