n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = []
for i in range(n):
  target = a[i]
  if target == x:
    continue
  ans.append(target)

print(*ans)
# print(ans)


#   if not target in ans_s:
#     ans.append(target)
#     ans_s.add(target)

# ans = sorted(set(a), key=a.index)
