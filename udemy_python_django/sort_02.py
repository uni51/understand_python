def price_sort(tpl):
    return tpl[1]

my_list = [('納豆', 78),('ヨーグルト',90),('コーヒー',120),('コーラ',120),('サバ缶',100)]

my_list.sort(key=price_sort)

print(my_list) # [('納豆', 78), ('ヨーグルト', 90), ('サバ缶', 100), ('コーヒー', 120), ('コーラ', 120)]