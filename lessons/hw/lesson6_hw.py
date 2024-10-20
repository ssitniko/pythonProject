
class Book:
    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = "read" if self.read else "unread"
        return f'{self.title} by {self.author}, {self.year} — {status}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [str(book) for book in self.books]

    def find_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def mark_book_as_read(self, title):
        book = self.find_by_title(title)
        if book:
            book.mark_as_read()
            return f'{book.title} marked as read.'
        return f'Book with title {title} not found.'

    def remove_book(self, title):
        book = self.find_by_title(title)
        if book:
            self.books.remove(book)
            return f'{book.title} has been removed.'
        return f'Book with title {title} not found.'

    def filter_by_read_status(self, read=True):
        return [book for book in self.books if book.read == read]

    def sort_books_by_year(self):
        return sorted(self.books, key=lambda book: book.year)



library = Library()

while True:
    main_input = input(
        'Введите одну из команд: добавить, найти, пометить как прочитанную, удалить, вывести все книги, фильтр по статусу: ').lower()

    if main_input == 'quit':
        break

    elif main_input == 'добавить':
        add_input = input('Введите через запятую название, автора и год издания книги: ')
        title, author, year = add_input.split(',')
        book = Book(title.strip(), author.strip(), int(year.strip()))
        library.add_book(book)
        print(f'Книга "{title.strip()}" добавлена в библиотеку.')

    elif main_input == 'найти':
        search_input = input('Найти по названию или автору? ').lower()

        if search_input == 'названию':
            name_input = input('Введите название книги: ')
            book = library.find_by_title(name_input)
            if book:
                print(book)
            else:
                print(f'Книга с названием "{name_input}" не найдена.')

        elif search_input == 'автору':
            author_input = input('Введите автора: ')
            books_by_author = library.find_by_author(author_input)
            if books_by_author:
                for book in books_by_author:
                    print(book)
            else:
                print(f'Книги автора "{author_input}" не найдены.')

    elif main_input == 'пометить как прочитанную':
        read_input = input('Введите название книги: ')
        result = library.mark_book_as_read(read_input)
        print(result)

    elif main_input == 'удалить':
        delete_input = input('Введите название книги для удаления: ')
        result = library.remove_book(delete_input)
        print(result)

    elif main_input == 'вывести все книги':
        for book in library.list_books():
            print(book)

    elif main_input == 'фильтр по статусу':
        status_input = input('Фильтр: прочитанные или непрочитанные? ').lower()
        if status_input == 'прочитанные':
            books = library.filter_by_read_status(True)
        else:
            books = library.filter_by_read_status(False)

        for book in books:
            print(book)








