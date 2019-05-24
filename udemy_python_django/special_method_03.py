class A:
    def __init__(self):
        self.name = '属性'

    def __str__(self):
        return self.name

a = A()
print(a)