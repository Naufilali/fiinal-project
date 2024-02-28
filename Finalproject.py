def add_contact(address_book, name, phone_number):
    address_book[name] = phone_number
    print(f"Contact {name} added successfully.")

def search_contact(address_book, name):
    if name in address_book:
        print(f"Name: {name}, Phone Number: {address_book[name]}")
    else:
        print(f"Contact {name} not found.")

def delete_contact(address_book, name):
    if name in address_book:
        del address_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def print_address_book(address_book):
    print("Address Book:")
    for name, phone_number in address_book.items():
        print(f"Name: {name}, Phone Number: {phone_number}")

def main():
    address_book = {}
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Print Address Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            add_contact(address_book, name, phone_number)
        elif choice == "2":
            name = input("Enter name to search: ")
            search_contact(address_book, name)
        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_contact(address_book, name)
        elif choice == "4":
            print_address_book(address_book)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
