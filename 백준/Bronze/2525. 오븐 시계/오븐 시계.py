h, m = map(int,input().split())
time = int(input())

time_h = h 
time_m = m + time

if time_m > 60 :
  time_h = time_h +(time_m // 60) 
  time_m = time_m % 60
  if time_h > 23:
      time_h  = time_h - 24

elif time_m == 60 :
  time_h += 1
  time_m = 0
  if time_h > 23:
      time_h  = time_h - 24

elif time_m < 0:
  time_h -=1
  time_m = 60 + time_m
  if time_h > 23:
      time_h  = time_h - 24



print (time_h,time_m,sep = ' ')