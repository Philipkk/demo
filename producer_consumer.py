import multiprocessing as mp
from random import choice
import os

def producer(goods, oput, loop_count=8):
    for i in range(loop_count):
        selected = choice(goods)
        oput.put(selected)
        print('{0} {1:<10} in store PID: {2}'.\
              format(i, selected, os.getpid()))

def consumer(iput):
    while True:
        purchase = iput.get()
        print('{0:>20} sold out! PID: {1}'.\
              format(purchase, os.getpid()))
        iput.task_done()

ex_queue = mp.JoinableQueue()
for i in range(2):
    p = mp.Process(target=consumer, args=(ex_queue,))
    p.daemon = True
    p.start()

cheese=['Edam', 'Graskaas', 'Gouda', 'Leerdammer',\
        'Leyden', 'Limburger', 'Maasdam', 'Nagelkaas']
producer(cheese, ex_queue)
ex_queue.join()
