# src/proj/resources_control/input_value.py
def input_value(message: str) -> int:
    try:
        return int(input(message))
    except ValueError:
        print('Неверное значение')
        return input_value(message)
