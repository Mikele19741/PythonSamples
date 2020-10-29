def is_cat_here(*args):
    for arg in args:
       x=str(arg)
       if x.lower()=='cat':
         return True
    return False
       
       

print('Cat Task')
print(is_cat_here('ddd', 'fdfasdfas', 'cat'))

print(is_cat_here('ddd', 'fdfasdfas', 'asdfasdf'))

print(is_cat_here('ddd', 'CAT', 'asdfasdf'))


def is_item_here(item ,*args):
    for arg in args:
       if item==arg:
         return True
    return False
       
       
print('Item Task')

print(is_item_here('ddd', 'fdfasdfas', 'cat', 'ddd'))

print(is_item_here(9, 'fdfasdfas', 'asdfasdf',5 ))



def your_favorite_color(my_color, **kwargs):
           if 'color' in kwargs:
                 print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
              
           else:
                 print('My favorite color is {}, what is your favorite color?'.format(my_color)) 

       
       
print('Color Task')

your_favorite_color('black', first='yellow',  second='red', color='green')

your_favorite_color('black', first='yellow',  second='red', thrid='green')



