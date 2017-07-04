import pg_python
import unittest
import requests

COL_1 = "col1"
COL_2 = "col2"
COL_3 = "col3"
COL_4 = "col4"
UPDATE = "update"
test_table = "pg_python_test"

class TestTests(unittest.TestCase):

    def test_update(self):
        pg_python.pg_server("crawler", "postgres", "@hawkerIndia", "postgres-master.hawker.news", False)
        create_rows()
        dict_lst =[
            {COL_1:'title1', UPDATE:'updated_name1'},
            {COL_1: 'title2', UPDATE: "update'd_name2"}
        ]
        pg_python.update_multiple(test_table,COL_4,[COL_1],dict_lst)
        title1 = pg_python.read(test_table,[COL_4],{COL_1:'title1'})
        title2 = pg_python.read(test_table, [COL_4], {COL_1: 'title2'})
        self.assertEqual(title1[0][COL_4],'updated_name1')
        self.assertEqual(title2[0][COL_4], "update'd_name2")

        clear_table()

    def test_single_update(self):
        pg_python.pg_server("crawler", "postgres", "@hawkerIndia", "postgres-master.hawker.news", False)
        create_rows()
        pg_python.update(test_table,{COL_4:'updated_name1'},{COL_1:'title1%'},clause='ilike')
        title1 = pg_python.read(test_table,[COL_4],{COL_1:'title15'})
        self.assertEqual(title1[0][COL_4],'updated_name1')

        clear_table()


    def test_multiple_insert(self):
        pg_python.pg_server("crawler", "postgres", "@hawkerIndia", "postgres-master.hawker.news", False)
        column_to_insert = [COL_1, COL_3]
        insert_dict_list = [
            {COL_1: "insert1", COL_3: 1},
            {COL_3: 2, COL_1: "insert2"},
            {COL_1: "insert3", COL_3: 3}
        ]
        pg_python.insert_multiple(test_table,column_to_insert,insert_dict_list)
        val1 = pg_python.read(test_table,[COL_1],{COL_3:1})
        val2 = pg_python.read(test_table, [COL_1], {COL_3: 2})
        val3 = pg_python.read(test_table, [COL_1], {COL_3: 3})
        values = [val1[0][COL_1],val2[0][COL_1],val3[0][COL_1] ]
        self.assertEqual(values,["insert1","insert2","insert3"])
        clear_table()





def create_rows():
    pg_python.write(test_table, {COL_1: "title1", COL_2: "read", COL_3: 76, COL_4: "reeer"})
    pg_python.write(test_table, {COL_1: "title2", COL_2: "read2", COL_3: 77, COL_4: "reeer"})
    pg_python.write(test_table, {COL_1: "title3", COL_2: "read3", COL_3: 77, COL_4: "reeer"})
    pg_python.write(test_table, {COL_1: "title4", COL_2: "read4", COL_3: 77, COL_4: "reeer"})
    pg_python.write(test_table, {COL_1: "title15", COL_2: "read5", COL_3: 77, COL_4: "reeer"})
    pg_python.write(test_table, {COL_1: "title6", COL_2: "read6", COL_3: 77, COL_4: "reeer"})

def clear_table():
    pg_python.write_raw("Delete from %s"%(test_table), None)

