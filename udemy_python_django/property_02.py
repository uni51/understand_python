class Person:

    def __init__(self, name):
        self.origin_name = name
        self.name = name # セッター呼び出し。real_nameに格納されます。

    @property
    def name(self):
        return self.real_name

    @name.setter
    def name(self, value):     
        if not value:
            value = '名無しの権兵衛'
        self.real_name = value


person = Person('田中')
print(person.name) # 田中が出力される

person.name = ''
print(person.name) # 名無しの権兵衛が出力される