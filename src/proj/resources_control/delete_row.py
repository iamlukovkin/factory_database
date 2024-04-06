from .input_key import input_key


def delete_row(database: dict) -> dict:
    key: str = input_key(database, False)
    if key:
        del database[key]
        print(f'Ресурс {key} удален')
    return database
