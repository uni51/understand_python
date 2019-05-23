num = 1;

def test():
    global num
    num = 100
    print(num)

print(num)
test()
print(num)