# задание
"""Составить программу, реализующую телефонный справочник. 
В справочнике содержится следующая информация о каждом абоненте: имя и телефон. 
Реализовать вывод всей информации из справочника, поиск телефона по
имени, поиск имени по телефону"""


def create_phonebook():
    # Инициализация пустого справочника
    return []


def add_contact(phonebook, name, phone):
    # Добавление контакта в справочник
    return phonebook + [{'name': name, 'phone': phone}]


def display_phonebook(phonebook):
    # Вывод всей информации из справочника
    for contact in phonebook:
        print(f"Имя: {contact['name']}, Телефон: {contact['phone']}")


def find_phone_by_name(phonebook, name):
    # Поиск телефона по имени
    matching_contacts = list(filter(lambda contact: contact['name'] == name, phonebook))
    return [contact['phone'] for contact in matching_contacts]


def find_name_by_phone(phonebook, phone):
    # Поиск имени по телефону
    matching_contacts = list(filter(lambda contact: contact['phone'] == phone, phonebook))
    return [contact['name'] for contact in matching_contacts]


# Пример использования:
phonebook = create_phonebook()
phonebook = add_contact(phonebook, 'Alice', '123-456-789')
phonebook = add_contact(phonebook, 'Bob', '987-654-321')
phonebook = add_contact(phonebook, 'Charlie', '555-123-456')

print("Весь справочник:")
display_phonebook(phonebook)

name_to_find = 'Bob'
print(f"\nПоиск телефона для {name_to_find}:")
result_phone = find_phone_by_name(phonebook, name_to_find)
print(result_phone)

phone_to_find = '555-123-456'
print(f"\nПоиск имени для телефона {phone_to_find}:")
result_name = find_name_by_phone(phonebook, phone_to_find)
print(result_name)
