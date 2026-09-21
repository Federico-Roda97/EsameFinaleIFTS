import mysql.connector as sql

def fetchall(query, params=None):
  conn = sql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="fit_net"
  )
  cursor = conn.cursor(dictionary=True)
  cursor.execute(query, params)
  return cursor.fetchall()

