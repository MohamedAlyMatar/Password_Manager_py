import pytest
from functions import *


def test_validate():
    assert validate("test@example.com") == True
    assert validate("invalid_email") == False
    assert validate("test@com") == False

def test_check_password_level():
    assert check_password_level("weakpassword") == "weak"
    assert check_password_level("StrongPassword123") == "strong"
    assert check_password_level("DiamondPa$$word123") == "diamond"
    assert check_password_level("123456789") == "Unknown"

def test_validate_password():
    assert validate_password("weakpassword", "weak") == True
    assert validate_password("StrongPassword123", "strong") == True
    assert validate_password("DiamondPa$$word123", "diamond") == True
    assert validate_password("123456789", "Unknown") == False

def test_add_password():
    # Test adding a valid password
    account = "test@example.com"
    password = "StrongPassword123"
    assert passwords.get(account) == None
    assert validate(account) == True
    assert check_password_level(password) == "strong"
    assert validate_password(password, "strong") == True
    assert add_password(account, password) == "Password added successfully!"
    assert passwords.get(account) == password

    # Test adding an invalid password
    account = "test2@example.com"
    password = "123456789"
    assert passwords.get(account) == None
    assert validate(account) == True
    assert check_password_level(password) == "Unknown"
    assert validate_password(password, "Unknown") == False
    assert add_password(account, password) == "Invalid password."
    assert passwords.get(account) == None

def test_retrieve_password():
    # Test retrieving an existing password
    account = "test@example.com"
    password = "StrongPassword123"
    assert passwords.get(account) == password
    assert retrieve_password(account) == f"Password for {account}: {password}"

    # Test retrieving a password that doesn't exist
    account = "test2@example.com"
    assert passwords.get(account) == None
    assert retrieve_password(account) == f"No password found for {account}."

def test_update_password():
    # Test updating an existing password with a valid password
    account = "test@example.com"
    old_password = passwords.get(account)
    password = "NewStrongPassword123"
    assert old_password != password
    assert validate(account) == True
    assert check_password_level(password) == "strong"
    assert validate_password(password, "strong") == True
    assert update_password(account, password) == "Password updated successfully!"
    assert passwords.get(account) == password

    # Test updating an existing password with an invalid password
    account = "test@example.com"
    old_password = passwords.get(account)
    password = "123456789"
    assert old_password != password
    assert validate(account) == True
    assert check_password_level(password) == "Unknown"
    assert validate_password(password, "Unknown") == False
    assert update_password(account, password) == "Invalid password."
    assert passwords.get(account) == old_password

def test_get_account_names():
    # Test getting account names when passwords dictionary is not empty
    passwords["test@example.com"] = "StrongPassword123"
    passwords["test2@example.com"] = "DiamondPa$$word123"
    assert get_account_names() == ["test@example.com", "test2@example.com"]

    # Test getting account names when passwords dictionary is empty
    passwords.clear()
    assert get_account_names() == []