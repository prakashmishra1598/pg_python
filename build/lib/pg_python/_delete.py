def make_postgres_delete_statement(table, kv_map, debug):
    _prefix = "DELETE FROM "
    keys = " and ".join([k + "=%s" for k in kv_map.keys()])
    statement = " ".join([_prefix, table, " where ", keys])
    if debug:
        print("Writing into Db: %s, %s" % (statement, kv_map.values()))
    return statement, kv_map.values()