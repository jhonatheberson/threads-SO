import threading, time

from enlargement import enlargement
from equalization import equalization




# Start a pool of 2 workers

t = threading.Thread(target=enlargement, name='enlargement')
t.start()
q = threading.Thread(target=equalization, name='equalization')
q.start()



# Give threads time to run
print('Main thread sleeping')
time.sleep(2)