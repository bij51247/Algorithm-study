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
    print('temp',temp)
    cmp = i - 1
    print('cmp',cmp)
    while cmp >=0:
        if(numlist[cmp]>temp):
            numlist[cmp+1] =numlist[cmp]
        print('cmp-1にした結果')
        cmp-=1
        print(cmp)
    numlist[cmp+1] = temp

# インスタンス作成
insert = InertionSort(numlist)
# 呼び出し
insert.printArray()
