try:
    print('try')
    int('abc')
except ValueError:
    print('except')
else:
    print('else')
finally:
    print('finally')
