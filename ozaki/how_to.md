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
N, A, B = map(int, input().split())
A, B, C, X = [int(input()) for i in range(4)]
でもいいのかも

map()はイテレータを作る

配列Aを大きい順に並び替える
A.sort(reverse=True)

問題文と同じ名前の変数にした方が良さそう

for文がネストしてあって 1つの候補が見つかったら強制終了って方法に
exit()を使う手法がある

正規表現を覚えないといけないのか
python で 正規表現を扱うのは re ライブラリ
re ライブラリで先頭を表す`^`と末尾を表す`$`と1回以上の繰り返しを表す`+`

一気に値を受け取らないで1行ずつ受け取るの賢いな
N = int(input())
for i in range(N):
    t, x, y = map(int, input().split())
1つ前の記録点の状態と今の状態でつながらないならエラーにするって賢い

リストでソートして文字列にして比較するの賢い
文字列にしたら大小はフツーに単語ごとのソートに等しくなる

問題文をちゃんと読んだら、めっちゃ簡単に解けることもある

計算対象を全部計算してリストにしたのち、一番小さい番目を取得するの賢い
