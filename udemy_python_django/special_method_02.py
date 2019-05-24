class A:
    def __init__(self):
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.count
        if current > 10:
            raise StopIteration
        self.count += 1
        return current       

a = A()
for count in a:
    print(count)