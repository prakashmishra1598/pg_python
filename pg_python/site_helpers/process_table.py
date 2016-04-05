"""
Package to process a table
"""


def remove_rows(table, row_numbers):
    """
    :param table: 2d array
    :param row_numbers: list of row numbers to delete, starts from 0
    :return: modified table
    """
    ret_val = []
    if table is None or len(table) == 0:
        return []
    for row in range(0, len(table)):
        if row not in row_numbers:
            ret_val.append(row)
    return ret_val

def get_cols(table, col_numbers):
    """
    :param table: 2d array
    :param row_numbers: list of row numbers to delete, starts from 0
    :return: modified table
    """
    ret_val = []
    if table is None or len(table) == 0:
        return []
    for row in range(0, len(table)):
        row_values = []
        for col in range(0, len(table[0])):
            if col in col_numbers:
                row_values.append(col)
        ret_val.append(row_values)
    return ret_val

