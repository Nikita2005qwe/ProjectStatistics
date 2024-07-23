from re import split

def uploadDict(string: str, dict_with_statistics: dict[str, int],
               function_result: callable, splitting: bool = False, *args) -> None:
    elements_in_string = string
    if splitting:
        elements_in_string: list[str] = split(r"[-,.! /<>():;?\n\t ]+", string)
    
    for element in elements_in_string:
        if not element:
            continue
        try:
            dict_with_statistics[element] += function_result(*args)
        except KeyError:
            dict_with_statistics[element] = function_result(*args)
