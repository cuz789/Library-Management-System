class Book:
        def __init__ (self, name, id, quantity):
                self.name = name
                self.id = id
                self.quantity = int(quantity)
        def __str__(self):
                return (f"name : {self.name}, id : {self.id}, quantity: {self.quantity} ")

class User:
        def __init__ (self, name, id):
                self.name = name
                self.id = id
                self.user_books ={}
        
        def __str__(self):
                return f"Name: {self.name}, ID: {self.id}, Books : {self.user_books}"

class Admin:
        def __init__(self):
                self.books = []
                self.users = {}
                                
        
        def add_book(self, name, id, quantity):
               new_book = Book(name, id, quantity)
               for book in self.books:
                       if book.id == id:
                               print("Book already exists")
                               return
                               
               self.books.append(new_book)
               print("Book addition successful")

        def add_user(self, name, id):
                new_user = User(name, id)
                if id in self.users:
                    print("User already exists")
                    return
                self.users[id]= new_user
                print("User addition successful")
        
        def Borrow_books(self, u_id, b_id, b_quantity):
                if u_id not in self.users:
                        print(f"User not found please register")
                        return
                
                for book in self.books:
                        if book.id == b_id:
                                if book.quantity == 0:
                                        print("Book is out of stock")
                                        return
                                elif book.quantity >= b_quantity :
                                        print("Book available for borrowing")
                                        book.quantity -= b_quantity

                                        user = self.users[u_id]
                                        if b_id in user.user_books:
                                                user.user_books[b_id] += b_quantity
                                        else:
                                                user.user_books[b_id] = b_quantity

                                        print(f"{b_quantity} copies of '{book.name}' borrowed successfully remaining quantity is '{book.quantity}' ")
                                        return
                                else:
                                        print(f"The available quantity is '{book.quantity}'")
                                        return
                
                
                
        def Return_books(self, u_id, b_id, b_quantity):
                       user = self.users[u_id]
                       if u_id not in self.users:
                              print("user not found")
                       else:
                        for book in self.books:
                            if book.id == b_id:
                                   book.quantity += b_quantity
                                   print(f"{b_quantity} copies of '{book.name}' added successfully")
                                   user.user_books[b_id] -= b_quantity
                                   if user.user_books[b_id] == 0:
                                           del user.user_books[b_id]  
                                   return    

                        print("Book not found")

        def print_lib_books(self):
                       self.books.sort(key= lambda book : book.id)
                       for book in self.books:
                               print(book)
                
        def print_borrowed_books(self):
                for user_id, user in self.users.items():
                        print(f"User ID: {user_id}, {user.user_books}")

        def print_users(self):
                for user_id, user in self.users.items():
                        print(f"User ID: {user_id}, User Name: {user.name}")