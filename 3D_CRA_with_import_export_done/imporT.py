import csv
import MySQLdb
import sys
import db_code 
from models import *
import insert
from commands import *
from setup import *

dbsession = get_db_session()
class Import():
    def __init__(self):
        self.dbsession = get_db_session()
        db_code.setup_db()
    def import1(self, fileName, tableName):
            data = {}
            index = 0
            cf = csv.reader(open(fileName+".csv", 'rb'), delimiter = ',')
            for fields in cf:
                    for i, f in enumerate(fields):
                        data[index] = f
                        index += 1
                    ist = data[0]
                    second = data[1]
                    third = data[2]
                    fourth = data[3]
                    fifth = data[4]
                    if tableName == "calls":
                            c_db(ist, second, third, fourth, fifth)
                    elif tableName == "emails":
                            e_db(ist, second, third, fourth, fifth)               
                    elif tableName == "msgs":
                            m_db(ist, second, third, fourth, fifth)                    
                    elif tableName == "persons":
                            p_db(ist, second, third, fourth, fifth)
                    cf.next()
