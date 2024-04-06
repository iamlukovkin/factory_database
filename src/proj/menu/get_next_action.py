def get_next_action(menu_actions: dict) -> int:
    """
    Запрашивает действие пользователя и возвращает его.

    :return: int: Номер действия
    """
    try:
        action: int = int(input('Выберите действие: ')) - 1
        if action in range(len(menu_actions.keys())):
            return action
        else:
            raise ValueError
    except ValueError:
        print('Такого действия нет')
        return get_next_action(menu_actions)
