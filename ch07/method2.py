class Player:
    LEVEL_LIMIT = 10 # クラス属性

    @classmethod # クラスメソッドの定義
    def print_limit(cls):
        print(cls.LEVEL_LIMIT) # クラス属性のLEVEL_LIMITを表示


Player.print_limit() # クラスメソッドの呼び出し
