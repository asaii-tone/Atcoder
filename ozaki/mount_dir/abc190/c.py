# n, m = map(int, input().split())

# wait = [0]*(n+1)
# out = set(range(n+1))
# for i in range(m):
#   a, b = map(int, input().split())
#   wait[a] += 1
#   wait[b] += 1

# k = int(input())
# for j in range(k):
#   c, d = map(int, input().split())
#   if c in out or d in out:
#     if wait[c] <= wait[d]:
#       if d in out:
#         out.discard(d)
#       elif c in out:
#         out.discard(c)
#     elif wait[c] > wait[d]:
#       if c in out:
#         out.discard(c)
#       elif d in out:
#         out.discard(d)

# for nil in out:
#   wait[nil] = m

# print(m - min(wait))


# コピペのやつ
import itertools

# N:皿の数, M:条件数
N, M = [int(x) for x in input().split()]

# 条件リスト
ab_list = []
for i in range(M):
    a, b = [int(x) for x in input().split()]
    ab_list.append((a, b))

# 皿にボールを置く人の数
K = int(input())

# 選択リスト
choice_list = []
for j in range(K):
    c, d = [int(x) for x in input().split()]
    choice_list.append((c,d))

# 条件を満たす数
ans = 0

# あり得る組み合わせcを1つとってきて、その中にAとBが存在しているか
for c in itertools.product(*choice_list):
    p = sum(A in c and B in c for A, B in ab_list)

    if ans < p:
        ans = p

print(ans)
