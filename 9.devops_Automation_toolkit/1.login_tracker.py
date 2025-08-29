def failed_login(log_file):
    with open(log_file,'r')as f:
        for line in f :
            if "Failed Password" in line:
                print("⚠️",line.strip())
            