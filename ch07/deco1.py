import functools

def deco(f): # デコレータ名（deco）
    @functools.wraps(f)
    def wrapper(*x, **y):
        print('BEGIN!') # 前処理（BEGIN!と表示する）
        f(*x, **y) # 関数の呼び出し
        print('END!') # 後処理（END!と表示する）
    return wrapper

@deco
def hello():
    print('hello')

hello()