from . import actions
from .get_actions import get_actions
from .get_next_action import get_next_action
from .determine_action import determine_action
from .start_print import start_print


menu_actions: dict[str, str] = {
    '1': 'Просмотр всех записей в базе данных',
    '2': 'Добавление N записей',
    '3': 'Удаление записи по ключу',
    '4': 'Поиск необходимой информации',
    '5': 'Завершение работы с базой данных',
}
