import pytest
from validator import validate_password

def test_password_too_short():
    result = validate_password("Abc12")
    assert result["is_valid"] is False
    assert "TOO_SHORT" in result["reasons"]

def test_password_no_number():
    result = validate_password("Abcdefgh")
    assert result["is_valid"] is False
    assert "NO_NUMBER" in result["reasons"]

def test_password_no_uppercase():
    result = validate_password("abcdefgh1")
    assert result["is_valid"] is False
    assert "NO_UPPERCASE" in result["reasons"]

def test_password_is_null():
    result = validate_password(None)
    assert result["is_valid"] is False
    assert "IS_NULL" in result["reasons"]

def test_password_all_valid():
    result = validate_password("Abcdefgh1")
    assert result["is_valid"] is True
    assert len(result["reasons"]) == 0