from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_of_card_or_account: str) -> str:
    """Маскирует номер карты или счета"""
    parts_of_card_or_account = number_of_card_or_account.split(" ")
    type_of_card_or_account = parts_of_card_or_account[0]
    number = parts_of_card_or_account[-1]
    """Проверка на специальный тип карты"""
    if (
        "Classic" in number_of_card_or_account
        or "Gold" in number_of_card_or_account
        or "Platinum" in number_of_card_or_account
    ):
        type_of_card = parts_of_card_or_account[1]
        if type_of_card_or_account in ["Visa", "Mastercard", "Maestro"]:
            masked_number = get_mask_card_number(number)
            return f"{type_of_card_or_account} {type_of_card} {masked_number}"
    """Проверка на карту или счет"""
    if type_of_card_or_account in ["Visa", "Mastercard", "Maestro"]:
        masked_number = get_mask_card_number(number)
    elif type_of_card_or_account == "Счет":
        masked_number = get_mask_account(number)
    else:
        raise Exception("Неизвестный тип карты или счета")

    return f"{type_of_card_or_account} {masked_number}"


def get_date(date: str) -> str:
    if len(date) > 5:
        if date[4] == '-' and date[7] == '-':
            return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    raise Exception("Неизвестный тип даты")
