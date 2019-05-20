class Player:
    LEVEL_LIMIT = 10 # クラス属性

    @staticmethod # 静的メソッドの定義
    def print_limit():
        print(Player.LEVEL_LIMIT) # クラス属性のLEVEL_LIMITを表示


Player.print_limit() # 静的メソッドの呼び出し
