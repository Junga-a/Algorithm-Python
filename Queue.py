#선입선출
from collections import deque #큐를 구현하기 위해 deque라이브러리 사용

Queue=deque()

Queue.append(5)
Queue.append(2)
Queue.append(3)
Queue.append(7)
Queue.popleft()  #6번 줄의 5가 삭제
Queue.append(1)
Queue.append(4)
Queue.popleft()  #7번 줄의 2가 삭제

print(Queue)
Queue.reverse()
print(Queue)