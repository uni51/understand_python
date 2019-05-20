class Player:
    LEVEL_LIMIT = 10

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display(self):
        print('Name:', self.name)
        print('Level:', self.level)

    def level_up(self, number):
        self.level += number
        self.__check_level()

    def __check_level(self):
        if self.level > Player.LEVEL_LIMIT:
            self.level = Player.LEVEL_LIMIT


class Fighter(Player): # Playerクラスを継承したFighter（戦士）クラスの作成

    def __init__(self, name, level, sword): # ← __init__メソッドの定義（オーバーライド）
        Player.__init__(self, name, level) # ← Playerクラスの__init__メソッドを呼び出す
        self.sword = sword # ← データ属性sword（剣）の設定

    def display(self): # ← displayメソッドの定義（オーバーライド）
        Player.display(self) # ← Playerクラスのdisplayメソッドを呼び出す
        print('Sword:', self.sword) # ← データ属性sword（剣）の表示

    def slash(self): # ← Fighterクラスに特有のslash（斬る）メソッド
        print('Slashing!')


class Wizard(Player): # Playerクラスを継承したWizard（魔法使い）クラスの作成

    def __init__(self, name, level, wand): # ← __init__メソッドの定義（オーバーライド）
        Player.__init__(self, name, level) # ← Playerクラスの__init__メソッドを呼び出す
        self.wand = wand # ← データ属性wand（杖）の設定

    def display(self): # ← displayメソッドの定義（オーバーライド）
        Player.display(self) # ← Playerクラスのdisplayメソッドを呼び出す
        print('Wand:', self.wand) # ← データ属性wand（杖）の表示

    def magic(self): # ← Wizardクラスに特有のmagic（魔法をかける）メソッド
        print('Casting a maagic!')


class MagicKnight(Fighter, Wizard): # Fighter（戦士）クラスとWizard（魔法使い）クラスを継承したWizardクラスの作成

    def __init__(self, name, level, sword, wand): # ← __init__メソッドの定義（オーバーライド）
        Player.__init__(self, name, level) # ← Playerクラスの__init__メソッドを呼び出す
        self.sword = sword # ← データ属性sword（剣）の設定
        self.wand = wand # ← データ属性wand（杖）の設定

    def display(self): # ← displayメソッドの定義（オーバーライド）
        Player.display(self) # ← Playerクラスのdisplayメソッドを呼び出す
        print('Sword:', self.sword) # ← データ属性sword（剣）の表示
        print('Wand:', self.wand) # ← データ属性wand（杖）の表示


mk = MagicKnight('Gobu', 3, 'silver', 'glass')
mk.display()
mk.slash() # Fighterクラスから継承したslash（斬る）メソッドの呼び出し
mk.magic() # Wizardクラスから継承したmagic（魔法をかける）メソッドの呼び出し
