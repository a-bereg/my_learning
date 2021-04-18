from random import randint

_hidden_numeric = ''


def new_numeric(numeric_len=4):     # Генерируем число из несовпадающих цифр
    global _hidden_numeric
    while len(_hidden_numeric) < numeric_len:
        element=str(randint(0, 9))
        if _hidden_numeric.count(element) == 0:
            _hidden_numeric += element


#    print(_hidden_numeric) # для отладки


def check_numeric(users_numeric):
    compare_result = {'bulls': 0, 'cows': 0, 'error_code': 0}
    if (len(str(users_numeric)) != len(_hidden_numeric)     # проверяем что ввел пользователь
            or not (str(users_numeric).isnumeric())
            or len(set(users_numeric)) != len(_hidden_numeric)):
        compare_result['error_code'] = 1
    else:
        for i in range(len(_hidden_numeric)):
            if _hidden_numeric[i] == users_numeric[i]:
                compare_result['bulls'] += 1
            elif _hidden_numeric.count(users_numeric[i]) != 0:
                compare_result['cows'] += 1
    return compare_result
