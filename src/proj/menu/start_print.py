import prettytable as pt
from .actions import wait_for_enter


# src/proj/menu/start_print.py
def start_print():
    table = pt.PrettyTable()
    table.add_column(fieldname='',
                     column=[
                         'МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ',
                         'ФЕДЕРАЛЬНОЕ ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ ОБРАЗОВАТЕЛЬНОЕ',
                         'ВЫСШЕГО ОБРАЗОВАНИЯ УЧРЕЖДЕНИЕ',
                         'РЯЗАНСКИЙ ГОСУДАРСТВЕННЫЙ РАДИОТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ',
                         'имени В.Ф. УТКИНА\n',
                         'ФАКУЛЬТЕТ ВЫЧИСЛИТЕЛЬНОЙ ТЕХНИКИ\n',
                         'КАФЕДРА ВЫЧИСЛИТЕЛЬНОЙ И ПРИКЛАДНОЙ МАТЕМАТИКИ\n',
                         'программа к курсовой работе по лисциплине',
                         'АЛГОРИТМИЧЕСКИЕ ЯЗЫКИ И ПРОГРАММИРОВАНИЕ',
                         'на тему',
                         'РАБОТА СО СЛОВАРЯМИ\n',
                         'автор программы: студент группы 345',
                         'Потапова А.А.',
                         'проверил: доцент кафедры ВПМ',
                         'Дмитриева Татьяна Александровна',
                         'Рязань, 2024\n'
                     ])
    table.set_style(pt.PLAIN_COLUMNS)
    print(table)
    wait_for_enter()
    return None
