x, m = [int(input()) for i in range(2)]

a = list(str(x))
b = list(map(int, a))
d = int(max(b))
# print(d)

# def Base_n_to_10(str_X, n):
#     out = 0
#     for i in range(1,len(str(str_X))+1):
#         out += int(str_X[-i])*(n**(i-1))
#     return out

# x = str(x)
# n = d
# count = 0
# while True:
#   n += 1
#   convert_nTo10 = Base_n_to_10(x, n)
#   # print(convert_nTo10)
#   if convert_nTo10 > m:
#     break
#   count += 1
# print(count)

# x = str(x)
# m = str(m)
# count = 0
# by2 = 2
# while True:
#   print("by2", by2)
#   if d+1 > by2:
#     by2 = by2**2
#     print("コンティニュー?")
#     continue
#   print("変換元", int(x, by2))
#   print("最大値", int(m, by2))
#   if int(x, by2) < int(m, by2):
#     print("どうや", by2)
#   by2 = by2**2



# tmp = "9"*60
# print(int(tmp, 32))
