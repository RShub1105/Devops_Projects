import psutil
import time
import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

THRESHOLD = 80
LOG_FILE = "7.1.system_report.log"
SLACK_WEBHOOK = ""
SENDER = "Your_emails@gmail.com"
PASSWORD = "Your_app_password"
RECEIVER = "reciver_email@gmail.com"

def send_slack_alert(message):
    if SLACK_WEBHOOK:
        requests.post(SLACK_WEBHOOK,json={"text":message})
        print("Slack Alert Sent")
def send_email_alert(subject,body):
    if not SENDER or not PASSWORD:
        return
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["Form"] = SENDER
    msg["To"] = RECEIVER
    with smtplib.SMTP('smtp.gmail.com',587) as server:
        server.starttls()
        server.login(SENDER,PASSWORD)
        server.sendmail(SENDER,RECEIVER,msg.as_string())
    print("Email alert sent")

def monitor_system():
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        log_entry = f"{datetime.now()}|CPU:{cpu}%|MEMORY:{memory}%|DISK:{disk}%\n"
        with open(LOG_FILE,'a') as f:
            f.write(log_entry)

        print(log_entry.strip())

        if cpu>THRESHOLD or memory>THRESHOLD or disk>THRESHOLD:
            alert_message = f"🚨Alert! CPU = {cpu}%, MEMORY = {memory}%, DISK = {disk}%"
            send_slack_alert(alert_message)
            send_email_alert("🚨System Alert!",alert_message)

if __name__ == "__main__":
    print("MINI monitoring System Started.....")
    while True:    
        monitor_system()  
        time.sleep(10)
 