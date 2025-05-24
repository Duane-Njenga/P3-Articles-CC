import pytest
from lib.models.magazine import Magazine

def test_create_magazine():
    mag = Magazine("Test Mag", "Test Category")
    mag.save()
    assert mag.id is not None