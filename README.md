├── 1.1.access_03.log              # Sample access log file

├── 1.problem_03(topIPs).py        # Script to analyze top IPs from access logs

├── 2.problem_06(cpu_memory).py    # Script to monitor CPU and memory usage

├── 3.problem_09(disk usages).py   # Script to monitor disk usage

├── 4.1system_log_12.1.txt         # System performance log (CPU, Memory, Disk)

├── 4.problem_12(Automated_disk).py # Automated disk usage monitoring & alerts

├── 5.problem_15(send_email_alert).py # Script to send email alerts

├── 6.slack_alert.py               # Script to send alerts via Slack

├── 7.1.system_report.log          # Daily system report log

├── 7.Mini_monetring_system.py     # Combined monitoring system script        

|-  8.Devops_automation_script     # A versatile DevOps automation script.

|-- 9.devops_Automation_toolkit    # A comprehensive collection of DevOps automation tools.


# 🚀 Features

#### 💻 Mini Monitoring System (7.Mini_monetring_system.py)

- This is the heart of the repository. It's an all-in-one script that combines multiple monitoring functions into a single, easy-to-run tool. It can monitor CPU, memory, and disk usage, and analyze log files to find top IPs,        providing a complete view of your system's health.


#### 🤖 DevOps Automation Toolkit (9.devops_Automation_toolkit)
- This toolkit contains a series of scripts designed to automate common DevOps tasks. It's an extensible framework you can use to streamline your workflows, from deployment to routine maintenance.

## 1. Clone Repository

 git clone https://github.com/your-repo/mini-monitoring-system.git
 cd mini-monitoring-system

## 2. Install Requirements

    pip3 install psutil requests smtplib

## 3. Run Individual Scripts

- Analyze top IPs:

      python3 1.problem_03(topIPs).py 1.1.access_03.log
		
- Monitor CPU & Memory:

      python3 2.problem_06(cpu_memory).py

- Check Disk Usage:

      python3 3.problem_09(disk usages).py
		
- Automated Disk Alerts:

      python3 4.problem_12(Automated_disk).py

- Send Email Alerts:

  	  python3 5.problem_15(send_email_alert).py

- Send Slack Alerts:

      python3 6.slack_alert.py

- Run Full Monitoring System:

      python3 7.Mini_monetring_system.py


# 📊 Sample Logs

- Access Log (1.1.access_03.log):

      203.0.113.99 - - [20/Aug/2025:14:06:55 +0000] "GET /admin HTTP/1.1" 403 215


- System Log (4.1system_log_12.1.txt):

      2025-08-25T10:14:05 | CPU:16.6% | Memory:56.0% | Disk:2.5%


- System Report (7.1.system_report.log):

      2025-08-26 12:48:05 | CPU:16.0% | MEMORY:57.2% | DISK:2.5%
 
# 🔔 Alerts

- Email Alerts require SMTP configuration (update credentials inside

      5.problem_15(send_email_alert).py).

- Slack Alerts require a webhook URL (configure in 6.slack_alert.py).


#📌 Future Improvements

- Add real-time dashboard for system metrics.

- Extend log analysis to detect brute-force attempts.

- Dockerize monitoring system for portability.




