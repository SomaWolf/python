'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(x, y, z):
    try:
        x = int(input('Число один: '))
        y = int(input('Число два: '))
        z = int(input('Число три: '))
        my_list = [x, y, z]
        out = sum(my_list) - min(my_list)
    except ValueError:
        return 'Что тебе в слове "число" было не понятно?'
    return out


print(my_func(1, 2, 3))