# 二次元配列を作成して、九九の一覧を表示する内包表記
table = [[x*y for x in range(1,10)] for y in range(1, 10)]
print(table)