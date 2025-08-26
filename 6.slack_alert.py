import psutil
import requests

WEBHOOK_URL = "https://hooks.slack.com/services/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"

def slack_alert(message):
    payload = {"text" : message }
    requests.post(WEBHOOK_URL,json=payload)

def monitor():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    if cpu>80 or memory>80 or disk>80:
        message = f"🚨Alert CPU:{cpu}%,MEMORY:{memory}%,DISK:{disk}%"
        slack_alert(message)
    else:
        print("systme is 🆗")
monitor()