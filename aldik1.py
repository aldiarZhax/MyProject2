book_inf=list()
def add_book():
    title=input("Title of the book: ")
    author=input("Author: ")
    year=int(input("Year: "))
    copies_available=int(input("Enter the number of copies available: "))
    for book in book_inf:
        if book["Title"].lower()==title.lower():
            book["Copies_Available"]+=1

    book_inf.append({"Title":title,"Author":author,"Year":str(year),"Copies_Available":str(copies_available)})

def search_book():
    title=input("Name of the Book: ")
    for book in book_inf:
        if book["Title"].lower()==title.lower():
            print("Book was found :)")
            print(f"{book["Title"], book["Author"], book["Year"],book["Copies_Available"]}")
            return
    print("“The book was not found")


def borrow_book():
    title=input("Name of the book: ")
    for book in book_inf:
        if book["Copies_Available"]>0:
            if book["Title"].lower()==title.lower():
                book["Copies_Available"]-=1
            return
    print("Error!")


def return_book():
    title=input("Name of the book: ")
    for book in book_inf:
            if book["Title"].lower()==title.lower():
                book["Copies_Available"]+=1
            return
    print("Error!")


def view_book():
    print("Title    Author    Year     Copies")
    print("----------------------------------")
    for book in book_inf:
        print(f"{book["Title"],book["Author"],book["Year"],book["Copies_Available"]}")

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. View All Books")
        print("6. Exit")
        number=int(input("Choose number's between [1,6]: "))
        if number==1:
            add_book()
        elif number==2:
            search_book()
        elif number==3:
            borrow_book()
        elif number==4:
            return_book()
        elif number==5:
            view_book()
        elif number==6:
            break
        else:
            print("You entered wrong number!")

if __name__ == "__main__":
    main_menu()
