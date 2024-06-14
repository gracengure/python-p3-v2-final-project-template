from models.__init__ import CURSOR, CONN

class User:
    # Dictionary to store all User objects saved to the database.
    all = {}

    def __init__(self, name, email, phone_number, id=None):
        self.id = id
        self._name = name
        self._email = email
        self._phone_number = phone_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        # Validate that phone number is an integer.
        if isinstance(value, int):
            self._phone_number = value
        else:
            raise ValueError("Phone number must be an integer")

    def __repr__(self):
        # Return a string representation of the User object.
        return f"<User {self.id}: Name='{self.name}', Email='{self.email}', Phone Number='{self.phone_number}'>"

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of User instances."""
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                phone_number INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists User instances."""
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the user details into the users table."""
        sql = """
            INSERT INTO users (name, email, phone_number)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.email, self.phone_number))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current User instance."""
        sql = """
            UPDATE users
            SET name = ?, email = ?, phone_number = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.email, self.phone_number, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current User instance,
        delete the dictionary entry, and reassign id attribute."""
        sql = """
            DELETE FROM users
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key.
        del type(self).all[self.id]

        # Set the id to None.
        self.id = None

    @classmethod
    def create(cls, name, email, phone_number):
        """Initialize a new User instance and save the object to the database."""
        user = cls(name, email, phone_number)
        user.save()
        return user

    @classmethod
    def instance_from_db(cls, row):
        """Return a User object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key.
        user = cls.all.get(row[0])
        if user:
            # Ensure attributes match row values in case local instance was modified.
            user.name = row[1]
            user.email = row[2]
            user.phone_number = row[3]
        else:
            # Not in dictionary, create new instance and add to dictionary.
            user = cls(row[1], row[2], row[3])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        """Return a list containing one User object per table row."""
        sql = """
            SELECT *
            FROM users
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        """Return a list of User objects with the specified name."""
        sql = """
            SELECT *
            FROM users
            WHERE name = ?
        """
        rows = CURSOR.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a User object corresponding to the table row matching the specified primary key."""
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def orders(self):
        """Return a list of orders associated with the current user."""
        from models.order import Order
        sql = """
            SELECT * FROM orders
            WHERE user_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [Order.instance_from_db(row) for row in rows]
