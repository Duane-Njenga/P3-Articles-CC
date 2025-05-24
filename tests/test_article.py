import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_create_article():
    author = Author("Writer")
    author.save()
    mag = Magazine("Cool Mag", "Culture")
    mag.save()
    article = Article("My Story", author.id, mag.id)
    article.save()
    assert article.id is not None