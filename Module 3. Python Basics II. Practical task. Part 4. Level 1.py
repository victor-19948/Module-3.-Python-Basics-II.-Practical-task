import json

login = input('Введите свой логин: ')
password = int(input('Введите свой пароль: '))


def register(login, password):
    data = {login: password}
    with open('users_data_1.json', 'w') as f:
        json.dump(data, f)


register(login, password)
