# Library Management System

## Overview

This is a simple library management system implemented in Python. The system allows you to:
- Add books
- Add users
- Borrow books
- Return books
- Print the list of books in the library
- Print the list of borrowed books
- Print the list of users

## Components

1. **`Book` Class**:
   - Represents a book with attributes: `name`, `id`, and `quantity`.
   - Includes a `__str__` method to provide a string representation of the book.

2. **`User` Class**:
   - Represents a user with attributes: `name`, `id`, and `user_books`.
   - `user_books` is a dictionary where keys are book IDs and values are quantities borrowed.

3. **`Admin` Class**:
   - Manages books and users.
   - Includes methods to add books, add users, borrow books, return books, and print details.
