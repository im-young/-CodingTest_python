# 1
E, S, M = map(int,input().split())

# 1 <= E <= 15
# 1 <= S <= 28
# 1 <= M <= 19

if E == S == M :
  print(E)

else :
  E_count = 0
  S_count = 0
  M_count = 0
  count = 0
  while True :
    count += 1
    E_count +=1
    if E_count == 16:
      E_count = 1
    S_count += 1
    if S_count == 29:
      S_count = 1
    M_count += 1
    if M_count == 20:
      M_count = 1
    
    if E_count == E and S_count == S and M_count == M:
      print(count)
      break