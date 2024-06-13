# lib/cli.py
from helpers import (
    exit_program,
    display_phones,
    display_phone_by_brand,
    display_phone_by_price,
    create_phone,
    update_phone,
    delete_phone,
    display_orders,
    display_order_by_quantity,
    display_order_by_status,
    create_order,
    update_order,
    delete_order,
    list_phone_orders,
    list_user_orders,
    display_users,
    display_user_by_name,
    create_user,
    update_user,
    delete_user,
)

def main():
    current_menu = "main"
    while True:
        if current_menu == "main":
            main_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                current_menu = "phone"
            elif choice == "2":
                current_menu = "order"
            elif choice == "3":
                current_menu = "user"
            elif choice == "4":
                exit_program()
            else:
                print("Invalid choice. Please try again.")
        
        elif current_menu == "phone":
            current_menu = phone_menu()
        
        elif current_menu == "order":
            current_menu = order_menu()
        
        elif current_menu == "user":
            current_menu = user_menu()

def main_menu():
    print("Welcome to Phone Inventory Management System (PIMS)")
    print("Please select a category:")
    print("1. Phone Management")
    print("2. Order Management")
    print("3. User Management")
    print("4. Exit the system")

def phone_menu():
    while True:
        print("\nPhone Management Menu:")
        print("1. Display all phones")
        print("2. Display phone by brand")
        print("3. Display phone by price")
        print("4. Create phone")
        print("5. Update phone")
        print("6. Delete phone")
        print("7. Return to main menu")
        print("8. Go to Order Management")
        print("9. Go to User Management")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_phones()
        elif choice == "2":
            display_phone_by_brand()
        elif choice == "3":
            display_phone_by_price()
        elif choice == "4":
            create_phone()
        elif choice == "5":
            update_phone()    
        elif choice == "6":
            delete_phone()
        elif choice == "7":
            return "main"
        elif choice == "8":
            return "order"
        elif choice == "9":
            return "user"
        else:
            print("Invalid choice. Please try again.")

def order_menu():
    while True:
        print("\nOrder Management Menu:")
        print("1. Display all orders")
        print("2. Display order by quantity")
        print("3. Display order by status")
        print("4. Create order")
        print("5. Update order")
        print("6. Delete order")
        print("7. List  all orders of a phone")
        print("8. List  all orders of a user")
        print("9. Return to main menu")
        print("10.Go to Phone Management")
        print("11.Go to User Management")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_orders()
        elif choice == "2":
            display_order_by_quantity()
        elif choice == "3":
            display_order_by_status()
        elif choice == "4":
            create_order()
            
        elif choice == "5":
            update_order()   

        elif choice == "6":
            delete_order()
        elif choice == "7":
            list_phone_orders() 
        elif choice == "8":
            list_user_orders()       
        elif choice == "9":
            return "main"
        elif choice == "10":
            return "phone"
        elif choice == "11":
            return "user"
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    while True:
        print("\nUser Management Menu:")
        print("1. Display all users")
        print("2. Display user by name")
        print("3. Create user")
        print("4. Update user")
        print("5. Delete user")
        print("6. Return to main menu")
        print("7. Go to Phone Management")
        print("8. Go to Order Management")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_users()
        elif choice == "2":
            display_user_by_name()
        elif choice == "3":
            create_user()
        elif choice == "4":
            update_user()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            return "main"
        elif choice == "7":
            return "phone"
        elif choice == "8":
            return "order"
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()