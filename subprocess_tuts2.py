# From https://stackoverflow.com/questions/375427/a-non-blocking-read-on-a-subprocess-pipe-in-python

import sys
from subprocess import PIPE, Popen
from threading import Thread
from queue import Queue, Empty

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()
    
p = Popen(['grep', 'f'], stdout=PIPE, stdin=PIPE)
q = Queue()
t = Thread(target=enqueue_output, args=(p.stdout, q))
t.daemon = True
t.start()

p.communicate(input=b'for the love of KNOWLEDGE') 

print("q:",q.get())

# I am still not sure I understand subprocess, but I got a better handle of it. 
# Things I don't understand: WHen to use subprocess, here is a list of examples https://queirozf.com/entries/python-3-subprocess-examples
# Reading and writing to a process is still blurry
# In the example above not sure why the thread doesn't immediately close and cause an error for the p.communicate (because it is already closed)

