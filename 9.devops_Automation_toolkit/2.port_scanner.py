import socket

def scan_ports(host,ports=[22,80,443]):
    for port in ports:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host,port))
        if result == 0:
            print(f"✅ Port{port} open on {host}")
        else:
            print(f"‼️ Port {port} closed on {host}")
        s.close()
scan_ports("127.0.0.1")