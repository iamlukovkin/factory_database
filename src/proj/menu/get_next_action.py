# src/proj/menu/get_next_action.py
def get_next_action(menu_actions: dict) -> int:
    """
    Запрашивает действие пользователя и возвращает его.

    :return: int: Номер действия
    """
    try:
        action: int = int(input('Выберите действие: ')) - 1
        if str(action + 1) in (menu_actions.keys()):
            print(f'Вы выбрали действие: {menu_actions[str(action + 1)]}')
            return action
        else:
            raise ValueError
    except ValueError:
        print('Такого действия нет')
        return get_next_action(menu_actions)
