# lambda 引数：返す値
numbers = [1,2,3,4,5]
for num in map(lambda num:num**2, numbers):
    print(num)

"""
# 内包表記でも書くことができる
numbers = [1,2,3,4,5]
squares = [x**2 for x in numbers]
"""
