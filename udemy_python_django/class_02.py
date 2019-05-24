members = {}

# クラスの場合は、先頭の1文字を大文字にするのが慣例
class Student:
    def __init__(self,name):
        self.name = name
        self.score = {} # 成績を管理するための辞書
    
    def add_score(self, subject_name, point):
        self.score[subject_name] = point

    def get_score(self, subject_name):
        return self.score.get(subject_name, 'その教科はまだです')


members['narito'] = Student('narito')
members['saitou'] = Student('saitou')
members['yoshida'] = Student('yoshida')
print(members)

members['narito'].add_score('math', 50)