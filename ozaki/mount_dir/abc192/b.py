s = input()

# True なら読みやすい
flag = False
for i in range(len(s)):
  if(i%2 == 1):
    if(s[i].istitle() == False):
      flag = True
      break
  else:
    if(s[i].istitle() == True):
      flag = True
      break

if flag:
  print("No")
else:
  print("Yes")
