def get_mask_card_number(number_of_card: str) -> str:
    """Маскирует номер банковской карты"""
    if len(number_of_card) == 16 and number_of_card.isdigit():
        masked_card = number_of_card[:5] + "******" + number_of_card[12:]
        return masked_card
    else:
        raise Exception("Номер карты должен содержать 16 цифр")


def get_mask_account(number_of_account: str) -> str:
    """Маскирует номер счёта"""
    if number_of_account.isdigit() and len(number_of_account) > 5:
        masked_account = "**" + number_of_account[2:]
        return masked_account
    else:
        raise Exception("Неверный номер счёта")
