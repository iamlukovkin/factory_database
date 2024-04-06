# src/proj/resources_control/input_key.py
def input_key(database: dict, new_key_required: bool) -> str | None:
    """
    Запрашивает у пользователя ключ записи.
    :return: str: Ключ записи
    """
    try:
        print(f"Существующие ключи: {list(database.keys())}")
        key: str = input('Введите ключ записи: ')
        if new_key_required ^ (key in database.keys()):
            return key
        else:
            raise ValueError
    except ValueError:
        print('Неверный ключ')
        if input('Хотите попробовать ещё раз? (y/n) ') == 'y':
            return input_key(database, new_key_required)
        else:
            return None
