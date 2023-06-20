import json

login = input('Введите свой логин: ')
password = int(input('Введите свой пароль: '))


def register(login, password):
    with open('users_data_2.json', 'r') as f:
        data = json.load(f)
    logins = list(data.keys())
    enter = True
    for i in logins:
        if login == i:
            enter = False
            print('Пользователь с таки именем уже существует')
            break
    if enter:
        data[login] = password
        with open('users_data_2.json', 'w') as f:
            json.dump(data, f)
        print('регистрация прошла успешно')

register(login, password)
