import sqlite3
import os
import sys


class UsedSqliteDB():
    def __init__(self, dbfile):
        self.db = dbfile
        self.conn = sqlite3.connect(dbfile)
        self.cur = sqlite3.connect(dbfile).cursor()


def createdb(db):
    pass

def gemeinde(db):

    sql = """
            CREATE TABLE gemeinde('gdenr' integer, 'gde_bez' text, 'gde_typ' text, 'bm_name' text, 'bm_typ' text);

            """
    db.cur.execute(sql)
    

def ewdaten(db):

    sql = """
        CREATE TABLE ew('gdenr' integer, 'Jahr_3006' integer, 'altersgruppe' text, 'm_w' text, 'anzahl' integer, FOREIGN KEY (gdenr) REFERENCES gemeinde(gdenr)); 
        """
    db.cur.execute(sql)

def EW_u20(db):
    pass

conn = None
dbfile="haushalt.db"

if os.path.exists(dbfile):
    print("database already in place - just input new tables")
    try: 
        conn = sqlite3.connect(dbfile)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


db = UsedSqliteDB(dbfile)

if db.cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='gemeinde';").fetchone()[0] > 0:
    print("Table 'gemeinde' exists")

else:
    gemeinde(db)


if db.cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='ew';").fetchone()[0] > 0:
    print("Table 'ew' exists")

else:
    ewdaten(db)



