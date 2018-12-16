from collections import deque

list1 = deque([11, 22, 33])
print(list1)
list1.append(66)
list1.popleft()
print(list1)
