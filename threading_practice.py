"""
Possible states of a thread:

New: thread hasn't been started yet and no resources allocated
Runnable: thread is waiting to run
Running: thread is being executed
Not-running: Thread has been paused because another thread took precedence
Finished: thread has finished execution 
"""

import threading 

# instantiate object of Thread class with a target function

def myTask():
   print("Hello World: {}".format(threading.current_thread()))

myFirstThread = threading.Thread(target=myTask)

myFirstThread.start()