def make_postgres_write_statement(table, kv_map, debug=True):
    _prefix = "INSERT INTO"
    keys = ",".join(kv_map.keys())
    values = []
    for value in kv_map.values():
      if type(value) == bool:
        if value == True:
          values.append('true')
        else:
          values.append('false')
      else:
        values.append(value)
  
    value_proxy_array = ["%s"] * len(kv_map)
    value_proxy_string = ", ".join(value_proxy_array)
    statement = " ".join([_prefix, table, "(", keys ,")", "VALUES", "(", value_proxy_string ,")"])
    if debug:
      print("Writing into Db: %s, %s" % (statement, values))
    return statement, kv_map.values()



def get_multi_insert_str(columns_to_insert,insert_values_dict_lst):
    """
    get_multi_insert_str creates the string for multiple insertion values.
    :param columns_to_insert:
    :param insert_values_dict_lst:
    :return:
    """
    dict_lst = []
    for row in insert_values_dict_lst:
        value_lst = []
        for col in columns_to_insert:
            value_lst.append("'"+row[col]+"'")
        row_col_str = "(" + ",".join(value_lst) + ")"
        dict_lst.append(row_col_str)
    insert_str = ",".join(dict_lst)
    return insert_str



def make_postgres_write_multiple_statement(table, columns_to_insert_lst, insert_values_dict_lst, print_debug_log=True):
    """
    make_postgres_write_multiple_statement generates the posgresql query.

    :param table:
    :param columns_to_insert_lst:
    :param insert_values_dict_lst:
    :param print_debug_log:
    :return:
    """
    prefix = "INSERT INTO"
    TABLE_NAME = table
    columns_str = "("+",".join(columns_to_insert_lst) + ")"
    insert_columns = get_multi_insert_str(columns_to_insert_lst, insert_values_dict_lst)
    statement = " ".join([prefix, TABLE_NAME, columns_str, "VALUES", insert_columns])
    return statement

