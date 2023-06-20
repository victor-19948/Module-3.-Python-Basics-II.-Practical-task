import json

login = input('Введите свой логин: ')
password = int(input('Введите свой пароль: '))


def verification(login, password):
    with open('users_data_3.json', 'r') as f:
        data = json.load(f)
    logins = list(data.keys())
    login_accept = False
    for i in logins:
        if login == i:
            login_accept = True
            break
    if login_accept:
        if data[login] == password:
            print('Вход в систему выполнен успешно')
        else:
            print('Логин подтвержден, но вы ввели неверный пароль')
    else:
        print('Пользователя с таким логином не существует')


verification(login, password)
