'''

1.input으로 들어온 값 리스트 만들기
2. dict 만들기 
3. (input[0][0] + input[1][0])*input[2][1]
'''
# input
in_li = []
for i in range(3):
  in_li.append(input())

# 1. dict 만들기

color = {
    'black':	[0, 1],
    'brown':[1,10],
    'red': [2, 100],
    'orange':[3, 1000],
    'yellow':	[4,	10000],
    'green':[5,	100000],
    'blue':[6, 1000000],
    'violet':	[7,	10000000],
    'grey':	[8, 100000000],
    'white':	[9, 1000000000]}

  
R = str(color[in_li[0]][0])+ str(color[in_li[1]][0])
result = int(R)*color[in_li[2]][1]
print(result)
