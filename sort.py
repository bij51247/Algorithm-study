class InertionSort:
    # コンストラクタ
    def __init__(self, num):
        self.num = num
    # 関数
    def printArray(self):
        print('ソート後',self.num)


numlist = [10, 43, 3, 24, 5]

print('ソート前', numlist)

for i in range(1,len(numlist)):
    temp = numlist[i]
    cmp = i - 1
    while cmp >=0:
        if(numlist[cmp]>temp):
            numlist[cmp+1] =numlist[cmp]
        cmp-=1
    numlist[cmp+1] = temp

# インスタンス作成
insert = InertionSort(numlist)
# 呼び出し
insert.printArray()
