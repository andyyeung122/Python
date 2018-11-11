
my_str = str(input("Enter two words with a space:"))
my_str_two = my_str.split()
my_str_three = sorted(my_str_two[0])
my_str_four = sorted(my_str_two[1])
if my_str_three == my_str_four:
    print('True')
else:
    print('False')

Letter_LowerCase="abcdefghijklmnopqrstuvwxyz"
Letter_UpperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
uniq=[]
Letter=Letter_LowerCase+Letter_UpperCase
count = 0
LetterLenght=len(Letter)
my_dictionary={}

import random
while True:
    index = random.randint(0,51)
    if index not in uniq:
        uniq.append(index)
    else:
        continue

    my_dictionary[Letter[index]] = index
    count += 1

    if count == LetterLenght:
        break
print(my_dictionary)

