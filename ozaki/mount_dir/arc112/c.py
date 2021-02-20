n = int(input())
p = list(map(int, input().split()))
weight = [0] *n
ans = 1
count = 0

for i in p:
  weight[i] += 1

getflag = True
for i in weight:
  if i == 0:
    count = 0
    continue
  else:
    count += 1
  if i%2 == 0:
    if getflag:
      ans += i/2
    getflag = not getflag
    if count%2 == 1:
      getflag = not getflag
  if getflag:
    ans += i
  print(weight)
  print(i)
  print(ans)
  print("count", count)

# print(weight)
print(int(ans))

# 7
# 1 1 2 2 3 3
# [0, 2, 2, 2, 0, 0, 0]
# 7
# 1 1 2 2 4 4
# [0, 2, 2, 0, 2, 0, 0]
# この2個は木の構造が違うが同じように扱ってしまっているのが問題
# 例3
# 10
# 1 1 3 1 3 6 7 6 6
# [0, 3, 0, 2, 0, 0, 3, 1, 0, 0]
# 数字の連続回数が深さなのでは?
# そんで今回深さが2だから同じ人

# ver01
# n = int(input())
# p = list(map(int, input().split()))
# weight = [0] *n
# ans = 1

# for i in p:
#   weight[i] += 1

# getflag = True
# for i in weight:
#   if i == 0:
#     continue
#   if i%2 == 0:
#     if getflag:
#       ans += i/2
#     getflag = not getflag
#   if getflag:
#     ans += i
#   print(weight)
#   print(i)
#   print(ans)

# # print(weight)
# print(int(ans))
