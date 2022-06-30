import sys
import os
import subprocess
import psutil

# getting input
print('Specify the path of the file to be executed. To do that, copy the exact path to the executable file.')
path = input()

print('Provide the interval for logging the information in seconds (default is 1 sec).\n')
interval = int(input())

# file checks
if (! os.access(path, os.F_OK)):
    print('The path does not exist.')
if (! os.access(path, os.X_OK)):
    print('Not an executable!')

# start the execution and get PID:
pid = subprocess.Popen(path).pid

# other viable options are:
# subprocess.call(path)
# os.command(path)

# providing process for psutil to handle
p = psutil.Process(pid)
cpu = p.cpu_percent()
mem = p.memory_info()
rss = getattr(mem, 'rss')
vms = getattr(mem, 'vms')
if sys.platform.startswith('win'):
    num = p.num_handlers()
else:
    num = p.num_fds()
