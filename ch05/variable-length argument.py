def sum(*number):
    s = 0
    for n in number: # 引数number（タプル）から要素を取り出して、nに代入
        s += n # sにn を加算
    # return s
    print(s)

sum(10,20,30)

