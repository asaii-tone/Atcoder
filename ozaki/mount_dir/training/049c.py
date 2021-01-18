import re

S = input()
# いずれかを1回以上繰り返しているか
if re.match("^(dream|dreamer|erase|eraser)+$", S):
  print("YES")
else:
  print("NO")
