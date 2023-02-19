#1
var_int = 10
var_float = 8.4
var_str = 'No'

#2
big_int = var_int*3.5

#3
var_float-=1

#4 
var_int/var_float
big_int/var_float

#5
var_str = 'No'*2 +'Yes'*3

#6
print (var_int)
print(var_float)
print (var_str)


#STROKI
#1
new_str = 'abcdefgh'
print(new_str[0])
print(new_str[-1])
print(new_str[2])
print(new_str[-3])
print(len(new_str))

#2
another_string = 'asdfghjklzxc'
print (another_string[0:8])
print (another_string[4:8])
print (another_string[0::3])
print (another_string[::-1])

#3
my_string = 'My name is name'
my_name = 'Michael'
my_string = my_string[0:-4] + my_name
print (my_string)

#4
test_tring = "Hello world!"
print(test_tring.find('w'))
print(test_tring.count('l'))
print(test_tring.startswith('Hello'))
print(test_tring.endswith('qwe'))

#SPISKI
#1
list_1 = [1.1,1.2,1.3,var_float]
list_2 = [1,2,3,var_int,4,5]

#2
print (list_1[1])

#3
list_2 [-1] = 6
print (list_2)

#4
list_3 = list_1+list_2
print (list_3)

#5
list_3[len(list_1)-1:len(list_3)-1]
print(list_3[len(list_1)-1:len(list_3)])
#6 
list_3 += [7, 8]
print (list_3)

#7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = list(set(a).intersection(b))
print (common)
#8
c = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print (list(set(c)))
#Логические операции
#1
x = 10
y = 20
#2
print (x<20 and y>10)
print (x>9 and y<21)
print (x<8 and y>21)
print (x>11 and y<18)
#3
print (x<9 or y>10)
print (x>9 or y<17)
print (x<9 or y>21)
print (x>11 or y<18)
#4
a = 'My name is Michael'
b = 'My name is Sergey'
print ('M' in a and 'S' in b)
print ('g' in a and 'e' in b)
print ('a' in a or'a' in b)
print ('t' in a or 'o' in b)

#SLOVARI
#1
school = {
          "1а": 23, 
          "1б": 22,  
          "2б": 20, 
          "6а": 20, 
          "7в": 25, 
          "8б": 26,
          "9б": 17, 
          "10а": 24, 
          "10б": 22,
          "11а": 24,
          }
print (school['11а'])
school ["1а"] = 20
school ["1б"] = 20
school ["2б"] = 19
school ['11в'] = 22
school ['11г'] = 22
del school ['7в']
print (school)


# ПРЕОБРАЗОВАНИЕ ТИПОВ
#1
string = "Robin Singh"
second_string = "I love arrays they are my favorite"
string = string.split(" ")
second_string = second_string.split (" ")
print (string)
print (second_string)

#2
new_list = ['Ivan', 'Ivanou']
city = ['Minsk']
country = ['Belarus']
print ('Привет ' + new_list[0] + ' ' + new_list[1] + '!' + 'Добро пожаловать в' + str(city) + str(country))

#3
list_4 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
list_to_string = " ".join(list_4)
print (list_to_string)

#4
list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
list_of_numbers[2] = 11
del list_of_numbers[6]
print (list_of_numbers)

#5
a = { 'a': 1, 'b': 2, 'c': 3} 
b = { 'c': 3, 'd': 4,'e': 5} 
ab = {}

for key, value in a.items():
    if key in b:
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [value, None]

for key, value in b.items():
    if key in a:
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [None, value]

print(ab)


#IF
#1 
number = int(input("Введите число: "))
if number > 0:
    number +=1
    print(number)

#2
numbers = [-500, 200, 4000]
count = 0
for number in numbers:
    if number > 0: count+=1
print("Количество положительных чисел: ", count)

# 3
n = int(input("Введите год: "))
if n % 4 != 0:
    print('365')
elif n % 100 != 0:
    print('366')
elif n % 400 != 0:
    print('365')
else:
    print('366')

#4
i =  str(input("Введите число из диапазона 1-7: "))
week_days = {
            '1': 'понедельник',
            '2': 'вторник',
            '3': 'среда',
            '4': 'четверг',
            '5': 'пятница',
            '6': 'суббота',
            '7': 'воскресенье'}
print(week_days[i])

# 5
print("1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер")
i = int(input("Ед. изм: "))
M = float(input("Масса: "))
if i == 1:
    print("Вводные данные: " + str(M) + " кг")
    m = M
elif i == 2:
    print("Вводные данные: " + str(M) + " мг")
    m = M / 1000000
elif i == 3:
    print("Вводные данные: " + str(M) + " г")
    m = M / 1000
elif i == 4:
    print("Вводные данные: " + str(M) + " т")
    m = M * 1000
elif i == 5:
    print("Вводные данные: " + str(M) + " ц")
    m = M * 100
print("В килограммах: ", m, " кг")


#For
#1
a = -10
b = 10
sum = 0 
for number in range(a, b+1):
    sum += number
print ("Сумма: ",sum)


# 2
if  a <= 0: 
    a=1
for number in range(a, b+1):
    print ("Число: ",number)
    sum += number
print ("Сумма: ",sum)

#3
numbers = [-10, -5, 3, 4, -20, 2, -8, 123, -150, 0]

multiply_number = 1
sum_of_negative = 0
count_of_negative = 0
for number in numbers:
    if number > 0:
        multiply_number *= number
    if number < 0:
        count_of_negative +=1
        sum_of_negative += number

print (multiply_number)
print (sum_of_negative)
print (count_of_negative)

#4
results = {
            'Бекиш Александр': 21.07, 
            'Будник Алексей': 20.34, 
            'Гребень Анастасия': 22.12, 
            'Давидович Татьяна': 30, 
            'Дешук Дмитрий': 24.01, 
            'Казак Анна': 28.17 
            }

best_result = max(results.values())
best_result = list(results.values())[0]


for result in results.values():
    if result < best_result:
        best_result = result
print (best_result)

#5
list_5 = [1, 5, 2, 9, 2, 9, 1]
for number in list_5:
        if list_5.count(number) == 1:
            print(number)


#While
# 1
number = 1
multiply_number = 1
N = 10
while number <= N:
    print("Следующее число ", number)
    multiply_number *= number
    number +=1
    print ("Произведение ", multiply_number)
print (multiply_number)

#2
S1= 1
S2 = 1
year = 0
while S1/S2 > 0.1:
    S1*=2
    S2*=3
    year+=1
    print (f"Площадь S1 = {S1}, Площадь S2 = {S2}, ГОД = {year}" )
print (year)
#3

number = 945612
sum_of_digits = 0
count = 0

number = 9456

while number:   # 0 == False
    last_digit = number%10
    print (last_digit)
    sum_of_digits += last_digit
    count+=1
    number = int( number/10)

print ("Count: ", count)
print("Sum: ", sum_of_digits)

# 4
M = 90
N = 5

x = M -2* N
print (f"Дед: {M+x}, Внук {N+x}, Кол-во лет: {x}"  )


#Вариант через циклы 
count_of_years = 0 
while M/N != 2:

    M += 1
    N += 1
    count_of_years +=1 

print (f"Дед: {M}, Внук {N}, Кол-во лет: {count_of_years}")
