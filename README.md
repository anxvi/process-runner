WHAT IS process-runner?

The pet project for running processes and checking the resourses it consumes.

WHAT IT'S SUPPOSED TO BE ABLE TO DO
- run the process from an executable
- check the percantage of CPU, the amount of RSS and VMS, as well as the number of handlers or fds (depending on the system) used by the process
- log those values with chosen intervals

TO-DO: 
- output the CPU / RAM / handlers info with chosen interval (ping-like?)
- logging the CPU / RAM / handlers info into file with chosen interval
- testing and debugging
- choose the most appropriate option for running the executable

WHAT MAY BE NICE: 
- some flag to force-stop the process ?
- stop the process on timer ?
- return the exit code ?
