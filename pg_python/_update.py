def make_postgres_update_statement(table, kv_map, where_kv_map, clause, debug = True):
    _prefix = "UPDATE"
    clause = " " + clause + " "
    keys = ", ".join([k + "=%s" for k in kv_map.keys()])
    where_keys = " AND ".join([k + clause + "%s" for k in where_kv_map.keys()])
    value_proxy_array = ["%s"] * len(kv_map)
    value_proxy_string = ", ".join(value_proxy_array)
    statement = " ".join([_prefix, table, "SET", keys, "WHERE", where_keys])
    if debug:
      print("Updating into Db: %s, %s" %(statement, kv_map.values() + where_kv_map.values()))
    return statement, kv_map.values() + where_kv_map.values()



def get_from_clause(query_values_dict_lst,columns_to_query_lst):
    """
    get_from_clause will return the from clause that contains all tuples.
    :param query_values_dict_lst: list of dictionary for values to set.
    :param columns_to_query_lst: columns for where clause
    :return:
    """
    from_str = ""
    for row in query_values_dict_lst:
        temp_str = "("
        for column_name in columns_to_query_lst:
            col_val = row[column_name]
            if isinstance(col_val, basestring):
                temp_str = temp_str + "'" + col_val.replace("'","''") + "'" + ","
            else:
                temp_str = temp_str + str(col_val) + ","

        update_value = row['update']
        if isinstance(update_value, basestring):
            temp_str = temp_str + "'" + update_value.replace("'","''") + "'"
        else:
            temp_str = temp_str + str(update_value)
        temp_str = temp_str + ")"
        from_str = from_str + temp_str
        if row != query_values_dict_lst[-1]:
            from_str = from_str + ","
    from_clause = "from (values " + from_str + ")"
    return from_clause


def get_as_clause(columns_to_query_lst):
    """
    get_as_clause will return all column names tuples.
    :param columns_to_query_lst: columns for where clause
    :return:
    """
    column_str = ""
    for col in columns_to_query_lst:
        column_str = column_str + col + ","
    column_str += "update"
    as_clause = "as c(" + column_str + ")"
    return  as_clause

def get_where_clause(columns_to_query_lst):
    """
    get_where_clause returns the where clause from the given query list.
    :param columns_to_query_lst: columns for where clause.
    :return:
    """
    where_str = "where "
    for row in columns_to_query_lst:
        where_str = where_str + "c." + row + " = t." + row
        if row != columns_to_query_lst[-1]:
            where_str = where_str + " AND "
    return where_str


def make_postgres_update_multiple_statement(table,column_to_update,
                                            columns_to_query_lst,
                                            query_values_dict_lst,
                                            print_debug_log = True):
    """
    It makes query statement.
    :param table: table to update.
    :param column_to_update: column name that is to be updated.
    :param columns_to_query_lst: columns name that will we used for where clause.
    :param query_values_dict_lst: list of dictionary that contains values to update.
    :param print_debug_log:
    :return:
    """
    _prefix = "UPDATE"
    table_name = table + " as t"
    keys = column_to_update + " = c.update"
    from_clause = get_from_clause(query_values_dict_lst, columns_to_query_lst)
    as_clause = get_as_clause(columns_to_query_lst)
    where_clause = get_where_clause(columns_to_query_lst)
    statement = " ".join([_prefix, table_name, "SET", keys, from_clause, as_clause, where_clause])
    if print_debug_log == True:
       print("Updating multiple rows into db %s"%(statement))
    return  statement
