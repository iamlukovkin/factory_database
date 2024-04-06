import os


def clear_screen() -> None:
    """
    Очищает экран.
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    return None
