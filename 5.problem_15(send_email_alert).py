import psutil
import smtplib
from email.mime.text import MIMEText
SENDER = "Your_email@gmail.com"
PASSWORD = "Yout_app_passoword"
RECEVIER = "receiver_email@gmail.com"
def send_email_alert(subject,body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = RECEVIER
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(SENDER,PASSWORD)
        server.sendmail(SENDER,RECEVIER,msg.as_string())
        print("Alert email sent!")
def monitor():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    if cpu>80 or memory>80 or disk>80:
        subject = "‼️ System Alert"
        body = f"CPU:{cpu} | Memory:{memory}% | Disk:{disk}% \n"
        send_email_alert(subject,body)
    else:
        print("system 🆗")
monitor()