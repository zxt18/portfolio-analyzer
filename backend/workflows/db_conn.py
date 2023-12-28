import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL 
# Configure the database connection
class MySQLDatabase(): 
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def __init__(self):
        config = {
            "drivername": "mysql+pymysql",
            "host": "localhost",
            "port": 3306,
            "username": "zatan",
            "password": "abc123",
            "database": "earnings",
            "query" : {}
        }
        url = URL(**config)
        engine = create_engine(url)
        self._engine = engine

    def query_to_pandas(self,query):
        with self._engine.connect() as connection :  
            return pd.read_sql(query, connection)

db = MySQLDatabase()
name_list = ("CPS", "AAPL")
query = f"""    
    SELECT bs.act_symbol, bs.date, bs.period, bs.common_stock,  bs.shares_outstanding
    FROM balance_sheet_equity AS bs
    WHERE bs.act_symbol IN {name_list}
    AND bs.period = 'Year'
    LIMIT 100"""
df = db.query_to_pandas(query)
