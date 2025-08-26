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


🚀 Features

1. Log Analysis

       Extracts top IP addresses from access logs (1.problem_03(topIPs).py).

       Helps identify suspicious or frequent traffic sources.

2. Resource Monitoring

       CPU & memory monitoring (2.problem_06(cpu_memory).py).

       Disk usage monitoring (3.problem_09(disk usages).py).

       Stores results in structured log files (4.1system_log_12.1.txt, 7.1.system_report.log).

3. Automation

       Automated disk usage alerts (4.problem_12(Automated_disk).py).

       Configurable thresholds for proactive monitoring.

4. Alert System

       Email alerts (5.problem_15(send_email_alert).py).

       Slack alerts (6.slack_alert.py).

       Ensures admins are notified immediately when resources exceed safe limits.

6. All-in-One Monitoring

        7.Mini_monetring_system.py combines CPU, memory, and disk monitoring with logging.

       Acts as the central monitoring script.

# 1. Clone Repository

 git clone https://github.com/your-repo/mini-monitoring-system.git
 cd mini-monitoring-system

# 2. Install Requirements

    pip3 install psutil requests smtplib

# 3. Run Individual Scripts

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





