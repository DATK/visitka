import sqlite3 as sq
import datetime


class Otsovik:

    def __init__(self,db="dbots.db") -> None:
        self.connect=sq.connect(f"./src/{db}")
        self.cursor=self.connect.cursor()
        self.crt_table='''CREATE TABLE "ots"(
        "ID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "Name" TEXT NOT NULL,
        "Text" TEXT NOT NULL,
        "Date" TEXT NOT NULL
        ); '''
        self.ins='INSERT INTO ots (Name,Text, Date) VALUES (?,?,?);'
        self.sel='SELECT * FROM ots'
        self.dl='DELETE FROM ots'
        self.create_table()


    def create_table(self):
        try:
            self.cursor.execute(self.crt_table)
            self.connect.commit()
        except:
            pass
    
    def add(self,name,text):
        self.cursor.execute(self.ins,(name,text,str(datetime.datetime.now())))
        self.connect.commit()

    def get(self):
        self.cursor.execute(self.sel)
        data=self.cursor.fetchall()
        res=[]
        for i in data:
            res.append(f"{i[1]} написал: {i[2]}")
        return res

    def delete(self):
        self.cursor.execute(self.dl)
        self.connect.commit()

    def close(self):
        self.connect.close()

    def __del__(self):
        self.close()