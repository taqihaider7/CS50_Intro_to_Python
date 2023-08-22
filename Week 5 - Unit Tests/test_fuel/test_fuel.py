from fuel import gauge, convert
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert('cat/1')

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(20) == "20%"

def test_convert():
    assert convert("1/100") == 1
    assert convert("50/100") == 50

