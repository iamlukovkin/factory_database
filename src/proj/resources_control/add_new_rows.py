# src/proj/resources_control/add_new_rows.py
from .input_key import input_key
from .input_value import input_value


def add_new_rows(database: dict) -> dict:
    """
    Добавляет N записей в базу данных.
    :param database: База данных
    """
    n = input_value('Введите количество записей, которые хотите добавить: ')
    for _ in range(n):
        print(f'Ресурс #{len(database) + 1}: ')
        temp_database = add_new_row(database)
        if database is None:
            break
        database = temp_database
    return database


def add_new_row(database: dict) -> dict | None:
    """
    Добавляет одну запись в базу данных.
    :param database: База данных
    """
    resource_code: str = input_key(database, True)
    if resource_code is not None:
        resource_name: str = input('Введите наименование ресурса: ')
        resource_unit: str = input('Введите единицу измерения ресурса: ')
        resource_plan: int = input_value('Введите плановое количество ресурса: ')
        resource_fact: int = input_value('Введите фактическое количество ресурса: ')
        database[resource_code] = [resource_name, resource_unit, resource_plan, resource_fact]
        print(f'Ресурс {resource_code} добавлен')
    return database
