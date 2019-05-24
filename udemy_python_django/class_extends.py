# 親クラス（スーパークラス）
class Character:
    def __init__(self, name):
        self.name = name

    def show_profile(self):
        profile = '名前:{0} 種族:Character'.format(self.name)
        print(profile)


# 子クラス（サブクラス）
class Monster(Character): 
    def __init__(self, name, hp=20):
        super().__init__(name)
        self.hp = hp

    def show_profile(self):
        profile = '名前:{0} 種族:Monster HP:{1}'.format(self.name, self.hp)
        print(profile)


monster_a = Monster('モンスターA')
monster_a.show_profile()