# デコレータ
def debug(function):
    def _debug(*args, **kwargs):
        # 本来の関数を呼び出し、結果を受け取る
        result = function(*args, **kwargs)
        # 本来の関数名と、引数、結果を出力
        print(function.__name__, args, kwargs, result)
        # 関数の実行結果を返す
        return result
    return _debug


@debug
def say_hello():
    print('hello')


say_hello()