k = int(input())
s = input()
t = input()

ten_1 = 10
ten_2 = 100
ten_3 = 1000
ten_4 = 10000
ten_5 = 100000

def count2point(no, count_no):
  point= 0
  if count_no == 0:
    point = no * 1
  elif count_no == 1:
    point = no * ten_1
  elif count_no == 2:
    point = no * ten_2
  elif count_no == 3:
    point = no * ten_3
  elif count_no == 4:
    point = no * ten_4
  elif count_no == 5:
    point = no * ten_5
  return point

def count_no(SorT):
  count_list = []
  count_1 = SorT.count("1")
  count_list.append(count_1)
  count_2 = SorT.count("2")
  count_list.append(count_2)
  count_3 = SorT.count("3")
  count_list.append(count_3)
  count_4 = SorT.count("4")
  count_list.append(count_4)
  count_5 = SorT.count("5")
  count_list.append(count_5)
  count_6 = SorT.count("6")
  count_list.append(count_6)
  count_7 = SorT.count("7")
  count_list.append(count_7)
  count_8 = SorT.count("8")
  count_list.append(count_8)
  count_9 = SorT.count("9")
  count_list.append(count_9)
  return count_list

def count2total(count_list):
  point_1 = count2point(1, count_list[0])
  point_2 = count2point(2, count_list[1])
  point_3 = count2point(3, count_list[2])
  point_4 = count2point(4, count_list[3])
  point_5 = count2point(5, count_list[4])
  point_6 = count2point(6, count_list[5])
  point_7 = count2point(7, count_list[6])
  point_8 = count2point(8, count_list[7])
  point_9 = count2point(9, count_list[8])
  total = point_1+point_2+point_3+point_4+point_5+point_6+point_7+point_8+point_9
  return total

def point_total(SorT):
  count_list = count_no(SorT)
  total = count2total(count_list)
  return total

def use_card_list(k, original_s, original_t):
  use_card_list = []
  original_st = original_s+original_t
  count_list = count_no(original_st)
  for i in range(9):
    use_card_list.append(k - count_list[i])
  return use_card_list

count_pattern_win = 0
count_pattern_total = 0

use_card_list = use_card_list(k, s, t)
for i in range(len(use_card_list)):
  if use_card_list[i] == 0:
    continue
  use_card_list_temp = use_card_list[:] # リストの参照渡しじゃないコピー
  temp_s = s + str(i+1) # listの0番目をカード番号にするための+1
  use_card_list_temp[i] -= 1
  point_temp_s = point_total(temp_s)
  # print(temp_s)
  for j in range(len(use_card_list_temp)):
      if use_card_list_temp[j] == 0:
        continue
      count_pattern_total += 1
      temp_t = t + str(j+1)
      # print(temp_t)
      if point_temp_s > point_total(temp_t):
        count_pattern_win += 1

# print(count_pattern_total)
# print(count_pattern_win)
print(count_pattern_win / count_pattern_total)


# 確率を出すときに 使ったカードを考えないといけない
# 高橋くんの裏のカードによっては青木くんの裏のカードの選択肢が変わる

# def count2point(s):
#   s = list(s)
#   s = list(map(int, s[:4]))
#   return s

# print(count_1)
# print(count_2)
# print(count_3)
# print(count_4)
# print(count_5)
# print(count_6)
# print(count_7)
# print(count_8)
# print(count_9)

# count_1 = s.count("1")
# count_2 = s.count("2")
# count_3 = s.count("3")
# count_4 = s.count("4")
# count_5 = s.count("5")
# count_6 = s.count("6")
# count_7 = s.count("7")
# count_8 = s.count("8")
# count_9 = s.count("9")

# print(point_total(s))

# print(use_card_list(k, s, t))
