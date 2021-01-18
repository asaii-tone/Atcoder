# 20191025
a,b=map(int, input().split())
c = a * b
if c%2 == 1:
  print("Odd")
else:
  print("Even")

# 20210118
x, y = map(int, input().split())
print("Even" if x*y%2 == 0 else "Odd")
