class Book:
    page_material = "бумага"
    presence_of_text = True

    def __init__(self, book_title, author, amount_pages, isbn, reserved):
        self.book_title = book_title
        self.author = author
        self.amount_pages = amount_pages
        self.isbn = isbn
        self.reserved = reserved


first_book = Book(
    "Идиот",
    "Достоевский",
    500,
    1234567,
    True
)
second_book = Book(
    "Статский советник",
    "Акунин",
    300,
    2345678,
    False
)
third_book = Book(
    "Война и мир",
    "Толстой",
    1000,
    3456789,
    False
)
fourth_book = Book(
    "Маленький принц",
    "Экзюпери",
    400,
    45678910,
    False
)
fifth_book = Book(
    "Мастер и Маргарита",
    "Булгаков",
    700,
    567891011,
    False
)

my_books = [first_book, second_book, third_book, fourth_book]

for book in my_books:
    if book.reserved:
        print(
            f"Название: {book.book_title}, "
            f"Автор: {book.author}, "
            f"страниц: {book.amount_pages}, "
            f"материал: {book.page_material}, "
            f"зарезервирована")
    else:
        print(
            f"Название: {book.book_title}, "
            f"Автор: {book.author}, "
            f"страниц: {book.amount_pages}, "
            f"материал: {book.page_material}"
        )

print("-" * 100)


class SchoolBook(Book):
    presence_of_tasks = True

    def __init__(
            self,
            book_title,
            author,
            amount_pages,
            isbn,
            reserved,
            subject,
            school_class
    ):
        super().__init__(
            book_title,
            author,
            amount_pages,
            isbn,
            reserved
        )
        self.subject = subject
        self.school_class = school_class


algebra_book = SchoolBook(
    "Алгебра",
    "Иванов",
    200,
    6789101112,
    True,
    "Математика",
    9
)
history_book = SchoolBook(
    "История",
    "Петров",
    100,
    78910111213,
    False,
    "История",
    9
)
geography_book = SchoolBook(
    "География",
    "Сидоров",
    300,
    891011121314,
    False,
    "География",
    9
)

my_school_books = [algebra_book, history_book, geography_book]

for school_book in my_school_books:
    if school_book.reserved:
        print(
            f"Название: {school_book.book_title}, "
            f"Автор: {school_book.author}, "
            f"страниц: {school_book.amount_pages}, "
            f"предмет: {school_book.subject}, "
            f"класс: {school_book.school_class}, "
            f"зарезервирована"
        )
    else:
        print(
            f"Название: {school_book.book_title}, "
            f"Автор: {school_book.author}, "
            f"страниц: {school_book.amount_pages}, "
            f"предмет: {school_book.subject}, "
            f"класс: {school_book.school_class}"
        )
