class InertionSort:
    #コンストラクタ
    def __init__(self, num):
        self.num = num
    #関数
    def printArray(self):
        print(self.num)

numlist = [10, 43, 3, 24, 5]

print('ソート前',numlist)


#インスタンス作成
insert = InertionSort(numlist)
#呼び出し
insert.printArray()
