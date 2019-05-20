import functools

def comment(f): # デコレータ名（comment）
    @functools.wraps(f)
    def wrapper(*x, **y):
        print('<!--') # 前処理（<!--と表示する）
        f(*x, **y) # 関数の呼び出し
        print('-->') # 後処理（-->と表示する）
    return wrapper

@comment
def hello():
    print('hello')

hello()