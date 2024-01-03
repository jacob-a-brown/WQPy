from pandas import DataFrame

def parse_wqp_results_to_list(results) -> dict:
    '''
    WQP currently returns query results as a tsv. This function parses the
    results into a list.

    Parameters:
        results (str): csv results from querying WQP

    Returns
        list: list of rows results
    '''
    result_rows = results.split('\n')
    result_rows = [row.split('\t') for row in result_rows]
    return result_rows