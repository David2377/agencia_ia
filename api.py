# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API Clientes y Agenda")

# ================================
# MODELOS DE DATOS
# ================================
class Cliente(BaseModel):
    id: int
    nombre: str
    email: str

class Reserva(BaseModel):
    id: int
    cliente_id: int
    fecha: str
    hora: str
    descripcion: str

# ================================
# BASE DE DATOS EN MEMORIA
# ================================
clientes_db: List[Cliente] = []
agenda_db: List[Reserva] = []

# ================================
# ENDPOINTS CLIENTES
# ================================
@app.get("/clientes", response_model=List[Cliente])
def obtener_clientes():
    return clientes_db

@app.post("/clientes", response_model=Cliente)
def crear_cliente(cliente: Cliente):
    # Evitar IDs duplicados
    for c in clientes_db:
        if c.id == cliente.id:
            raise HTTPException(status_code=400, detail="Cliente ya existe")
    clientes_db.append(cliente)
    return cliente

# ================================
# ENDPOINTS AGENDA
# ================================
@app.get("/agenda", response_model=List[Reserva])
def obtener_agenda():
    return agenda_db

@app.post("/reserva", response_model=Reserva)
def crear_reserva(reserva: Reserva):
    # Verificar cliente existente
    if not any(c.id == reserva.cliente_id for c in clientes_db):
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    agenda_db.append(reserva)
    return reserva

