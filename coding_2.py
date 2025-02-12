import sqlite3
import random
conn = sqlite3.connect('words.db')

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Создание таблицы, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT NOT NULL,
    word TEXT NOT NULL
);
''')
def coding():
    word = input("Введите слово для кодировки:")
    ke=[]
    ku = []
    kf =''
    key_v = "1234567890qwertyuiopasdfghjklzxcvbnm"
    for i in key_v:
        ku.append(i)
    for k in range(len(word)):
        ke.append(random.choice(ku))
    kf = ''.join(ke)
    cursor.execute('INSERT INTO words (key, word) VALUES (?, ?)', (kf, word))
    conn.commit()
    print(f'ключ для разкодировки:{kf}')

def uncoding():
    kr = input('Введите ключ: ')

    # Извлечение слова по ключу
    cursor.execute("SELECT word FROM words WHERE key = ?", (kr,))
    result = cursor.fetchone()

    if result:
        print(f'Слово: {result[0]}')
    else:
        print('Ключ не найден.')


coding_uncoding = input('Что сделать?:')
if coding_uncoding == 'кодировка':
    coding()
elif coding_uncoding == 'разкодировка':
    uncoding()