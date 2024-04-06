# src/proj/menu/determine_action.py
from . import actions
from src.proj import resources_control


def determine_action(database: dict, action: int) -> tuple[dict, bool]:
    """
    Выполняет действие пользователя.
    :param database: База данных
    :param action: Номер действия
    :return: База данных и флаг завершения действия
    """
    if action == -1:
        return database, False
    else:
        if action == 0:
            resources_control.display_all(database)
        elif action == 1:
            database = resources_control.add_new_rows(database)
        elif action == 2:
            database = resources_control.delete_row(database)
        elif action == 3:
            resources_control.search_row(database)
        elif action == 4:
            resources_control.display_ordered_items(database)
        actions.wait_for_enter()
        actions.clear_screen()
    return database, True
