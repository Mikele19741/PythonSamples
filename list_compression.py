greetings = ['hello', 'hi', 'hey', 'hola']

list_second= [ greet for greet in greetings]
list_final=[]
for greet in list_second:
   list_final.append(greet[1])
print(list_final)

list_final=[]
list_second= [  list_final.append(greet[1])  for greet in greetings]

print(list_final)


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_second_1=[digit for digit in digits if digit%2==0]
print(list_second_1)