import sqlite3


def create_tables(connection):
    connection.execute('''DROP TABLE IF EXISTS library''')
    connection.execute('''
    CREATE TABLE IF NOT EXISTS library (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    ''')
    connection.commit()
    print("Таблица 'library' успешно создана.")


def insert_books(connection):
    cursor = connection.cursor()

    books_data = [
        ('Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Роман', 384, 5),
        ('Преступление и наказание', 'Федор Достоевский', 1866, 'Роман', 672, 8),
        ('Война и мир', 'Лев Толстой', 1869, 'Эпопея', 1225, 3),
        ('1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 328, 6),
        ('Гарри Поттер и философский камень', 'Дж. К. Роулинг', 1997, 'Фэнтези', 320, 12),
        ('Маленький принц', 'Антуан де Сент-Экзюпери', 1943, 'Философская сказка', 96, 10),
        ('Так говорил Заратустра', 'Фридрих Ницше', 1883, 'Философия', 352, 6),
        ('Наедине с собой', 'Марк Аврелий', 180, 'Философия', 256, 7),
        ('Анна Каренина', 'Лев Толстой', 1877, 'Роман', 864, 7),
        ('Сто лет одиночества', 'Габриэль Гарсиа Маркес', 1967, 'Магический реализм', 416, 5),
        ('Моби Дик', 'Герман Мелвилл', 1851, 'Приключения', 635, 3),
        ('Гордость и предубеждение', 'Джейн Остин', 1813, 'Роман', 432, 9),
    ]

    insert_query = """
    INSERT INTO library (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?) 
    """

    cursor.executemany(insert_query, books_data)
    connection.commit()

    cursor.execute("SELECT COUNT(*) FROM library")
    count = cursor.fetchone()[0]

    print(f"Успешно добавлено {count} книг в таблицу 'library'.")


if __name__ == "__main__":
    connection = sqlite3.connect('library.db')

    try:
        create_tables(connection)
        insert_books(connection)
    finally:
        connection.close()

        print("Соединение с базой данных закрыто.")
