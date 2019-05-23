# lambda 引数：返す値
numbers = [1,2,3,4,5]
for num in filter(lambda num:num%2==0, numbers):
    print(num)

"""
# 内包表記でも書くことができる
numbers = [1,2,3,4,5]
evens = [x for x in numbers if x%2==0]
"""