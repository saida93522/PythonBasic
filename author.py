class Author:
    # books = []

    def __init__(self, name):
        self.name = name
        self.books = []  # empty book list

    def publish(self, title):  # append the title of the book to the list
        if title in self.books:
            print('oops, looks like this book is currently on the list')
            return
        else:
            return self.books.append(title)

    def __str__(self):  # returns a string with the author's name, and their book's titles
        book_list = ', '.join(self.books) or 'No published books'
        return f'Author name: {self.name}\nBooks Published: {book_list}'


def main():
    book1 = Author('Theodore Taylor')
    book1.publish('The Cay')
    book1.publish('The Cay')
    print(book1)

    book2 = Author('Lois Lowry')
    book2.publish('The Giver')
    book2.publish('The Giver')

    print(book2)


# **Note**
# '__main__' = scope in which top-level code executes
# A  __name__,
if __name__ == '__main__':
    main()  # only run if script is executing when invoked directly
else:
    # __name__ = imported module
    print('script is getting imported by other module')
