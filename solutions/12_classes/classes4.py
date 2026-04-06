# classes4
# Fix the program so it prints `Lion: 300`.

# hint: A long book has more pages, and the summary should start with the title.
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_long(self):
        return self.pages >= 300

    def summary(self):
        return self.title + ": " + str(self.pages)


book = Book("Lion", 300)
print(book.summary())
