
# 🔧 Utility Scripts Collection

A set of lightweight Python utilities for cloud management, security checks, and system monitoring.

## 📂 Included Tools

- AWS S3 Uploader (AWS_s3_uploader.py)

   Upload files to AWS S3 with ease.

- Docker Container Checker (Docker_container_checker.py)
 
   Check running containers and their statuses.

- Login Tracker (login_tracker.py)
  
   Monitor and log user login activity.

- Port Scanner (port_scanner.py)
  
  Scan open ports on a target system.

## Usage

Each script can be run independently:

    python script_name.py [options]

Example:

    python AWS_s3_uploader.py myfile.txt my-bucket


## 📦 Requirements

- Python 3.8+

- Install dependencies (if any):

      pip3 install -r requirements.txt

## Notes

- Configure AWS credentials before using the S3 uploader (~/.aws/credentials).

- Run port scans responsibly and only on systems you own or have permission to test.

- Docker must be installed and running for the container checker.
