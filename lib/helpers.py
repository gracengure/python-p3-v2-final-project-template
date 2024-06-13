# lib/helpers.py
from models.phone import Phone
from models.order import Order
from models.user import User

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Thank you for using the Phone Inventory Management System (PIMS). Have a great day!")
       
    exit()
def display_phones():
    # Fetch all phones from the database
    phones = Phone.get_all()
    for phone in phones:
        print(phone)

    pass
def display_phone_by_brand():
    brand = input("Enter the phone's brand: ")
    phone =Phone.find_by_brand(brand)
    print(phone) if phone else print(
        f' Phone {brand} not found')
    pass

def display_phone_by_price():
     #use a trailing underscore not to override the built-in id function
    price = input("Enter the phone's price: ")
    phone = Phone.find_by_price(price)
    print(phone) if phone else print(f'Phone {price} not found')
    pass

def create_phone():
    brand = input("Enter the phone's brand: ")
    model = input("Enter the phone's model: ")
    
    # Validate price input
    try:
        price = float(input("Enter the phone's price: "))
        if price < 0:
            raise ValueError("Price must be a non-negative number")
    except ValueError as e:
        print(f"Invalid price input: {e}")
        return
    
    # Validate stock input
    try:
        stock = int(input("Enter the phone's stock: "))
        if stock < 0:
            raise ValueError("Stock must be a non-negative number")
    except ValueError as e:
        print(f"Invalid stock input: {e}")
        return

    try:
        phone = Phone.create(brand, model, price, stock)
        print(f'Success: Phone {phone.brand} {phone.model} added with price {phone.price} and stock {phone.stock}')
    except Exception as exc:
        print("Error creating phone:", exc)
def update_phone():
    id_ = int(input("Enter Phone's ID: "))
    if phone := Phone.find_by_id(id_):
        try:
            brand = input("Enter the Phone's Brand: ")
            phone.brand = brand
            model = input("Enter the Phone's Model: ")
            phone.model = model
            price = float(input("Enter the Phone's Price:"))
            if price < 0:
                raise ValueError("Price must be a non-negative number")
            phone.price = price
            stock = int(input("Enter the Phone's Stock: "))
            phone.stock = stock
            phone.update()

            print(f"Phone successfully updated: {phone}")
        except Exception as exc:
            print("Error Updating Phone", exc)
    else:
        print(f"Phone with Phone ID: {id_} not found")


def delete_phone(): 
    id_ = input("Enter the phone's id: ")
    if phone := Phone.find_by_id(id_):
        phone.delete()
        print(f'Phone in id{id_} deleted')
            
    else:
        print(f'Phone in id {id_} not found')
    pass


def display_orders():
    # Fetch all orders from the database
    order = Order.get_all()
    for order in order:
        print(order)

    pass
def display_order_by_quantity():
    quantity = input("Enter the order's quantity: ")
    order =Order.find_by_quantity(quantity)
    print(order) if order else print(
        f' Phone {order} not found')
    pass

def display_order_by_status():
     #use a trailing underscore not to override the built-in id function
    status = input("Enter the order's  status: ")
    order = Order.find_by_status(status)
    print(order) if order else print(f'Phone {order} not found')
    pass

def create_order():
    try:
        phone_id = int(input("Enter the phone's ID: "))
        if phone_id <= 0:
            raise ValueError("Phone ID must be a positive integer")
    except ValueError as e:
        print(f"Invalid phone ID input: {e}")
        return
    
    # Validate user_id input
    try:
        user_id = int(input("Enter the user's ID: "))
        if user_id <= 0:
            raise ValueError("User ID must be a positive integer")
    except ValueError as e:
        print(f"Invalid user ID input: {e}")
        return

    # Validate quantity input
    try:
        quantity = int(input("Enter the order's quantity: "))
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
    except ValueError as e:
        print(f"Invalid quantity input: {e}")
        return

    status = input("Enter the order's status: ")
    order_date = input("Enter the order's order_date (YYYY-MM-DD): ")

    try:
        # phone_id, quantity, order_date, status, user_id
        order = Order.create(phone_id,  quantity,  order_date, status, user_id)
        print(f'Success: Order {order}')
    except Exception as exc:
        print("Error creating order: ", exc)

def update_order():
    id_ = int(input("Enter Order's ID: "))
    if order := Order.find_by_id(id_):
        try:
            phone_id = int(input("Enter the Phone ID for the Order: "))
            order.phone_id = phone_id
            quantity = int(input("Enter the Quantity: "))
            order.quantity = quantity
            order_date = input("Enter the Order Date (YYYY-MM-DD): ")
            order.order_date = order_date
            status = input("Enter the Order Status: ")
            order.status = status
            user_id = int(input("Enter the User ID: "))
            order.user_id = user_id
            order.update()

            print(f"Order successfully updated: {order}")
        except Exception as exc:
            print("Error Updating Order", exc)
    else:
        print(f"Order with Order ID: {id_} not found")


def delete_order(): 
    id_ = input("Enter the order's id: ")
    if order := Order.find_by_id(id_):
        order.delete()
        print(f'Order in id{id_} deleted')
    else:
        print(f'Order in id {id_} not found')
    pass

def list_phone_orders():
    phone_id = int(input("Enter Phone ID: "))
    phone = Phone.find_by_id(phone_id)
    
    if phone:
        orders = phone.orders()
        if orders:
            print(f"Orders for phone {phone.brand} {phone.model}:")
            for order in orders:
                print(order)
        else:
            print(f"No orders found for phone {phone.brand} {phone.model}.")
    else:
        print(f"Phone with ID {phone_id} not found.")

def display_users():
    # Fetch all orders from the database
    user = User.get_all()
    for user in user:
        print(user)

    pass
def display_user_by_name():
    name = input("Enter the user's name: ")
    user =User.find_by_name(name)
    print(user) if user else print(
        f' Phone {user} not found')
    pass


def create_user():
    try:
        name = input("Enter the user's name: ")
        email = input("Enter the user's email: ")
        phone_number = input("Enter the user's phone number: ")
        
        if not name or not email or not phone_number:
            raise ValueError("All fields are required")

        user_id = User.create(name, email, phone_number)
        print(f'Success: User created with ID {user_id}')
        return user_id
    except Exception as exc:
        print("Error creating user: ", exc)
        return None
def update_user():
    user_id = int(input("Enter User's ID: "))
    if user := User.find_by_id(user_id):
        try:
            name = input("Enter the User's Name: ")
            user._name = name
            email = input("Enter the User's Email: ")
            user._email = email
            phone_number = input("Enter the User's Phone Number: ")
            user._phone_number = phone_number
            user.update()

            print(f"User successfully updated: {user}")
        except Exception as exc:
            print("Error Updating User", exc)
    else:
        print(f"User with User ID: {user_id} not found")
    

def delete_user(): 
    id_ = input("Enter the user's id: ")
    if user := User.find_by_id(id_):
        user.delete()
        print(f'User in id{id_} deleted')
            
    else:
        print(f'User in id {id_} not found')
    pass