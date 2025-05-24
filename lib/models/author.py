from lib.db.connection import get_connection


class Author:
    all = {}
    def __init__(self, name, id = None):
        self.name = name
        self.id = id


    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    def save(self):
        sql = """
        INSERT INTO authors (name) 
        VALUES (?)
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (self.name,))
        self.id = cursor.lastrowid

        Author.all[self.id] = self
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT * FROM authors 
        where id = ?
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()

        if row:
            return cls(name=row[1], id=row[0])
        else:
            raise Exception("Author not found with id of {id}")
        
    @classmethod
    def find_by_name(cls, name):
        sql = """
        SELECT * FROM authors 
        where name = ?
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (name,))
        row = cursor.fetchone()

        if row:
            return cls(name=row[1], id=row[0])
        else:
            return "Author not found"
        

        