import logging

from redis_client import connector
from task import Task



class PriorityQueue():

    def __init__(self,queue_name='priority_queue', maxq=5):
        """
        create a priority_queue
        set default of queue max=5
        """
        self.qkey = queue_name
        self.maxq = maxq

    def len_queue(self):
        return connector.zcard(self.qkey)

    def is_empty(self):
        """
        check if queue is empty
        """
        return self.len_queue == 0
    
    def is_max(self):
        """
        check if hit the max_limit of the queue
        """
        return self.len_queue < self.maxq

    def push(self, score=Task.get_priority(), member=Task.key()):
        while not self.is_max:
          connector.zadd(self.qkey, score, member)
          logging.info(f"task: {member} is added into queue")

    def pop(self):
        score = None
        member = None
        result = connector.ZREVRANGE (self.qkey, 0, -1, withscores=True)
        # [( member, score), (member, score), ...]
        if result:
            member, score = result[0]
            ret = connector.zrem(self.key, member)
            assert ret == 1
        return score, member

    def get_list(self):
        return connector.ZREVRANGE (self.qkey, 0, -1, withscores=True)
