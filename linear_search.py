numlist = [9, 41, 32, 2, 121, 5, 73]

inputnum = int(input('数字を入れてください:'))

for i, num in enumerate(numlist):
  if num == inputnum:
    index = i
    print('添字:',index)
    exit()
  
print('not found')