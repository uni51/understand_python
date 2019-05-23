# 辞書型のデータで、キーとvalueを入れ替える内包表記
score = { 'math': 80, 'english': 20 }
new_score = {value:key for key,value in score.items()}
print(new_score)