import pytest
from lib.models.author import Author

def test_create_author():
    author = Author("Test Author")
    author.save()
    assert author.id is not None

def test_find_by_id():
    author = Author("Find Me")
    author.save()
    found = Author.find_by_id(author.id)
    assert found.name == "Find Me"