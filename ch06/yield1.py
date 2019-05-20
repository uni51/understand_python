def do_yield():
    yield 1
    yield 2
    yield 'Fizz'
    yield 4
    yield 'Buzz'

for i in do_yield():
    print(i)