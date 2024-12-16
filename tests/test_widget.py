import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_type():
    mask_account_card("Visa Platinum 1234123412341234")
    mask_account_card("Visa 1234123412341234")
    assert mask_account_card("Счет 123456") == "Счет **3456"


def test_mask_account_card_negative():
    with pytest.raises(Exception):
        mask_account_card("-Visa Platinum 1234123412341234")


def test_get_date():
    get_date("2024-03-11T02:26:18.671407")


def test_get_date_wrong():
    with pytest.raises(Exception):
        get_date("2024-03s11T02:26:18.671407")
        get_date("20240311T02:26:18.671407")
        get_date("")
