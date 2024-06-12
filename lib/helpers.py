# lib/helpers.py
from models.phone import Phone
from models.order import Order

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
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
    model= input("Enter the phone's model: ")
    price=input("Enter the phone's price: ")
    stock=input("Enter the phone's status: ")
    try:
        phone =Phone.create(brand,model,price,stock)
        print(f'Success: {phone}')
    except Exception as exc:
        print("Error creating phone: ", exc)

    pass
def update_phone():
    id_ = input("Enter the phone's id: ")
    if phone := Phone.find_by_id(id_):
        try:
            brand = input("Enter the phone's new brand: ")
            phone.brand = brand
            model = input("Enter the phone's new model: ")
            phone.model =model
            price=input("Enter the phone's  new price: ")
            phone.price=price
            stock=input("Enter the phone's  new status: ")
            phone.stock=stock

            phone.update()
            print(f'Success: {phone}')
        except Exception :
            print("Error updating phone: ")
    else:
        print(f'Phone {id_} not found')
    pass
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
    phone_id = input("Enter the order's phone_id: ")
    quantity= input("Enter the order's quantity ")
    status=input("Enter the order's status ")
    order_date=input("Enter the order's order_date: ")
    try:
        order =Order.create(phone_id,quantity,status,order_date)
        print(f'Success: {order}')
    except Exception as exc:
        print("Error creating order: ", exc)

    pass
def update_order():
    id_ = input("Enter the order's id: ")
    if order := Order.find_by_id(id_):
        try:
            phone_id = input("Enter the order's phone_id: ")
            order.phone_id=phone_id
            quantity= input("Enter the order's quantity ")
            order.quantity=quantity
            status=input("Enter the order's status ")
            order.status=status
            order_date=input("Enter the order's order_date: ")
            order.order_date =order_date

            order.update()
            print(f'Success: {order}')
        except Exception :
            print("Error updating order: ")
    else:
        print(f'Order {id_} not found')
    pass
def delete_order(): 
    id_ = input("Enter the order's id: ")
    if order := Order.find_by_id(id_):
        order.delete()
        print(f'Order in id{id_} deleted')
    else:
        print(f'Order in id {id_} not found')
    pass


