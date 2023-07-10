import pytest 
from functions import *
from main import passwords

@pytest.fixture
def sample_passwords():
    passwords.clear()
    passwords["account1"] = "Passw0rd"
    passwords["account2"] = "StrongPassword123"
    passwords["account3"] = "WeakPwd"
    passwords["account4"] = "D1amond!Password"


def test_check_password_level():
    assert check_password_level("password") == "weak"
    assert check_password_level("Passw0rd") == "strong"
    assert check_password_level("D1amond!Password") == "diamond"
    assert check_password_level("12345678") == "Unknown"


def test_validate_password(sample_passwords):
    assert validate_password("password", "weak") is True
    assert validate_password("Passw0rd", "strong") is True
    assert validate_password("WeakPwd", "strong") is False
    assert validate_password("D1amond!Password", "diamond") is True
    assert validate_password("12345678", "weak") is False


def test_add_password(sample_passwords):
    account = "new_account"
    password = "NewPassword123"
    level = "strong"

    add_password()
    assert account in passwords
    assert passwords[account] == password


def test_retrieve_password(sample_passwords, capsys):
    account = "account2"

    retrieve_password()
    captured = capsys.readouterr()
    assert captured.out.strip() == f"Password for {account}: {passwords[account]}"


def test_update_password(sample_passwords):
    account = "account3"
    password = "UpdatedPassword"
    level = "strong"

    update_password()
    assert passwords[account] == password


def test_get_account_names(sample_passwords):
    expected_names = ["account1", "account2", "account3", "account4"]
    names = get_account_names()
    assert sorted(names) == sorted(expected_names)
