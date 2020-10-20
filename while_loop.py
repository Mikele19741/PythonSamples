from random import randint

number = 0
my_list = []

while number != 7:
    number = randint(1, 10)
    my_list.append(number)

print(my_list)