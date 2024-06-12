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
)


def main():
    while True:
        menu()
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
            display_orders()
        elif choice == "8":
            display_order_by_quantity()
        elif choice == "9":
            display_order_by_status()
        elif choice == "10":
            create_order()
        elif choice == "11":
            update_order()
        elif choice == "12":
            delete_order() 
        elif choice =="13":
             exit_program()
        else:
            print("Invalid choice .Please try again.")


def menu():
    
    print("Welcome to Phone Inventory Management System(PIMS)")
    print("Please select an option:")
    print("1. Display all phones")
    print("2. Display phone by brand")
    print("3. Display phone by price")
    print("4. Create phone")
    print("5. Update phone")
    print("6. Delete phone")
    print("7. Display all orders")
    print("8. Display order by quantity")
    print("9. Display order by status")
    print("10.Create order")
    print("11.Update order")
    print("12.Delete order") 
    print("13.Exit the system")

    

    

if __name__ == "__main__":
    main()
