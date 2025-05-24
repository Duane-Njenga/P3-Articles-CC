import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.connection import get_connection

def setup_database():
    with open("lib/db/schema.sql", "r") as file:
        schema = file.read()

    conn = get_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()
    print("✅ Database has been set up successfully.")

if __name__ == "__main__":
    setup_database()
