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


class Fighter(Player): # Playerクラスを継承したFighterクラスの作成

    def __init__(self, name, level, sword): # ← __init__メソッドの定義（オーバーライド）
        Player.__init__(self, name, level) # ← Playerクラスの__init__メソッドを呼び出す
        self.sword = sword # ← データ属性sword（剣）の設定

    def display(self): # ← displayメソッドの定義（オーバーライド）
        Player.display(self) # ← Playerクラスのdisplayメソッドを呼び出す
        print('Sword:', self.sword) # ← データ属性sword（剣）の表示

    def slash(self): # ← Fighterクラスに特有のslash（斬る）メソッド
        print('Slashing!')


class Wizard(Player): # Playerクラスを継承したWizardクラスの作成

    def __init__(self, name, level, wand): # ← __init__メソッドの定義（オーバーライド）
        Player.__init__(self, name, level) # ← Playerクラスの__init__メソッドを呼び出す
        self.wand = wand # ← データ属性wand（杖）の設定

    def display(self): # ← displayメソッドの定義（オーバーライド）
        Player.display(self) # ← Playerクラスのdisplayメソッドを呼び出す
        print('Wand:', self.wand) # ← データ属性wand（杖）の表示

    def magic(self): # ← Wizardクラスに特有のmagic（魔法をかける）メソッド
        print('Casting a maagic!')

f = Fighter('Daikon', 1, 'iron')
f.display()
f.slash()

w = Wizard('Ninjin', 2, 'wood')
w.display()
w.magic()
