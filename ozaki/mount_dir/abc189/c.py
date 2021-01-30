n = int(input())
a = list(map(int, input().split()))

# count_max = 0
# for i in range(1, n):
#   # スライスの大きさ i
#   for j in range(n):
#     # スライスのスタート j
#     b = a[j:j+i]
#     # print(a)
#     # print(b)
#     count_min = min(b)
#     tmp_max = count_min*len(b)
#     # print(tmp_max)
#     if(count_max < tmp_max):
#       count_max = tmp_max
# print(count_max)

# count_max = 0
# for i in range(1, n):
#   for j in range(n):
#     b = a[j:j+i]
#     count_min = min(b)
#     tmp_max = count_min*len(b)
#     if(count_max < tmp_max):
#       count_max = tmp_max
# print(count_max)

# これで解ける
# ある地点から 後ろを調べる
# ある地点からlenが1, 2, 3ってやって それぞれの時の最小値かける皿の枚数ってやる
ans = 0
for i in range(n):
    minh = 1000000
    for j in range(i, n):
        minh = min(minh, a[j])
        ans = max(ans, minh * (j + 1 - i))
print(ans)
