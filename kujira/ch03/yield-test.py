def gen1to3():
    yield 1;
    yield 2;
    yield 3;

itObj = gen1to3()

for i in itObj:
    print(i)