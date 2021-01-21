N, X = map(int, input().split())
m = [int(input()) for i in range(N)]
a = 0
if sum(m) < X:
  a = int((X - sum(m))/min(m))
print(N+a)
