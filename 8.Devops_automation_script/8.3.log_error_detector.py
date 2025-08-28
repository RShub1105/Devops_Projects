def scan_errors(log_file):
    with open(log_file,"r") as f, open("error_report.log","w") as out:
        for line in f:
            if "ERROR" in line:
                out.write(line)
                print("⚠️ Error found:",line.strip()) 
scan_errors("system.log") 