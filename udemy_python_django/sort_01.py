def my_sort(string):
    return string[-1]

my_list = ['python', 'django', 'tkinter', 'requests', 'kivy']

my_list.sort(key=my_sort) # 末尾の1文字でソートする
print(my_list)