from enum import Enum

class Methods():
    FIFO = 'fifo' 
    PRIORITY = 'priority'

class TaskPriority(Enum):
    """
    example:
        score = TaskPriority.LOW
        score.name => LOW, type:<class 'str'>
        score.score => LOW, type:<class 'int'>
    """
    LOW = 0
    MEDIUM = 1 
    HIGH = 2

class Status():
    WAITING = 'waiting'
    RUNNING = 'running' 
    KILLED = 'killed'