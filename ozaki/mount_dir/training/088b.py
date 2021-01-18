N = int(input())
A = [int(i) for i in input().split()]

A.sort(reverse=True)
alice = 0
bob = 0
for i in range(N):
  if i%2 == 0:
    alice += A[i]
  else:
    bob += A[i]
print(alice - bob)
