# デコレータ
def decorator(function):
    print('decorator')
    return function

@decorator
def say_hello():
    print('hello')


# say_hello = decorator(say_hello)
say_hello()