from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

queue = deque([])


for _ in range(n):
    i = sys.stdin.readline().rstrip()

  #push
    if 'push' in i :
        X= int(i.split(' ')[1])
        queue.append(X)
    
    # pop
    if i == 'pop':
        # try:
        if len(queue) != 0:
            pop = queue.popleft()
            print(pop)
        else :
            print(-1)
        # except IndexError:
        #   print(-1) # list가 비면 -1
    
    #size # 오류나면 정수일떄 조건문 넣어보기
    if i =='size':
        print(len(queue))
        # elif len(queue) == 0 :
        #   print(-1)


    #empty
    if i =='empty':
        if len(queue) == 0: 
            print(1)
        else :
            print(0)

        
    # front
    if i == 'front':
        if len(queue) != 0 :
            print(queue[0])
        else:
            print(-1)


    # back
    if i == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else: 
            print(-1)
