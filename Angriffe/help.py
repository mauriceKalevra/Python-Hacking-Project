import subprocess
import sys
import time
from os import system
arg = "root"
child_proccess = subprocess.Popen(["scp", "SW.py", "root@172.17.0.2:/root"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
time.sleep(1)
child_process_output = child_proccess.communicate(b'root')
print(child_process_output)
