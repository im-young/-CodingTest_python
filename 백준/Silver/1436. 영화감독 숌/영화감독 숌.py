# 3
N = int(input())

num = ['666']
start = 666
plus = 0

while len(num) < N :
  plus += 1
  num_plus = str(start + plus)
  if '666' in num_plus:
    num.append(num_plus)

print(int(num[-1]))
