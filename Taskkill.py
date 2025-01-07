import subprocess
import sys

def run_process(id):

    command = [
        "taskkill",
        "/F",
        "/PID", "{}".format(id)
    ]
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    import Server
    Server.Server("Cancel")

run_process(sys.argv[1])