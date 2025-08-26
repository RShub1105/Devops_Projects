import psutil
import time
from datetime import datetime
def log_system_status():
    with open("12_system_log_12.1.txt","a") as f:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage("/").percent

            log = f"{datetime.now()} | CPU:{cpu}% | Memory:{memory}% | Disk:{disk}% \n"
            f.write(log)
            f.flush()
            print("Logged",log.strip())
            time.sleep(10)
log_system_status()
