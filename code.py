
class Library:
    books = []
    @classmethod
    def __init__(cls,listofbooks):
        cls.books = listofbooks
    @classmethod
    def displaybooks(cls):
        print("The list of available books")
        for book in cls.books:
            print(" \t -" + book)

    def borrowbook(self, bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. Please keep it safe and return it within 30 days" )
            self.books.remove(bookname)
        else:
            print("Sorry, the book  is either not available or already been issued to someone else.Try again after 30 days")

    def returnbook(self, bookname):
        self.books.append(bookname)
        print("Thanks, for returning the book.")

    def donatebook(self):
        bookname = input("Enter the book you would like to donate: ")
        self.books.append(bookname)

class Student:
    def request(self):
         self.book = input("Enter the book you would like to borrow: ")
         return self.book

    def returnb(self):
         self.book = input("Enter the book you would like to return: ")
         return self.book
         


if __name__ == "__main__":

    Librarycenter = Library(["Algo", "Python", "CSS", "HTML"])
    Librarycenter.displaybooks()
    student = Student()
    while(True):
        welcome =  '''
        =====Welcome to the Library=======
        Please choose an option from the following options:
        1- List all the books
        2- Request a book
        3- Add/ Return a book
        4- Donate the book
        5- Exit the library 
        
        '''
        print(welcome)
        a = int(input("Enter a choice:"))
        if a == 1:
              Librarycenter.displaybooks()
        elif a == 2:
              Librarycenter.borrowbook(student.request())
        elif a == 3:
              Librarycenter.returnbook(student.returnb())
        elif a == 5:
              print("Thanks for using library")
              exit()
        elif a == 4:
              Librarycenter.donatebook()
              print("Thank you so much for donating the book.")
        else:
              print("Invalid choice")

