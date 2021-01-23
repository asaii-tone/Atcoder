N = int(input())
L = list(map(int, input().split()))

# 三角形の条件 a+b>c かつ b+c>a かつ c+a>b
count = 0
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      li, lj, lk = L[i], L[j], L[k]
      if(li != lj and li != lk and lj != lk):
        if(li+lj>lk and lj+lk>li and lk+li>lj):
          count += 1
print(count)

# n=int(input())
# s=[int(x) for x in input().split()]
# cnt=0
# for i in range(n):
#   for j in range(n):
#     for k in range(n):
#       if s[i]<s[j]<s[k] and s[i]+s[j]>s[k]:
#         cnt+=1
# print(cnt)
# 確かにコンビネーションを考えるからソートが必要になるがいくらなんでも強引では?w
# 同じ棒を選んでもそれは絶対に三角形にならないだろうという予想?
# 同じ棒を選んだら if の前半で False になるからいいんだ
