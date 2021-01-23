# N = int(input())
# a = N%11
# if a%4 == 0:
#   print("Yes")
# elif a%7 == 0:
#   print("Yes")
# else:
#   print("No")
# 25 が反例 7*3+4 で Yes なのに 11*2+3 で No になる

N = int(input())
for i in range(int(N/7)+1):
  a = N-7*i
  if a%4 == 0:
    print("Yes")
    exit()
print("No")
