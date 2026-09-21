from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import uvicorn

from db import fetchall

app = FastAPI()

@app.get("/api/iscrizioni/{citta}")
def get_iscrizioni_by_city(citta: str):
    citta_clean = citta.strip().lower()

    result = fetchall(
                        """
                       SELECT iscrizioni.id AS ID_Iscrizione, utenti.nome, utenti.cognome, utenti.citta, articoli.descrizione, articoli.prezzo
                        FROM iscrizioni, articoli, contiene, carrello, utenti
                        WHERE iscrizioni.id = articoli.id
                        AND articoli.id = contiene.id_articolo
                        AND contiene.id_carrello = carrello.id_carrello
                        AND carrello.id_utente = utenti.id_utente
                        AND utenti.citta = %s
                        """
                        , [citta_clean]
                        )
    
    return result



app.mount("/", StaticFiles(directory="statics", html=True), name="static")

uvicorn.run(app, host="127.0.0.1", port=8000)
