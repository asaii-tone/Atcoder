# N = int(input())
# a = N%11
# if a%4 == 0:
#   print("Yes")
# elif a%7 == 0:
#   print("Yes")
# else:
#   print("No")
# ダメなパターンが分からん

N = int(input())
for i in range(int(N/7)+1):
  a = N-7*i
  if a%4 == 0:
    print("Yes")
    exit()
print("No")
