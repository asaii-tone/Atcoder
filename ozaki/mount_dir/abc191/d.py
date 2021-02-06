import math
from decimal import Decimal
 
x, y, r = map(Decimal, input().split())
 
count = 0
 
for i_x in range(math.ceil(x-r), math.floor(x+r)+1):
  p = Decimal(r**2-(x-i_x)**2).sqrt()
  count += math.floor(y+p) - math.ceil(y-p) + 1
 
print(count)

# x, y, r = map(float, input().split())

# x_ue = 0
# x_sita = 0
# count = 0

# def ue(num):
#   if num > 0:
#     if(num == int(num)):
#       return int(num)
#     return int(abs(num)) + 1
#   else:
#     return int(abs(num)) * -1
# def sita(num):
#   if num > 0:
#     return int(abs(num))
#   else:
#     if(num == int(num)):
#       return int(abs(num))
#     return int(abs(num)+1) * -1

# # if(x-r == ue(x-r) and int(y) == y):
# #   count += 1
# # if(x+r == sita(x+r) and int(y) == y):
# #   count += 1

# for i_x in range(ue(x-r), sita(x+r)+1):
#   # print("i_x", i_x)
#   p = (r**2-(x-i_x)**2)**0.5
#   # print("p", p)
#   # if(int(p) == p):
#     # count += 1
#   for i_y in range(ue(y-p), sita(y+p)+1):
#     # print("i_y", i_y)
#     count += 1
#   # 0の文で+1
#   # count += sita(y+p) - ue(y-p) + 1

# print(count)
