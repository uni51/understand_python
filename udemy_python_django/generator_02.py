def make_squares(n):
    for i in range(1, n+1):
        yield i**2


squares = make_squares(10)
for i in squares:
    print(i)
