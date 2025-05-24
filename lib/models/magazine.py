from lib.db.connection import get_connection
class Magazine:
    all = {}
    def __init__(self,name, category, id = None):
        self.name = name 
        self.id = id
        self.category = category

    @property 
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError("Name must be a string.")
        
        if len(val) < 3:
            raise ValueError("Name must be longer than three characters.")
        
        self._name = val

    @property 
    def category(self):
        return self._category
    
    @category.setter 
    def category(self, val):
        if not isinstance(val, str):
            raise TypeError("Category must be a string.")
        
        if len(val) < 3:
            raise ValueError("Category must be longer than three characters.")
        
        self._category = val

    def save(self):
        sql = """
        INSERT INTO magazines (name, category)
        VALUES (?, ?)
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(sql, (self.name, self.category,))
        
        self.id = cursor.lastrowid
        Magazine.all[self.id] = self

        conn.commit()
        conn.close()
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT * FROM magazines 
        WHERE id = ?
        """

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(sql,(id,))
        row = cursor.fetchone()

        if row:
            return Magazine(name=row[1], category=row[2], id=row[0])
        else:
            raise Exception(f"No Magazine found with an id of {id} ")
        
    @classmethod
    def find_by_name(cls, name):
        sql = """
        SELECT * FROM magazines 
        WHERE name = ?
        """

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(sql,(name,))
        row = cursor.fetchone()

        if row:
            return Magazine(name=row[1], category=row[2], id=row[0])
        else:
            raise Exception(f"No Magazine found with an name of {name} ")
        
    @classmethod
    def find_by_category(cls, category):
        sql = """
        SELECT * FROM magazines 
        WHERE category = ?
        """

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(sql,(category,))
        row = cursor.fetchone()

        if row:
            return Magazine(name=row[1], category=row[2], id=row[0])
        else:
            raise Exception(f"No Magazine found with an category of {category} ")
        
        