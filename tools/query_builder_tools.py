from typing import Union


def create_query_list(s: Union[list, str]) -> list:
    '''
    Returns lists of query elements

    Parameters:
        s (list or str): string or list of strings

    Returns:
        list: list of query elements 
    '''
    if type(s) is str:
        query_list = [s]
    else:
        query_list = [str(element) for element in s]
    return query_list