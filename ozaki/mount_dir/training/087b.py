count = 0
x = [int(input()) for i in range(4)]
for i in range(x[0]+1):
  for j in range(x[1]+1):
    for k in range(x[2]+1):
      if 500*i+100*j+50*k == x[3]:
        count += 1
print(count)
