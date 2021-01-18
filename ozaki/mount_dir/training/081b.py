rows = int(input())
x = [int(i) for i in input().split()]
count = 0
while all(i%2 == 0 for i in x):
  x = [i/2 for i in x]
  count += 1
print(count)
