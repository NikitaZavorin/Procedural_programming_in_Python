users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
len_users = len(users)
set_users = len(set(users))
dist ={
    'Общее количество' : 0,
    'Уникальные посещения' : 0
}
dist['Общее количество'] = len_users
dist['Уникальные посещения'] = set_users
print(dist)