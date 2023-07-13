Count = int(input())

List =[] # 색종이 좌표 시작


for _ in range(Count):
  coordinate =list(map(int,input().split())) # coordinate: 좌표
  List.append(coordinate)

# 도화지 : 100* 100 칸 만들기
#list18 = [[0 for j in range(1, 6, 1)] for i in range(1,3,1)]
big_paper = [[0 for j in range(100)] for i in range(100)]

# 사각형 만들기


for i in range(len(List)): 
   coordinate= List[i] # 좌표
   y = coordinate[0] # 가로
   x = coordinate[1] # 세로
   for color_height in range(x,x+10): # 도화지에 색종이 크기 만큼 
    for color_widht in range(y,y+10):
      big_paper[color_height][color_widht] = 1 # 색종이가 있는 부분(1)과 없는부분을 구분 (0)

#  답1
# # print(sum(big_paper, [])) # array 배열을 한 리스트로 바꿔줌
# print(sum(sum(big_paper, []))) # 리스트로 바꾼 것을 sum 하는 것

# 답2
result = 0
for i in big_paper:
  result += sum(i)
print(result)