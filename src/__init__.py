from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

print(mask_account_card("Visa Platinum 1234123412341234"))
print(get_date("2024-03-11T02:26:18.671407"))
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], 'ss'))
