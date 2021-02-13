t = int(input())

for i in range(t):
  ans = 0
  l, r = map(int, input().split())
  # ver04
  n = r-l-l+1
  if n > 0:
    ans = (1/2) * n * (n+1)
  else:
    ans = 0
  print(int(ans))

  # n = 0
  # while(r-n-l-l >= 0):
  #   # print(r-n-l-l)
  #   ans += r-n-l-l+1
  #   n += 1

  # ver02
  # ans = 1/2 * (r-l-l-1) * (1+r-l-l)
  # ver03
  # ans = 1/2 * (r-l-l+1) * (r-l-l-1+1)
