import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_float():
    with pytest.raises(Exception):
        get_mask_card_number("1234123412341234.0")


def test_get_mask_card_number_negative_17_symbols():
    with pytest.raises(Exception):
        get_mask_card_number("-1234123412341234")


def test_get_mask_card_number_empty():
    with pytest.raises(Exception):
        get_mask_card_number("")


def test_get_mask_account_float():
    with pytest.raises(Exception):
        get_mask_account("123412341234.0")


def test_get_mask_account_less_waiting_length():
    with pytest.raises(Exception):
        get_mask_account("12")


def test_get_mask_account_negative():
    with pytest.raises(Exception):
        get_mask_account("-123412341234")
