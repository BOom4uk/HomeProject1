from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state
from src.widget import get_date, mask_account_card

print(mask_account_card('Счет 123456'))
print(get_mask_card_number(''))
print(get_mask_account("12"))
print(get_date("2024-03-11T02:26:18.671407"))
print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )
)
