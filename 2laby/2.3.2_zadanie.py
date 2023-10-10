# задание
"""Багаж пассажира характеризуется количеством вещей и общим весом
вещей. Пусть дан словарь, содержащий информацию о багаже нескольких пассажиров.
 Выясните, имеется ли пассажир, багаж которого состоит из одной вещи весом не менее 30 кг;
  удалите сведения о багаже, общий вес вещей в котором меньше, чем 10 кг"""


def filter_passengers(passengers):
    # Функция проверки, имеется ли пассажир с багажом весом не менее 30 кг
    def has_heavy_baggage(passenger):
        return any(item['weight'] >= 30 for item in passenger['baggage'])

    # Функция проверки, общий вес вещей в багаже больше или равен 10 кг
    def total_weight_greater_than_10(passenger):
        total_weight = sum(item['weight'] for item in passenger['baggage'])
        return total_weight >= 10

    # Фильтрация пассажиров
    filtered_passengers = filter(
        lambda passenger: has_heavy_baggage(passenger) or total_weight_greater_than_10(passenger), passengers)

    # Удаление из словарей информации о багаже, общий вес в котором меньше 10 кг
    updated_passengers = map(lambda passenger: {**passenger, 'baggage': list(
        filter(lambda item: item['weight'] >= 10, passenger['baggage']))}, filtered_passengers)

    return list(updated_passengers)


# Пример использования:
passengers_data = [
    {'name': 'Alice', 'baggage': [{'item': 'Laptop', 'weight': 5}, {'item': 'Clothes', 'weight': 8}]},
    {'name': 'Bob', 'baggage': [{'item': 'Book', 'weight': 2}, {'item': 'Camera', 'weight': 12}]},
    {'name': 'Charlie', 'baggage': [{'item': 'Guitar', 'weight': 15}]},
]

updated_passengers_data = filter_passengers(passengers_data)

print(updated_passengers_data)
