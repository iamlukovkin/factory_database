from .input_key import input_key


def add_new_rows(database: dict) -> dict:
    """
    Добавляет N записей в базу данных.
    :param database: База данных
    """
    n = int(input('Введите количество записей, которые хотите добавить: '))
    for _ in range(n):
        print(f'Ресурс #{len(database) + 1}: ')
        database = add_new_row(database)
    return database


def add_new_row(database: dict) -> dict:
    """
    Добавляет одну запись в базу данных.
    :param database: База данных
    """
    resource_code: str = input_key(database, True)
    if resource_code:
        resource_name: str = input('Введите наименование ресурса: ')
        resource_unit: str = input('Введите единицу измерения ресурса: ')
        resource_plan: int = int(input('Введите плановое количество ресурса: '))
        resource_fact: int = int(input('Введите фактическое количество ресурса: '))
        database[resource_code] = [resource_name, resource_unit, resource_plan, resource_fact]
        print(f'Ресурс {resource_code} добавлен')
    return database
