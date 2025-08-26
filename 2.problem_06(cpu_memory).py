# check the cpu and memory usages.
import psutil

def system_monitor():
    cpu = psutil.cpu_percent(interval=1)
    Memory = psutil.virtual_memory().percent
    print(f"CPU Usages: {cpu}%")
    print(f"Memory Usages: {Memory}%")

system_monitor()