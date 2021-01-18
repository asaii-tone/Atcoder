x = [int(i) for i in input().split()]
out = 0
for i in range(1, x[0]+1):
  sumx = 0
  a = map(int, str(i))
  for j in a:
    sumx += j
  if x[1] <= sumx <= x[2]:
    out += i
print(out)
