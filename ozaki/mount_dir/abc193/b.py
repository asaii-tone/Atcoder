n = int(input())
d = [list(map(int, input().split())) for i in range(n)]

# 問題条件の最大値
place_min = 1000000000
min_flag = False
for i in range(n):
  a = d[i][0]
  p = d[i][1]
  x = d[i][2]
  if x - a > 0:
    if p < place_min:
      place_min = p
      min_flag = True

if min_flag:
  print(place_min)
else:
  print(-1)
