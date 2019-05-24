members = {}


def add_score(name, subject, point):
    """点数を追加する"""
    student = members.setdefault(name, {})
    student[subject] = point


def get_score(name, subject):
    """点数を取得する"""

    # 生徒の取得を試みて、いなければいないと返す
    student = members.get(name)
    if not student:
        return 'いません'

    # 教科の点数の取得を試みて、まだならまだ、と返す
    point = student.get(subject)
    if not point:
        return 'その教科はまだです'
    
    # 生徒を取得し、その教科を受けていれば点数を返す
    return point


add_score('narito','math',50)
narito_math = get_score('narito', 'math')
print(narito_math)