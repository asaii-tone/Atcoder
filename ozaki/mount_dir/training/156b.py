n, k = map(int, input().split())

count = 1
while True:
  if(n<k):
    print(count)
    exit()
  n = int(n/k)
  count += 1


# n, k = map(int, input().split())
 
# count = 1
# tmp = int(n/k)
# while True:
#   if(tmp<k):
#     count += 1
#     print(count)
#     exit()
#   tmp = int(tmp/k)
#   count += 1
