# src/proj/menu/get_actions.py
def get_actions(menu_actions: dict) -> str:
    """
    Получает выводимый пользователю список действий.

    :return: str: Список действий
    """
    result: str = ''
    for key, value in menu_actions.items():
        result += f'{key} - {value}\n'
    return result
