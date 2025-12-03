from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel
from typing import List
from components import ui

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

class Flight(BaseModel):
    codice: int
    compagnia: str
    durataMinuti: int

@app.get("/flights", response_model=List[Flight])
def get_flights():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT codice, comp, durataMinuti FROM Volo")
    flights = cursor.fetchall()
    conn.close()
    return [Flight(codice=row["codice"], compagnia=row["comp"], durataMinuti=row["durataMinuti"]) for row in flights]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
