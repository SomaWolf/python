'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

def dumb_func():
    out = False
    res = 0
    while out == False:
        number = input('Введите числа для рассчета или "н" для того, чтобы завершить операцию: ').split()
        y = 0
        for x in number:
            if 'н' in x:
                out = True
                print('На, хавай!')
                break
            y += int(x)
        res += y
    return res


print(dumb_func())