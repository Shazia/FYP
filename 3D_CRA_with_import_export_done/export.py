import csv
import MySQLdb
import sys
from db_code import get_db_session
from models import *
import insert
from commands import *

dbsession = get_db_session()
class Export():
    def __init__(self):
        #self.dbsession = get_db_session()
        self.conn = MySQLdb.connect(host = "localhost",
                                    user = "root",
                                    passwd = "iostream",
                                    db = "contacts"
                                    )
        self.cursor = self.conn.cursor()

    def export1(self, fileName, tableName):
        self.cursor.execute("select * from "+ tableName + ";")
        csv_writer = csv.writer(open(fileName+".csv", "wt"))
        csv_writer.writerow([i[0] for i in self.cursor.description]) # write headers
        csv_writer.writerows(self.cursor)
        del csv_writer # this will close the CSV file

