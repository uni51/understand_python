class A:
    def __init__(self):
        # self._value = 1 # _（アンダースコア1つ）は慣例的なもので、プライベート属性を意味する
        self.__value = 1 # __（アンダースコア2つ）は名前空間の衝突を避け、プライベート属性を意味する

a = A()
# print(a._value)
print(a._A__value)