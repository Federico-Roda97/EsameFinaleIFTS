from db import fetchall
from pprint import pprint

print("TABELLA UTENTI")
result = fetchall("Select * from utenti")
pprint(result)

print("TABELLA ORDINI")
result = fetchall("Select * from ordini")
pprint(result)

citta = input("Inserisci citta: ")
result = fetchall("""
SELECT *
FROM ordini AS o
JOIN carrello AS ca ON o.id_carrello = ca.id_carrello
JOIN utenti AS u ON ca.id_utente = u.id_utente 
WHERE u.citta LIKE %s
""", [f"%{citta}%"])

print(f"RISULTATI PER {citta.upper()}")
pprint(result)