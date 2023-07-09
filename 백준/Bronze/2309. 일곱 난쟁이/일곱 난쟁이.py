# 규리
# 9명 중에 7명을 찾는게 아니라 9명 중 2명을 찾는 것
height_list = []
height_sum = 0
for i in range(9):
    height = int(input())
    height_list.append(height)
    height_sum += height
height_list.sort()

is_ok = False
for first in range(9):
    for second in range(9):
        if first == second:
            continue
        if (height_sum-height_list[first]-height_list[second]) == 100:
            height_list.remove(height_list[second])
            height_list.remove(height_list[first])
            is_ok = True
        if is_ok:
            break
    if is_ok:
        break

for i in height_list:
    print(i)