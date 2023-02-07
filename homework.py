# #Номер 1
print (int(1.6))
print (int (2.99))
# #Номер 2
string1 = 'www.my_site.com#about'
new_string = string1.replace ('#', "/")
print (new_string)

new_string = string1.replace ('#', "/")
print (new_string)
## НОМЕР 3
a = 'stroka'
b = 'ing'
print (a+b)
c = 'stroka'
print (c+'ing')
## НОМЕР 4
string = 'Ivanou Ivan'
new_string1 = string.split(' ')[::-1]
print (new_string1)
print (" ".join(new_string1))

##НОМЕР 5
# Напишите программу которая удаляет пробел в начале, в конце строки
a = ' Hello dear Michael! '
b = a.strip ()
print (b)
    
##НОМЕР 6
school = {"1а": 30, "1б": 28, "2а": 25, "2б": 21, "3а": 18, "3б": 19, "4а": 20, "4б": 23, "5а": 23, "5б": 18,}


##НОМЕР 7
#  Создайте список и извлеките из него списка второй элемент.
List = ['Max','Michael','Jake','Finn','Olov']
print (List[1])
##НОМЕР 8
sting = 'employ'
string2 = 'employment'
if sting in string2:
    print (True)
else:
    print (False)
##НОМЕР 9
x = "My name is Agent Smith"
y = len (x)
print (len(x))
print(x[1]) #y
print(x[3:18:3]) #nesgt
##НОМЕР 10
list10 = [1, 5, 2, 9, 2, 9, 1]
for number in list10:
    if list10.count(number)<2:
        print (number)