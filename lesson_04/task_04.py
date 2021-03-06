'''
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''

f_list = [1, 1, 2, 12, 12, 34, 34, 65, 24, 6, 18, 86, 7, 8, 9, 20, 21, 54, 54, 78, 79]
s_list = [x for x in f_list if f_list.count(x) == 1]
print(s_list)