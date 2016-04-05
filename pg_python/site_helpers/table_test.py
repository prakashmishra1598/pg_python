import unittest
import requests
from table import get_table
__author__ = 'gaurav'

class TestTable(unittest.TestCase):

    def test_get_request_multiple(self):
        r = requests.get('http://99v.info/html/html_tables.html')
        num_tables, tables = get_table(r.text)
        for table in tables:
            print table['title']
        assert num_tables == 11

    def test_no_tables(self):
        r = requests.get('http://www.w3.org/TR/html401/struct/tables.html')
        num_tables, tables = get_table(r.text)
        assert num_tables == 0

    def test_get_request_multiple_2(self):
        r = requests.get('http://accessiblehtml.sourceforge.net/html_tables_cookbook.html')
        num_tables, tables = get_table(r.text)
        assert num_tables == 11

    def test_get_real_life(self):
        r = requests.get('http://www.atbltd.com/assets/Documents/auctionprices.htm')
        num_tables, tables = get_table(r.text)
        print num_tables
        for table in tables:
            print table['data'][0]
        return True


if __name__=='__main__':
    unittest.main()
pass


