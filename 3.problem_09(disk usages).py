import psutil
def system_info():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint).percent
            if usage > 80:
                print(f"Alert 🚨:{partition.device}is{usage}%full")
            else:
                print(f"{partition.device}is ok ({usage}%)")
        except PermissionError:
            continue
system_info()
