import csv, itertools, matplotlib.pyplot as plt, os, random

# CLASSES =========================================================================================

class Job():
    
    job_id: int = itertools.count()
    
    def __init__(self, arrival, burst, priority):
        self.id:        int =   next(Job.job_id)
        self.arrival:   int =   int(arrival)
        self.burst:     int =   int(burst)
        self.priority:  int =   int(priority)
        self.start:     int =   0
        self.end:       int =   0
        self.wait:      int =   0
        self.run_time:  int =   0
        
    def __str__(self) -> str:
        
        return f"Job(id: {self.id}, arrival: {self.arrival}, burst: {self.burst}, priority: {self.priority}, start: {self.start}, end: {self.end}, wait: {self.wait})"

# METHODS =========================================================================================

def initialize_job_lists() -> None:
    """Initialize 4 job lists where:
    - Each list has 10 to the power of the list number jobs (i.e., 10, 100, etc.)
    - Each job will be assigned an arrival time, burst time, and priority
    - Arrival time is randomly incremented based on coin toss as loop progresses
    - Burst time is in random range of 0 - 100
    - Priority is randomly assigned in the range of 1 - 3, with 1 being the highest priority
    """
    for i in [1, 2, 3, 4]:

        with open(f"input/job_list_{i}.csv", "w", newline = "", encoding = "utf-8") as file_out:

            writer: csv.writer =    csv.writer(file_out)

            writer.writerow(["ARRIVAL TIME", "BURST TIME", "PRIORITY"])
            
            arrival_time = 0

            for i in range (0, 10 ** i):
                
                arrival_time += random.randint(0, 1)

                writer.writerow([arrival_time, random.randint(0, 100), random.randint(1, 3)])

def get_job_list(list_number: int, sort_key: tuple = None) -> list:
    """Read job list file into list.

    Args:
        list_number (int): List number
        sort_key (tuple): Key by which to sort list before returning

    Returns:
        list: Job list
    """
    with open(f"input/job_list_{list_number}.csv", "r") as job_list_in:
        
        # Read the file into a list, without the header
        job_list = [Job(x, y, z) for x, y, z in list(csv.reader(job_list_in))[1:]]
        
    return sorted(job_list, key = sort_key)

def make_graph() -> None:
    """Create graphs to visualize statistics."""
    
    # Initialize list to hold data
    data = dict()
    
    # For each of the job lists
    for list_number in [1, 2, 3, 4]:
        
        # Open the results file
        with open(f"output/job_list_{list_number}.csv", "r") as file_in:
            
            # Read file without header into list
            reader = list(csv.reader(file_in))[1:]
            
            # Add list to data with label
            data.update({f"job_list_{list_number}": reader})
            
        # For each record
        for job_list, stats in data.items():
            
            print([stat[0] for stat in stats])
            print([stat[1] for stat in stats])
            
            # Initialize bar plot
            fig = plt.figure(figsize=(10, 10))
            
            for x, y in stats:
                
                plt.bar(
                    x,    # Sort key
                    float(y),    # Turn around time
                    color = (0.6, 0.0, 0.9, 0.5),
                    width = 0.8,
                    align = "center",
                    label = y
                )
            
            # Make labels
            plt.xlabel("Sort keys")
            plt.xticks(rotation=20)
            plt.ylabel("Average Turn Around")
            plt.yscale('log')
            plt.title(f"Job List {list_number}")
            
            # Save figure
            plt.savefig(f"output/job_list_{list_number}.jpg")
            
            plt.clf()

# EXPERIMENTS =====================================================================================

# Ensure input directory exists
os.makedirs("input", exist_ok=True)

# Initialize job lists
initialize_job_lists()

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# For each of the job lists....
for list_number in [1, 2, 3, 4]:
    
    # Open results file for job list
    with open(f"output/job_list_{list_number}.csv", "w", newline="", encoding="utf-8") as job_list_results_file:
        
        # Initialize writer
        job_list_writer = csv.writer(job_list_results_file)
        
        # Write header
        job_list_writer.writerow(["Sort Key", "Average Turn Around"])
    
        # Communicate action
        print(f"Executing from job list {list_number}")
        
        # Define sort keys
        sort_keys = {
            "arrival":                  lambda job: (job.arrival),
            "arrival, priority":        lambda job: (job.arrival, job.priority),
            "arrival, burst":           lambda job: (job.arrival, job.burst),
            "arrival, priority, burst": lambda job: (job.arrival, job.priority, job.burst),
            "arrival, burst, priority": lambda job: (job.arrival, job.burst, job.priority),
        }
        
        # For each sort key
        for sort_key in sort_keys:
            
            # Communicate action
            print(f"\tExecuting on sort key: {sort_key}")
        
            # Read job list
            job_list = get_job_list(list_number, sort_keys[sort_key])
        
            # Create output directory for results
            os.makedirs(f"output/job_list_{list_number}", exist_ok=True)
            
            # Open results file for writing
            with open(f"output/job_list_{list_number}/{sort_key.replace(', ', '_')}.csv", "w", newline="", encoding="utf-8") as results_file:
                
                # Initialize writer
                results_writer = csv.writer(results_file)
                
                # Write header
                results_writer.writerow(["Job ID", "Arrival", "Burst", "Priority", "Start", "End", "Turn Around"])
                
                # Rest job IDs
                Job.job_id = itertools.count()
                    
                # Initialize the program counter
                pc = 0
                
                # Initialize turn around time tracking
                turn_around_times = 0
                
                # For each job in the job list...
                for job in job_list:
                    
                    # Record the job start time
                    job.start = pc
                    
                    # While the job has tasks to run...
                    while job.run_time < job.burst:
                        
                        # Increment the run time
                        job.run_time += 1
                        
                        # Increment the program counter
                        pc += 1
                        
                    # When the job completes, record it's end time
                    job.end = pc
                    
                    # Record wait time
                    job.wait = (job.end - job.arrival)
                    
                    # Record job statistics
                    results_writer.writerow([job.id, job.arrival, job.burst, job.priority, job.start, job.end, job.wait])
                    
                    # Update turn around time tracker
                    turn_around_times += job.wait
                    
                # Record job list's average turn around
                results_writer.writerow(["Average turn around time", (turn_around_times / len(job_list)), "", "", "", "", ""])
                
            # Print job statistics
            print(f"\t\tAverage job completion: {turn_around_times / len(job_list)}")
            
            # Record job list statistics
            job_list_writer.writerow([sort_key.replace(", ", "_"), (turn_around_times / len(job_list))])
            
# Create visualization of data
make_graph()