import pytest 
from lib.db.connection import get_connection
from lib.models.magazine import Magazine

def setup_function():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM authors")
    conn.commit()
    conn.close()

def test_create_magazine():
    mag = Magazine("Test Mag", "Test Category")
    mag.save()
    assert mag.id is not None

def test_find_by_id():
    mag = Magazine("Test Mag", "Test Category")
    mag.save()
    found = Magazine.find_by_id(mag.id)
    assert found.name ==  "Test Mag"

def test_find_by_name():
    mag = Magazine("Test Mag", "Test Category")
    mag.save()
    found = Magazine.find_by_name(mag.name)
    assert found.name ==  "Test Mag"

def test_find_by_category():
    mag = Magazine("Test Mag", "Test Category")
    mag.save()
    found = Magazine.find_by_category(mag.category)
    assert found.category ==  "Test Category"

def test_valid_name_setter():
    mag = Magazine("Initial Name", "Test Category")
    mag.name = "Updated Name"
    assert mag.name == "Updated Name"

def test_invalid_name_type():
    with pytest.raises(TypeError):
        mag = Magazine(123, "Test Cat")  

def test_invalid_name_length():
    with pytest.raises(ValueError):
        mag = Magazine("", "Test Cat") 

def test_valid_category_setter():
    mag = Magazine("Test Name", "Init Category")
    mag.category = "Updated Category"
    assert mag.category == "Updated Category"

def test_invalid_category_type():
    with pytest.raises(TypeError):
        mag = Magazine("Test Name", 123)  

def test_invalid_category_length():
    with pytest.raises(ValueError):
        mag = Magazine("Test Name", "") 