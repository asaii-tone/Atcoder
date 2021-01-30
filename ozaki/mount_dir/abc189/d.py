n = int(input())
s = [int(input()) for i in range(n)]

# 2択なら 2進数で考えれる
# and ならパターン数保持として 加える大きい桁は0
# or ならパターン数増加で 加える大きい桁は1
