# Создайте класс Author и класс Book. Класс Book должен использовать
# композицию для включения автора в качестве объекта.

class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

book = Book("War and Peace", Author("Leo", "Tolstoy"))

print(book.name)
print(book.author.name)
print(book.author.surname)
