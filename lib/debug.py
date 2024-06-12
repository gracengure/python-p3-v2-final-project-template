from models.__init__ import CONN, CURSOR
from models.order import Order
from models.phone import Phone
from models.user import User
from datetime import datetime

import ipdb


def reset_database():
    
    Phone.drop_table()
    Phone.create_table()

    # Create seed data
    Phone.create("Apple", "iPhone 13", 45999.99, 50)
    Phone.create("Samsung", "Galaxy S21", 12999.99, 30)
    Phone.create("Tenco", "Pixel 5", 26999.99, 20)
    Phone.create("Realme", "C55", 23999.99, 10)
    Phone.create("Vivo", "Y03", 18999.99, 15)
    Phone.create("Huawei", "P40 Pro", 25999.99, 25)
    Phone.create("Vivo", "Y02t", 12999.99, 35)
    Phone.create("Infinix", "V60 ThinQ", 30999.99, 20)
    Phone.create("Redmi", "A3", 13999.99, 10)
    Phone.create("Nokia", "8.3 5G", 11999.99, 30)
    Phone.create("Tenco", "Spark20", 45999.99, 15)
    Phone.create("Redmi", "12c", 26999.99, 5)
    Phone.create("Samsung", "Galaxy S27", 25999.99, 15)
    Phone.create("Apple", "iPhone 15", 30999.99, 10)
    Phone.create("Oppo", "Find X3 Pro", 35999.99, 25)
    Phone.create("Apple", "iPhone 11", 35999.99, 50)
    Phone.create("Samsung", "Galaxy S24", 18999.99, 10)
    Phone.create("Realme", "C51", 13999.99, 10)
    Phone.create("Vivo", "Y27s", 26999.99, 15)
    Phone.create("Huawei","P40 Pro", 23999.99, 25)
    Phone.create("Vivo", "V29", 30999.99, 35)
    Phone.create("Samsung", "Galaxy S23", 13999.99, 15)
    Phone.create("Infinix", "V60 ThinQ", 45999.99, 20)
    Phone.create("Redmi", "13c", 18999.99, 10)
    Phone.create("Nokia", "8.3 5G",13999.99, 30)
    Phone.create("Tenco", "U20 5G", 23999.99, 15)
    Phone.create("Realme", "C30", 12999.99, 5)
    Phone.create("Apple", "iPhone 12", 26999.99, 10)
    Phone.create("Oppo", "Find X3 Pro", 23999.99, 25)
    
    Order.drop_table()
    Order.create_table()

    # Create seed data
    Order.create(1, 10, datetime.now(), 'pending', 1)
    Order.create(2, 20, datetime.now(), 'shipped', 2)
    Order.create(3, 10, datetime.now(), 'delivered', 3)
    Order.create(4, 30, datetime.now(), 'canceled', 4)
    Order.create(5, 20, datetime.now(), 'pending', 5)
     
    
    User.drop_table() 
    User.create_table()
    
    User.create("John Doe", "john@gmail.com",  789675434)
    User.create("Jane Smith", "jane@gmail.com", 9876543210)
    User.create("Ivy Kerubo", "sokoro@gmail.com", 7654321098)
    User.create("Gideon Bett", "giddy@gmail.com", 5432109876)
    User.create("Angela Mukami", "angie@gmail.com", 3210987654)
    User.create("Eliza Kangeo", "lizzy@gmail.com", 1098765432)
    User.create("Vincent Kimeli", "vinnie@gmail.com", 8765432109)
    User.create("Kelvin Biwott", "kevo@gmail.com", 6543210987)
    User.create("Ashley Kyalo", "bazu@gmail.com", 4321098765)
    User.create("Charity Wanjiku", "chae@gmail.com",  3672781890)
    User.create("Grace Ngure", "gracie@gmail.com", 3467258934)
    User.create("Daniel Mbachu", "danteh@gmail.com", 4536728921)
    User.create("Kelvin Mbachu", "mwana@gmail.com", 5467438291)
    User.create("Annah Kirui", "bobo@gmail.com", 4567329810)
    User.create("Patrick Kinyanjui", "pato@gmail.com", 1537428193)
    User.create("Princess Mumbi", "cutie@gmail.com", 6547839201)
    User.create("Eric  Kimani", "erico@gmail.com", 7834650231)
    User.create("Samuel  Mwangi", "sam@gmail.com", 1436728193)    

    

reset_database()
ipdb.set_trace()