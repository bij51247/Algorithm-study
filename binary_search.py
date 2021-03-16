# 前提：このような場合、小数値は切り捨てられ整数値のみになる
# print(int(5/2))
# 2

numlist = [13, 24, 56, 78, 102, 262, 409]
#先頭
head = 0
#最後尾
tail = len(numlist) - 1

#-1で初期化（見つからなかった場合は-1を表示)
pos = -1

x = int(input(''))

while pos == -1 and head <= tail:
  center  = int((head+tail)/2) #真ん中
  if x == numlist[center]:
    pos = center
  elif x > numlist[center]:
    head = center + 1
  else:
    tail = center - 1

print(pos)
  
  