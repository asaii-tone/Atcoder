## 入力
```python
x = int(input())

# string なことに注意
x = input()

# 123 -> 1 2 3 ただし string
x, y, z = input()

# abcde -> ['a', 'b', 'c', 'd', 'e']
s = list(input())

# 1 2 -> 1\n 2
x, y = map(int, input().split())

# hello world! -> hello\n world!
x, y = input().split()

# 1 2 3 -> [1, 2, 3]
x = list(map(int, input().split()))
x = [int(i) for i in input().split()]

# Hello world ! -> ['Hello', 'world', '!']
x = list(input().split())
x = [i for i in input().split()]

# 1\n 2 -> 1 2
x, y = [int(input()) for i in range(2)]

# 1\n 2\n 3\n -> [1, 2, 3]
x = [int(input()) for i in range(3)]

# 入力数 3 が与えられて その後に値
# 3\n 2\n 1\n 3\n -> [2, 1, 3]
rows = int(input())
x = [int(input()) for i in range(rows)]

# 2次元配列
# 3 (入力行)
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
x = [list(map(int, input().split())) for i in range(rows)]
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
```

print("Even" if x*y%2 == 0 else "Odd")

すべての要素がTrueか判定: all()
いずれかの要素がTrueか判定: any()

テキストの中身を同じように input してくれる
python a.py < test.txt

入力の個数が決まっているときは
```python
N, A, B = map(int, input().split())
A, B, C, X = [int(input()) for i in range(4)]
```
でもいいのかも

map()はイテレータを作る

配列Aを大きい順に並び替える
`A.sort(reverse=True)`

問題文と同じ名前の変数にした方が良さそう

for文がネストしてあって 1つの候補が見つかったら強制終了って方法に
exit()を使う手法がある

正規表現を覚えないといけないのか
python で 正規表現を扱うのは re ライブラリ
re ライブラリで先頭を表す`^`と末尾を表す`$`と1回以上の繰り返しを表す`+`

一気に値を受け取らないで1行ずつ受け取るの賢いな
```python
N = int(input())
for i in range(N):
t, x, y = map(int, input().split())
```
1つ前の記録点の状態と今の状態でつながらないならエラーにするって賢い

リストでソートして文字列にして比較するの賢い
文字列にしたら大小はフツーに単語ごとのソートに等しくなる

問題文をちゃんと読んだら、めっちゃ簡単に解けることもある

計算対象を全部計算してリストにしたのち、一番小さい番目を取得するの賢い

`[スタート:ゴール:ステップ]`でスライスする
`[::-1]`だとすべての要素を逆順にする

string から探す系はfind, index, rfind, rindex
r がついてると後ろから探して その探したい文字列の最初の番号を返す
index は find と同じだが 見つからなかったら -1 じゃなくてエラーを返す

`n//4`は切り捨て除算
`int(n/4)`と同じことっぽい

平方根は`math.sqrt(n)`
二乗は`math.pow(x, y)`
階乗`math.factorial(n)`

組み合わせ(combination)の nCr
def comb(n, r):
    return int(math.factorial(n) / math.factorial(r) * math.factorial(n-r))
float 型が整数かTrueFalseで判定
f = 3.14
boolean = f.is_integer()
または float%1 == 0 でも判定できる

あまりリストのインデックス番号で値を取ってくると計算速度が出ない?

```python
# リストに含まれているか
if(要素 in リスト)
# リストに含まれていないか
if(要素 not in リスト)
if(not(要素 in リスト))
# あるリストからある要素をすべて取り除く
set(リスト)-{要素}
```

コメントを書くとコード長は長くなるが
実行時間やメモリは変わらない

無限ループ
`while True:`

N進数の桁を求める問題はその桁の最大値より小さいかで判断すればいいんやん
33 なら 33 < 10**2 で2桁って

割り算すると割り切れない問題が発生するっぽい
float の扱い注意
パーセントで 割る100するぐらいなら 対象の数字をかける100する

リストの要素を1個ずつ取り出して渡す操作をアンパックという
```python
l = [0, 1, 2]
print(l)
# [0, 1, 2]
print(l[0], l[1], l[2])
# 0 1 2
print(*l)
# 0 1 2
```

itertools.product() は引数のリスト分の全通りを返す

from decimal import Decimal
math.ceil()
math.floor()

二分探索
```python
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) //2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None
```
