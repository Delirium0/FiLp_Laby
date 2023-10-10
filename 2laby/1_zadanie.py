# задание
"""Найти наибольшее и наименьшее абсолютное значение вещественного
массива. Если таких значений несколько, определить их количество. Создать
функции для определения минимума и максимума. """
# from functools import reduce
#
#
# def find_minimum(arr):
#     return reduce(lambda x, y: x if x < y else y, arr)
#
#
# def find_maximum(arr):
#     return reduce(lambda x, y: x if x > y else y, arr)
#
#
# def count_occurrences(value, arr):
#     return len(list(filter(lambda x: x == value, arr)))
#
#
# # Пример использования:
# real_numbers = [1.5, -3.7, 2.8, -4.2, 5.1, -1.9, -4.2]
#
# min_value = find_minimum(real_numbers)
# max_value = find_maximum(real_numbers)
#
# min_occurrences = count_occurrences(min_value, real_numbers)
# max_occurrences = count_occurrences(max_value, real_numbers)
#
# print(f"Минимальное значение: {min_value}, встречается {min_occurrences} раз(а)")
# print(f"Максимальное значение: {max_value}, встречается {max_occurrences} раз(а)")


# _______________________________________________________________
# решение с рекурсией без лишних библиотек

def find_extremum(arr, compare, initial_value):
    if not arr:
        return initial_value
    return find_extremum(arr[1:], compare, compare(initial_value, arr[0]))


# мы передаем в функция find_extremum первый аргумент это массив чисел, второй фунция сравнения
# lambda x, y: x if x < y else y
# а третий это бесконечный минус или плюс, потом если у нас массив не пуст то мы идём дальше по итерации в рекурсия
# массив обрезается на одно число, так же передается функция сравнения и 3 это передается предположительно самое
# меленькое или большое число
real_numbers = [1.5, -3.7, 2.8, -4.2, 5.1, -1.9]

min_value = find_extremum(real_numbers, lambda x, y: x if x < y else y, float('inf'))
max_value = find_extremum(real_numbers, lambda x, y: x if x > y else y, float('-inf'))

min_occurrences = real_numbers.count(min_value)
max_occurrences = real_numbers.count(max_value)

print(f"Минимальное значение: {min_value}, встречается {min_occurrences} раз(а)")
print(f"Максимальное значение: {max_value}, встречается {max_occurrences} раз(а)")

# __________________________________________________________________
# решение с min max
# def find_minimum(arr):
#     return min(arr)
#
#
# def find_maximum(arr):
#     return max(arr)
#
#
# def count_occurrences(value, arr):
#     return len(list(filter(lambda x: x == value, arr)))
#
#
# # Пример использования:
# real_numbers = [1.5, -3.7, 2.8, -4.2, 5.1, -1.9]
#
# min_value = find_minimum(real_numbers)
# max_value = find_maximum(real_numbers)
#
# min_occurrences = count_occurrences(min_value, real_numbers)
# max_occurrences = count_occurrences(max_value, real_numbers)
#
# print(f"Минимальное значение: {min_value}, встречается {min_occurrences} раз(а)")
# print(f"Максимальное значение: {max_value}, встречается {max_occurrences} раз(а)")
