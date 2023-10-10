# задание
"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг
другу. Считается, что любые два элемента, равные друг другу, образуют одну
пару, которую необходимо посчитать"""


def count_equal_pairs(lst):
    if not lst:
        return 0

    def count_pairs_recursive(current, remaining, count):
        if not remaining:
            return count
        else:
            equal_pairs = list(filter(lambda x: x == current, remaining))
            new_count = count + len(equal_pairs)
            return count_pairs_recursive(remaining[0], remaining[1:], new_count)

    return count_pairs_recursive(lst[0], lst[1:], 0)


numbers = [1, 2, 3, 2, 4, 1, 5, 5, 10, 10]
result = count_equal_pairs(numbers)
print(f"Количество пар: {result}")
