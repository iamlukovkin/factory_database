# src/proj/resources_control/search_row.py
from .input_key import input_key


def search_row(database: dict) -> None:
    """
    Поиск записи по ключу.
    :param database: База данных
    :return: None
    """
    key: str = input_key(database, False)
    if key:
        value = database[key]
        print(
            f'{key}: {value[0]}\n'
            f'План производства: {value[2]}\n'
            f'Факт производства: {value[3]}\n'
            f'Отклонение: {int(value[3]) - int(value[2])}'
        )
    return None
