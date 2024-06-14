from models.__init__ import CURSOR, CONN

class Phone:

    # Dictionary to keep track of all Phone instances created.
    all = {}

    def __init__(self, brand, model, price, stock, id=None):
        self.id = id
        self.brand = brand
        self.model = model
        self.price = price
        self.stock = stock

    def __repr__(self):
        return  f"<Phone {self.id}: Brand='{self.brand}', Model='{self.model}', Price={self.price}, Stock={self.stock}>"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        # Ensure brand is a non-empty string
        if isinstance(brand, str) and len(brand):
            self._brand = brand
        else:
            raise ValueError("Brand must be a non-empty string")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        # Ensure model is a non-empty string
        if isinstance(model, str) and len(model):
            self._model = model
        else:
            raise ValueError("Model must be a non-empty string")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        # Ensure price is a non-negative number
        if isinstance(price, (int, float)) and price >= 0:
            self._price = price
        else:
            raise ValueError("Price must be a non-negative number")

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        # Ensure stock is a non-negative integer
        if isinstance(stock, int) and stock >= 0:
            self._stock = stock
        else:
            raise ValueError("Stock must be a non-negative integer")

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Phone instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS phones (
                id INTEGER PRIMARY KEY,
                brand TEXT,
                model TEXT,
                price REAL,
                stock INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Phone instances"""
        sql = """
            DROP TABLE IF EXISTS phones;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the phone details into the phones table"""
        sql = """
            INSERT INTO phones (brand, model, price, stock)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.brand, self.model, self.price, self.stock))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Phone instance"""
        sql = """
            UPDATE phones
            SET brand = ?, model = ?, price = ?, stock = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.brand, self.model, self.price, self.stock, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Phone instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM phones
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, brand, model, price, stock):
        """Initialize a new Phone instance and save the object to the database"""
        phone = cls(brand, model, price, stock)
        phone.save()
        return phone

    @classmethod
    def instance_from_db(cls, row):
        """Return a Phone object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key
        phone = cls.all.get(row[0])
        if phone:
            # Ensure attributes match row values in case local instance was modified
            phone.brand = row[1]
            phone.model = row[2]
            phone.price = row[3]
            phone.stock = row[4]
        else:
            # Not in dictionary, create new instance and add to dictionary
            phone = cls(row[1], row[2], row[3], row[4])
            phone.id = row[0]
            cls.all[phone.id] = phone
        return phone

    @classmethod
    def get_all(cls):
        """Return a list containing one Phone object per table row"""
        sql = """
            SELECT *
            FROM phones
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_price(cls, price):
        """Return a list of Phone objects corresponding to all table rows matching the specified price"""
        sql = """
            SELECT *
            FROM phones
            WHERE price = ?
        """
        rows = CURSOR.execute(sql, (price,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_brand(cls, brand):
        """Return a list of Phone objects corresponding to all table rows matching the specified brand"""
        sql = """
            SELECT *
            FROM phones
            WHERE brand = ?
        """
        rows = CURSOR.execute(sql, (brand,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Phone object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM phones
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def orders(self):
        """Return list of orders associated with the current phone"""
        from models.order import Order
        sql = """
            SELECT * FROM orders
            WHERE phone_id = ?
        """
        CURSOR.execute(sql, (self.id,))

        rows = CURSOR.fetchall()
        return [Order.instance_from_db(row) for row in rows]