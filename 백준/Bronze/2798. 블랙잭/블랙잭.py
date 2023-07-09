N ,M = map(int,input().split())
card_num = list(map(int,input().split()))

## 카드 3장의 합의 모든 경우의 수
hap = []
for i in range(N-2):
  for j in range(i+1,N-1): 
    for k in range(j+1,N):
       card_hap = card_num[i]+card_num[j]+ card_num[k]
      #  if card_hap in hap: 
      #   continue
       hap.append(card_hap)

## # 3장의 합이 M이하면서 가장 큰수
card_max = []
for i in range(len(hap)):
  if hap[i]<=M:
    card_max.append(hap[i])

print(max(card_max))


