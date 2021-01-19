N = int(input())
count = 1
while True:
  if N < count * 2:
    print(count)
    exit()
  count = count * 2
