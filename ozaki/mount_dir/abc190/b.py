n, s, d = map(int, input().split())
xy = [list(map(int, input().split())) for i in range(n)]

flag = False
for i in range(n):
  if xy[i][0] < s and xy[i][1] > d:
    flag = True
    break

if(flag):
  print("Yes")
else:
  print("No")
