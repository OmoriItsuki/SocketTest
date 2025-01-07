import subprocess

def run_process():
    command = [
        r"C:\Users\kinok\AppData\Local\Programs\Python\Python37-32\python.exe",
        "TempProcess.py",
    ]
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("process id: " + str(process.pid))

    while True:
        if(process.poll() is not None):
            import Client
            Client.Client()
            break
        line = process.stdout.readline()
        if line:
            print(line.decode().strip())

run_process()