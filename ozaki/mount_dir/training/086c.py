N = int(input())
count = 0
dt, dx, dy = 0, 0, 0
for i in range(N):
    t, x, y = map(int, input().split())
    if abs(x-dx)+abs(y-dy) <= t-dt and t%2 == (x+y)%2:
      count += 1
    dt, dx, dy = t, x, y
print("Yes" if count == N else "No")

# うまくいくところもあるけど行かないところもある ロジックがおかしい
# N = int(input())
# S = [list(map(int, input().split())) for i in range(N)]
# T = [S[i][0] for i in range(N)]
# X = [S[i][1] for i in range(N)]
# Y = [S[i][2] for i in range(N)]

# for i in range(N):
#   if (X[i] + Y[i])%2 != T[i]%2:
#     print("No")
#     exit()
# print("Yes")
