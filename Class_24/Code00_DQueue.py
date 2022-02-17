from collections import deque

queue = deque(['hello', 'world'])
queue.append('python')
queue.append('go')
queue.append('java')
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)
queue.appendleft('c')
print(queue)
queue.append('c++')
print(queue)

queue.rotate()
print(queue)
