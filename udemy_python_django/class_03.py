class A:
    def __init__(self):
        self.number = 10 # インスタンスの属性にnumberを代入する

class B:
    number = 10 # クラス属性


b1 = B()
b2 = B()
B.number = 100
b1.number = 2
# 100,2,100と出力される（まず、インスタンス属性を確認し、なければクラス属性を確認する）
print(B.number, b1.number, b2.number)