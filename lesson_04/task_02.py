'''
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''

ori_list = [1, 12, 56, 23, 546, 765, 12, 2, 213, 1005, 996, 2604, 1986]
replace_list = [x for i, x in enumerate(ori_list) if x > ori_list[i - 1] and i != 0]  #  что-то много текста вышло, нет?
print(replace_list)