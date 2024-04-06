# src/main.py
from src.proj.menu import *
from src.data import data


def main(database: dict) -> None:
    is_continue: bool = True

    start_print()

    while is_continue:
        print(get_actions(menu_actions))
        action: int = get_next_action(menu_actions)
        database, is_continue = determine_action(database, action)
    return actions.exit_app()


if __name__ == '__main__':
    main(data)
