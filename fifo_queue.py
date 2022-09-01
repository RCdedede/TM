import logging

from redis_client import connector
from task import Task



class FIFOQueue():

    def __init__(self,queue_name='fifo_queue', maxq=5):
        """
        create a priority_queue
        set default of queue max=5
        """
        self.qkey = queue_name
        self.maxq = maxq

    def len_queue(self):
        return connector.llen(self.qkey)

    def is_empty(self):
        """
        check if queue is empty
        """
        return self.len_queue() == 0

    def is_max(self):
        """
        check if hit the max_limit of the queue
        """
        return self.len_queue() < self.maxq()

    def push(self, task_key):
        """
        tasks will be enqueue when status are waiting and the queue doesn't hit the max 
        add task to the tail of queue (push in from left)
        """
        task_key = Task.key()
        while not self.is_max:
            connector.lpush(self.qkey, task_key)
            logging.info(f"task: {task_key} is added into queue")

    def pop(self):
        """
        tasks will be dequeued from the head (pop out from right)
        """
        connector.rpop(self.qkey)


    def get_list(self):
        """
        return queue
        """
        return connector.lrange(self.qkey, 0, -1)
