import pytest
from twttr import shorten

def test_default():
    assert shorten("Hello World")
  
def test_argument():
    assert shorten("David") == "Dvd"
    assert shorten("mngomezulu") == "mngmzl"

def test_num():
    with pytest.raises(TypeError):
        shorten(5)

def test_bool():
    with pytest.raises(TypeError):
        shorten(False)
