# Номер 1
def ex1():
    print(int(1.6))
    print(int(2.99))


# Номер 2
def ex2():
    string = 'www.my_site.com#about'
    new_string = string.replace('#', "/")
    print(new_string)


# НОМЕР 3
def ex3():
    a = 'stroka'
    b = 'ing'
    print(a+b)
    c = 'stroka'
    print(c+'ing')


# НОМЕР 4
def ex4():
    string = 'Ivanou Ivan'
    new_string = string.split(' ')[::-1]
    print(new_string)
    print(" ".join(new_string))


# НОМЕР 5
# Напишите программу которая удаляет пробел в начале, в конце строки
def ex5 ():
    a = ' Hello dear Michael! '
    b = a.strip()
    print(b)


# НОМЕР 6
def ex6():
    school = {
        "1а": 30,"1б": 28, "2а": 25, "2б": 21, "3а": 18,
        "3б": 19, "4а": 20, "4б": 23, "5а": 23, "5б": 18, 
        }


# НОМЕР 7
def ex7():
    list = ['Max', 'Michael', 
            'Jake', 'Finn', 'Olov'
            ]
    print(list[1])


# НОМЕР 8
def ex8():
    if 'employ' in 'employment':
        print(True)
    else:
        print(False)


# НОМЕР 9
def ex9():
    name_string = "My name is Agent Smith"
    print(len(name_string))
    print(name_string[1])
    print(name_string[3:18:3])

# НОМЕР 10
def ex10():
    list = [1, 5, 2, 9, 2, 9, 1]
    for number in list:
        if list.count(number) < 2:
            print(number)


def main():
    print('Задание 1')
    ex1()
    print(f"{'_':_^20}")
    print('Задание 2')
    ex2()
    print(f"{'_':_^20}")
    print('Задание 3')
    ex3()
    print(f"{'_':_^20}")
    print('Задание 4')
    ex4()
    print(f"{'_':_^20}")
    print('Задание 5')
    ex5()
    print(f"{'_':_^20}")
    print('Задание 6')
    ex6()
    print(f"{'_':_^20}")
    print('Задание 7')
    ex7()
    print(f"{'_':_^20}")
    print('Задание 8')
    ex8()
    print(f"{'_':_^20}")
    print('Задание 9')
    ex9()
    print(f"{'_':_^20}")
    print('Задание 10')
    ex10()
    print(f"{'_':_^20}")

if __name__ == '__main__':
    main()