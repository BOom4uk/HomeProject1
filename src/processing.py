def filter_by_state(list_of_dicts: list, parameter: str = 'EXECUTED') -> list:
    """Принимает список словарей и значение ключа state(по умолчанию - EXECUTED)
    Возвращает изменённый список словарей, у которых ключ state
    изменён на указанный ключ"""

    if isinstance(list_of_dicts, list) and isinstance(parameter, str):
        return [line for line in list_of_dicts if line.get("state") == parameter]
    else:
        raise Exception('Некорректный тип данных')

def sort_by_date(list_of_dicts: list, is_sort: bool = True) -> list:
    """Принимает список словарей и значение сортировки(по умолчанию - True)
    Возвращает список, отсортированный по дате"""

    if isinstance(list_of_dicts, list) and isinstance(is_sort, bool):
        result = sorted(list_of_dicts, key=lambda x: x.get('date'), reverse=is_sort)
        return result
    else:
        raise Exception('Некорректный тип данных')