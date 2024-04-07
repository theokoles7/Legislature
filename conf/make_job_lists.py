"""Initialize job lists."""

import csv, random

for i in [1, 2, 3, 4]:

    with open(f"conf/job_lists/job_list_{i}.csv", "w", newline = "", encoding = "utf-8") as file_out:

        writer: csv.writer =    csv.writer(file_out)

        writer.writerow(["ARRIVAL TIME", "BURST TIME", "PRIORITY"])
        
        arrival_time = 0

        for i in range (0, 10 ** i):
            
            arrival_time += random.randint(0, 1)

            writer.writerow([arrival_time, random.randint(0, 100), random.randint(1, 3)])