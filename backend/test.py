from db import fetchall
from pprint import pprint

print("TABELLA UTENTI")
result = fetchall("Select * from utenti")
pprint(result)

print("TABELLA ORDINI")
result = fetchall("Select * from ordini")
pprint(result)



