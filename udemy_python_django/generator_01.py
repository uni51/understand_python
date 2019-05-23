numbers = [1,5,6,11,3,5,7,3]
square_gen = (num**2 for num in numbers)
for num in square_gen:
    print(num)