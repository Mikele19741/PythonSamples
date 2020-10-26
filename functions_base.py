from random import randint

def dog_voice1():
    print('Woof!')

print(dog_voice1())

def cat_voice1():
    print('Meow!')

print(cat_voice1())

def cat_voice():
    return 'Meow!'

print(cat_voice())
print(cat_voice())

def dog_voice():
    return 'Woof!'

print(dog_voice())
print(dog_voice())

def get_voice(name):
    return name

print(get_voice('Bla Bla!'))

my_list=[]
for item in range(10):
    number = randint(1, 10)
    if(number%2==1):
        my_list.append(number)

print(my_list)
