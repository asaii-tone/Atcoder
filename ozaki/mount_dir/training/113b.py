# N = int(input())
# T, A = map(int, input().split())
# H = list(map(int, input().split()))
# dT = [abs((T - Hi*0.006) - A) for Hi in H]
# print(dT.index(min(dT)) +1)

N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
# とりあえず大きそうな数字を選ぶのはいいのか?
T_max = 10**5
out = 1
for i in range(N):
  dT = abs((T - H[i]*0.006) - A)
  if dT < T_max:
    T_max = dT
    out = i+1
print(out)
