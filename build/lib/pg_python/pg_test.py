import pg_python

pg_python.pg_server("crawler", "postgres", "@hawkerIndia", "postgres-master.hawker.news", False)
pg_python.delete("xyz", {"key": "1000", "name": "2000"})