import subprocess

def docker_status():
    result = subprocess.run(["docker","ps"], capture_output= True,text=True)
    print(result.stdout)
docker_status()