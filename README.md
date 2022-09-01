# Task Manager
Task manager in Python using redis
FIFO method and Priority method is applied for adding new task
- task is based on redis hash
- FIFO queue is based on redis list
- Priority queue is based on sort set

## pre-setup
**install redis**
```sh
brew install redis
brew services restart redis
```
**python part**
```sh
pip install redis
```

## Basic usage
### worker
`add()` add a task into queue based on method choice of user
`get_list()` get all tasks from the queue based on method choice of user

## todo
- add argparse part to make user choice
- add unitest







## task

`{'task_priority': 'low', 'status': 'waiting', 'methods': 'fifo', 'started_at': 'Thu Sep 01 11:29:37  2022', 'goup': 'IT'}`