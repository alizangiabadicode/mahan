import sqlite3

class DataAccess:
  def connection():
    conn= sqlite3.connect('/Users/kasrarh/Desktop/mahan_db.db')
    return conn
  def execute(sql,args):
    conn=DataAccess.connection()
    conn.cursor().execute(sql,args)
    conn.commit()
    conn.close()
  
  def fetch_one(sql,args):
    conn=DataAccess.connection()
    c=conn.cursor()
    c.execute(sql,args)
    data=c.fetchone()
    conn.commit()
    conn.close()
    return data

  def fetch_all(sql,args):
    conn=DataAccess.connection()
    c=conn.cursor()
    c.execute(sql)
    data=c.fetchall()
    conn.commit()
    conn.close()
    return data