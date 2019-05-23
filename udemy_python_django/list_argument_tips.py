def create_int_list(numbers=None):
    if numbers is None:
        numbers = []
    for i in range(10):
        numbers.append(i)
    return numbers

numbers = create_int_list()
print(numbers)

numbers2 = create_int_list()
print(numbers2)

numbers3 = create_int_list()
print(numbers3)