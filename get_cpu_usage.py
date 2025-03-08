import time
# write a python code to get the current CPU usage of a linux system and save the data in a csv file
def get_cpu_usage():
    import psutil
    import csv
    import time
    import os
    import datetime

    # get the current time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # get the current cpu usage
    cpu_usage = psutil.cpu_percent()
    # get the current memory usage
    mem = psutil.virtual_memory()
    mem_usage = mem.percent

    # if the file does not exist, create a new file and write the header
    if not os.path.exists('cpu_usage.csv'):
        with open('cpu_usage.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Time', 'CPU Usage', 'Memory Usage'])

    # write the data to the csv file
    with open('cpu_usage.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, cpu_usage, mem_usage])

    print('Data written to cpu_usage.csv')

# run the function every 5 seconds
while True:
    get_cpu_usage()
    time.sleep(5)

