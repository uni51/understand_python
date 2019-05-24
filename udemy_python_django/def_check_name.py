def check_name(name):
    if len(name)>=6:
        return True
    else:
        return False


name = input()
result = check_name(name)
if result:
    print('登録完了')
else:
    print('名前が短いです')