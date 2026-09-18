from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import uvicorn

from db import fetchall

app = FastAPI()

@app.get("/api/ordini/{citta}")
def get_ordini_by_city(citta: str):
    citta_clean = citta.strip().lower()

    result = fetchall(
                        """
                        SELECT *
                        FROM ordini AS o
                        JOIN carrello AS ca ON o.id_carrello = ca.id_carrello
                        JOIN utenti AS u ON ca.id_utente = u.id_utente 
                        WHERE LOWER(u.citta) = %s
                        """
                        , [citta_clean]
                        )
    
    return result



app.mount("/", StaticFiles(directory="statics", html=True), name="static")

uvicorn.run(app, host="127.0.0.1", port=8000)
