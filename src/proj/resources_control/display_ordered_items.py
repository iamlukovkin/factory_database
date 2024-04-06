# src/proj/resources_control/display_ordered_items.py
from .display_all import display_all


def display_ordered_items(database: dict) -> None:
    """
    Отображает список ресурсов в порядке убывания.
    :param database: База данных
    :return: None
    """
    for key, value in database.items():
        database[key].append(int(value[3]) - int(value[2]))
    new_database = dict(sorted(
        database.items(),
        key=lambda x: x[1][4], reverse=False)
    )
    display_all(new_database)
