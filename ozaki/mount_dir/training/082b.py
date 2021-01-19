ls = list(input())
lt = list(input())
# どんな並び順でもいいから すぐ判定できる順にする
ls.sort(reverse=False)
lt.sort(reverse=True)
ss = "".join(ls)
st = "".join(lt)
print("Yes" if ss<st else "No")
