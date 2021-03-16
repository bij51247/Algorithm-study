# セルの定義
class Cell:
    def __init__(self, x, y=None):
        # value:ノードのデータを格納
        # 次のノードのポインタを格納
        self.data = x
        self.next = y

    # 先頭のセルの要素を取り出す
    def first(self): return self.data
    # 先頭のセルを取り除いた残りの連結リスト
    def rest(self): return self.next

    # それぞれ,インスタンスの変数の値を書き換える
    def set_first(self, x): self.data = x
    def set_reset(self, x): self.next = x


class LinkedList:
    def __init__(self):
        self.top = None

    # insert(n,x)n番目の位置にデータxを挿入する
    def insert(self, n, x):
        # リストの先頭にデータを追加するかチェック
        # 先頭の場合（引数nが0か、topがNone( 空リスト)の場合)
        if n == 0 or not self.top:
            # 2番目の引数にself.topを渡し,生成したセルの後ろにtopの連結リストがリンクされる
            self.top = Cell(x, self.top)
        # 先頭じゃない場合
        else:
            cp = self.top
            # cp.rest()でセルを辿っていく
            while cp.rest():
                n -= 1
                if n == 0:
                    break
                # whileループを脱出してnextを書き換える
                cp = cp.rest()
            # whileループを終了するとcpは最後尾のセルになっているので,その後ろにデータxを追加
            # 第2引数にcp.rest()を指定することでnew_cpの後ろにcpの後ろにある連結リストをリンクすることができる
            new_cp = Cell(x, cp.rest())
            # cp.set_rest()でcpの変数nextをnew_cpに書き換える
            cp.set_reset(new_cp)

    def delete(self, n):
        if n == 0:
          # 先頭にあるデータを削除する場合はself.topに連結リストがあるかを確認
            if self.top:
              # topの値をtop.rest()に書き換えてTrueを返す
                self.top = self.top.rest()
                return True
        # リストの途中にあるデータを削除する場合
        else:
            cp = self.top
            # セルを辿って一つ前のセルを求める
            while cp.rest():
                n -= 1
                if n == 0:
                    # cp.set_rest()でセルcpのnextをcp.rest().rest()に書き換えてTrueを返す
                    # cp.rest().rest()は次の次の意
                    cp.set_reset(cp.rest().rest())
                    return True
                cp = cp.rest
        # whileループが終了するとcpは最後尾のセルになり削除するセルはないのでFalseを返す
        return False

    def index(self, x):
        n = 0
        cp = self.top
        while cp:
            # データxと等しい要素がないか調べる
            # cp.firstでセルのdataを取り出し,xと等しい場合は位置nを返す
            if cp.first() == x:return n
            n += 1
            cp = cp.rest()
        # whileループが終了する場合はxと等しい要素が見つからないので-1を返す
        return -1

    def show(self):
        cp = self.top
        while cp:
          print(cp.data)
          cp = cp.next
          

linklist = LinkedList()
linklist.insert(3, '木村')
linklist.insert(4, '佐伯')
linklist.insert(2, 'チンパンジー')
linklist.show()
index =  linklist.index('佐伯')
print(index)
linklist.delete(0)
linklist.show()