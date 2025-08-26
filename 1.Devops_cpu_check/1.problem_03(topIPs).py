from collections import Counter

def top_ips(log_file):
    with open(log_file,'r') as f:
        IPs = [line.split()[0]for line in f.readlines()]
        counter = Counter(IPs)
        for IP,count in counter.most_common(5):
            print(IP,'->',count)
top_ips("3.1.access_03.1.log") 