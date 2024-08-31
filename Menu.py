from classes import Admin

class Library:
   def __init__ (self):
        self.admin = Admin()

   def Library_Menu(self):
    while True:
        print("Select from the mentioned menu options:  \n"
              "1: Add book \n"
              "2: Add User \n"
              "3: Borrow book \n"
              "4: Return book\n"
              "5: Print Library books \n"
              "6: Print users borrowed books \n"
              "7: Print users \n"
              "8: Exit")

        option = input("Enter number from 1 to 8 as shown in the menu: ")

        if not option.isdigit() or not (1 <= int(option) <= 8):
            print("Invalid input. Please enter a number between 1 and 8.")
            continue
        
        option = int(option)

        if option == 1:
            book_id = input("Enter book id: ")
            book_name = input("Enter book name: ")
            book_qty = int(input("Enter Book Qty: "))
            self.admin.add_book(book_name, book_id, book_qty)

        elif option == 2:
            user_id = input("Enter user id: ")
            user_name = input("Enter user name: ")
            self.admin.add_user(user_name, user_id)

        elif option == 3:
            user_id = input("Enter user id: ")
            book_id = input("Enter book id: ")
            book_qty = int(input("Enter Book Qty: "))
            self.admin.Borrow_books(user_id, book_id, book_qty)

        elif option == 4:
            user_id = input("Enter user id: ")
            book_id = input("Enter book id: ")
            book_qty = int(input("Enter Book Qty: "))
            self.admin.Return_books(user_id, book_id, book_qty)

        elif option == 5:
            self.admin.print_lib_books()

        elif option == 6:
            self.admin.print_borrowed_books()

        elif option == 7:
            self.admin.print_users()

        elif option == 8:
            print("Exiting...")
            break







