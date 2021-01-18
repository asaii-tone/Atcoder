N, Y = map(int, input().split())
flag = 1
for i in range(N+1):
  for j in range(N-i+1):
    # 残りの枚数なんかfor文回さなくても確定なの確かに
   k = N-i-j
   if 10000*i+5000*j+1000*k == Y:
     print(i, j, k)
     exit()
print("-1 -1 -1")

# 途中までしか正解にならなかった
# N, Y = map(int, input().split())
# flag = 1
# for i in range(N+1):
#   for j in range(N-i+1):
#     for k in range(N-i-j+1):
#       if 10000*i+5000*j+1000*k == Y:
#         print(i, j, k)
#         flag = 0
#         break
#     if flag == 0:
#       break
#   if flag ==0:
#     break
# if flag:
#   print("-1 -1 -1")
