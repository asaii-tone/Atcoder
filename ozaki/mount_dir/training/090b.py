A, B = map(int, input().split())

count = 0
for i in range(1, 10):
  for j in range(10):
    for k in range(10):
      num = i*10000+j*1000+k*100+j*10+i
      if(A<=num<=B):
        count += 1
print(count)
