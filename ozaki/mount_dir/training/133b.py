import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]

count = 0
for i in range(N-1):
  for j in range(1, N-i):
    sum = 0
    for k in range(D):
      sum += math.pow(X[i][k]-X[i+j][k], 2)
    if(math.sqrt(sum).is_integer()):
      count += 1
print(count)

# range を回数だと思いすぎたが range(2番目, 最後まで) でも良かった
