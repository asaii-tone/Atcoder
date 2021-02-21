a, b, c = map(int, input().split())

rot_0 = [0]
rot_1 = [1]
rot_2 = [2, 4, 8, 6] 
rot_3 = [3, 9, 7, 1]
rot_4 = [4, 6]
rot_5 = [5]
rot_6 = [6]
rot_7 = [7, 9, 3, 1]
rot_8 = [8, 4, 2, 6]
rot_9 = [9, 1]
rot_kind = [rot_0, rot_1, rot_2, rot_3, rot_4, rot_5, rot_6, rot_7, rot_8, rot_9]

int_n = int(str(a)[-1])
rot_kind_n = rot_kind[int_n]
b_next = b%len(rot_kind_n)
c_next = c%len(rot_kind_n)
if b_next == 0 or c_next == 0:
  print(rot_kind_n[0])
  exit()
bc_next = b_next**c_next
n = bc_next%len(rot_kind_n)
print(rot_kind_n[n-1])

# nn = b**c
# int_n = int(str(a)[-1])

# if nn == 1:
#   print(int_n)
#   exit()
# for i in range(nn):
#   str_n = str(int_n*a)[-1]
#   int_n = int(str_n)
# print(int_n)

# rot_flag = False
# rot_list = [a]

# for i in range(2, nn):
#   str_n = str(rot_list[i-2]*a)[-1]
#   int_n = int(str_n)
#   rot_list.append(int_n)

#   if int_n == rot_list[0]:
#     sa = i-0
#     if sa*2 > len(rot_list):
#       continue
#     else:
#       count = 0
#       for j in range(sa):
#         if rot_list[j] == rot_list[j+sa] and rot_flag:
#           count += 1
#         else:
#           rot_flag = False
#           break
#       if count == sa:
#         break


#   if rot_flag:
#     break

# print(rot_list)
# del rot_list[0]
# print(rot_list)

# l = len(rot_list)
# print(l)
# num = nn%l
# print(num)
# ans = rot_list[num-1]
# print(ans)
