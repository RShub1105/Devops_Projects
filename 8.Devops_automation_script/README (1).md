
# Python Utilities Collection

A set of essential and minimal Python scripts for everyday system maintenance.
Each script is standalone, requires only Python 3, and avoids heavy dependencies.

## Scripts

1. 🧹 Old File Cleaner (8.1.old_file_cleaner.py)

- Removes files older than a defined number of days.

- Useful for cleaning up temporary or log directories.

### Usages

    python3 8.1.old_file_cleaner.py /path/to/dir --days 30

2. 🔄 Service Restarter (8.2.service_restarter.py)

- Monitors a service and restarts it if it stops running.

- Works well for lightweight process supervision.

### Usages

    python3 8.2.service_restarter.py myservice

3. 📜 Log Error Detector (8.3.log_error_detector.py)

- Scans a log file for error keywords (e.g., "ERROR", "CRITICAL").

- Prints matches and can be extended for alerts.

### Usages

    python3 8.3.log_error_detector.py /var/log/myapp.log

### Requirements

- Python 3.6+

- No external dependencies

## Philosophy

- Minimal: No extra packages, no complexity.

- Practical: Scripts solve real, common system admin tasks.

- Composable: Can be combined into cron jobs or automation pipelines.

## Examples

- Clean /tmp daily:

    0 2 * * * python3 /path/to/8.1.old_file_cleaner.py /tmp --days 7

- Keep a service alive:

    */5 * * * * python3 /path/to/8.2.service_restarter.py nginx

- Watch logs for issues:

    tail -f /var/log/app.log | python3 /path/to/8.3.log_error_detector.py


