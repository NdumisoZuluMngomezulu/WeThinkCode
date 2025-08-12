import pytest
from bank import value

def test_hello():
    assert value("hello") == "$0"

def test_firstH():
    assert(value)("hallelujah") == "$20"

def test_notH():
    assert("Sawubona") == "$100"

def test_Integer():
    with pytest.raises(TypeError):
        value(10)

def test_bool():
    with pytest.raises(TypeError):
        value(True)

