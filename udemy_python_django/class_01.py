# クラスの場合は、先頭の1文字を大文字にするのが慣例
class Student:
    def __init__(self,name):
        self.name = name

a = Student('narito')
print(a.name)