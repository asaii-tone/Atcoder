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

すべての要素がTrueか判定: all()
いずれかの要素がTrueか判定: any()

テキストの中身を同じように input してくれる
python a.py < test.txt

入力の個数が決まっているときは
N, A, B = map(int, input().split())
A, B, C, X = [int(input()) for i in range(4)]
でもいいのかも

map()はイテレータを作る
