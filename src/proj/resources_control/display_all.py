# src/proj/resources_control/display_all.py
import prettytable as pt


def display_all(database: dict[str, list[str, str, int, int]]) -> None:
    """
    Выводит на экран содержимое базы данных.
    :param database:
    :return: None
    """
    table = pt.PrettyTable()
    table.field_names = ['Шифр', 'Наименование', 'Единица измерения', 'План', 'Факт', 'Отклонение']
    for key, value in database.items():
        table.add_row([key, value[0], value[1], value[2], value[3], int(value[3]) - int(value[2])])
    print(table)
    return None
