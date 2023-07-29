
N = int(input())
s = []
c = []
for _ in range(N):
    c.append(input().split(' '))

for l in c:
    commend = l[0]
    num = 0 if len(l) == 1 else int(l[1])
    if commend == 'top':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
    elif commend == 'size':
        print(len(s))
    elif commend == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif commend == 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif commend == 'push':
        s.append(num)