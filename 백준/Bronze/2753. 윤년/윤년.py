y = int(input())

if y % 4 == 0 and y % 100 != 0: 
  yoon = 1
  print(yoon)
elif y % 100 == 0 and y % 400 == 0 :
  yoon = 1
  print(yoon) 
else : 
  yoon = 0
  print(yoon)