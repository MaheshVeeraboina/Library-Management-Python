from src.library import Library

library = Library()

while True:
    print("===== Library Menu =====")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Remove Book")
    print("4. Add Borrower")
    print("5. Update Borrower")
    print("6. Remove Borrower")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Search Book")
    print("10. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.update_book()
    elif choice == "3":
        library.remove_book()
    elif choice == "4":
        library.add_borrower()
    elif choice == "5":
        library.update_borrower()
    elif choice == "6":
        library.remove_borrower()
    elif choice == "7":
        library.borrow_book()
    elif choice == "8":
        library.return_book()
    elif choice == "9":
        library.search_books()
    elif choice == "10":
        print("Thank you! Goodbye 😊")
        break
    else:
        print("❌ Invalid Choice, Try Again.\n")
