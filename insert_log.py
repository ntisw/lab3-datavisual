from datetime import datetime
from db_util import Db_util
db_util = Db_util()

class Insert_log:

    def insert(self,type,data_):
        cdatetime = str(datetime.now())
        sql = """INSERT INTO data_log (type, data, cdate) VALUES (%s,%s,%s)"""
        data =(type, data_, cdatetime)
        db_util.execute_sql(sql, data)