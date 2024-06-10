from __init__ import CURSOR, CONN
class Order:
    def _init_(self, id , phone_id ,quantity, order_date, status):
       self.id=id
       self.phone_id=phone_id
       self.quantity=quantity
       self.order_date=order_date
       self.status=status
          
       pass 