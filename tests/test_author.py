import pytest 
from lib.db.connection import get_connection
from lib.models.author import Author

def setup_function():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM authors")
    conn.commit()
    conn.close()

def test_create_author():
    author = Author("Test Author")
    author.save()
    assert author.id is not None

def test_find_by_id():
    author = Author("Found by id")
    author.save()
    found = Author.find_by_id(author.id)
    assert found.name == "Found by id"

def test_find_by_name():
    author = Author("Found by name")
    author.save()
    found = Author.find_by_name(author.name)
    found.name == "Found by name"

def test_valid_name_setter():
    author = Author("Initial Name")
    author.name = "Updated Name"
    assert author.name == "Updated Name"

def test_invalid_name_type():
    with pytest.raises(ValueError):
        author = Author(123)  


