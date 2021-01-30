n, x = map(int, input().split())
vp = [list(map(int, input().split())) for i in range(n)]

# total = 0
# for i in range(n):
#   total += vp[i][0] * vp[i][1] / 100
#   if(x < total):
#     print(i+1)
#     exit()
# print(-1)

# al = 0
# for i in range(n):
#   if(al <= x):
#     al += vp[i][0] * vp[i][1] / 100
#     print(i+1)
#     exit()
# print(-1)

total = 0
for i in range(n):
  total += vp[i][0] * vp[i][1]
  if x*100 < total:
    print(i+1)
    exit()
print(-1)
