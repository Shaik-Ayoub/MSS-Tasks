class Book:
    def __init__(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre

    def info_update(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Genre : {self.genre}")

first_book = Book("the great","ayoub","fiction")

first_book.display_info()