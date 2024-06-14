from models.__init__ import CURSOR, CONN
from models.phone import Phone
from models.user import User

class Order:
    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, phone_id, quantity, order_date, status, user_id, id=None):
        self.id = id
        self.phone_id = phone_id
        self.quantity = quantity
        self.order_date = order_date
        self.status = status
        self.user_id = user_id

    def __repr__(self):
        return (
            f"<Order {self.id}: Phone ID {self.phone_id}, Quantity {self.quantity}, " +
            f"Order Date: {self.order_date}, Status: {self.status}, User ID: {self.user_id}>"
        )

    @property
    def phone_id(self):
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        if isinstance(phone_id, int) and Phone.find_by_id(phone_id):
            self._phone_id = phone_id
        else:
            raise ValueError("phone_id must reference a phone in the database")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int) and quantity > 0:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be a positive integer")

    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        self._order_date = order_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str) and status in {"pending", "shipped", "delivered", "canceled"}:
            self._status = status
        else:
            raise ValueError("Status must be 'pending', 'shipped', 'delivered', or 'canceled'")

    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int) and User.find_by_id(user_id):
            self._user_id = user_id
        else:
            raise ValueError("user_id must reference a user in the database")

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Order instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                phone_id INTEGER,
                quantity INTEGER,
                order_date TIMESTAMP,
                status TEXT,
                user_id INTEGER,
                FOREIGN KEY (phone_id) REFERENCES phones(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Order instances"""
        sql = """
            DROP TABLE IF EXISTS orders;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the order details into the orders table"""
        sql = """
            INSERT INTO orders (phone_id, quantity, order_date, status, user_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.phone_id, self.quantity, self.order_date, self.status, self.user_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Order instance"""
        sql = """
            UPDATE orders
            SET phone_id = ?, quantity = ?, order_date = ?, status = ?, user_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.phone_id, self.quantity, self.order_date, self.status, self.user_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Order instance"""
        sql = """
            DELETE FROM orders
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, phone_id, quantity, order_date, status, user_id):
        """Initialize a new Order instance and save the object to the database"""
        order = cls(phone_id, quantity, order_date, status, user_id)
        order.save()
        return order

    @classmethod
    def instance_from_db(cls, row):
        """Return an Order object having the attribute values from the table row"""
        order = cls.all.get(row[0])
        if order:
            order.phone_id = row[1]
            order.quantity = row[2]
            order.order_date = row[3]
            order.status = row[4]
            order.user_id = row[5]
        else:
            order = cls(row[1], row[2], row[3], row[4], row[5])
            order.id = row[0]
            cls.all[order.id] = order
        return order

    @classmethod
    def get_all(cls):
        """Return a list containing one Order object per table row"""
        sql = """
            SELECT *
            FROM orders
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_quantity(cls, quantity):
        """Return a list of Order objects corresponding to all table rows matching the specified quantity"""
        sql = """
            SELECT *
            FROM orders
            WHERE quantity = ?
        """
        rows = CURSOR.execute(sql, (quantity,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_status(cls, status):
        """Return a list of Order objects corresponding to all table rows matching the specified quantity"""
        sql = """
            SELECT *
            FROM orders
            WHERE status = ?
        """
        rows = CURSOR.execute(sql, (status,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return an Order object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM orders
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def user(self):
        """Return the user associated with this order"""
        from models.user import User  # Assuming User class exists
        return User.find_by_id(self.user_id)

    def phone(self):
        """Return the phone associated with this order"""
        from models.phone import Phone  # Assuming Phone class exists
        return Phone.find_by_id(self.phone_id)
