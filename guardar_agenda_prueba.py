# guardar_agenda_prueba.py
import json
from random import choice, randint
import os

# ====== Carpeta data ======
data_dir = os.path.join(os.path.dirname(__file__), "../data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

agenda_file = os.path.join(data_dir, "agenda.json")

# ====== Datos de ejemplo ======
nombres = ["Juan", "Ana", "Carlos", "Lucía", "Pedro", "Marta", "Luis", "Sofía", "Diego", "Elena"]
apellidos = ["Perez", "Lopez", "Ruiz", "Gomez", "Martinez", "Sanchez", "Diaz", "Fernandez", "Morales", "Castro"]
tipos = ["Consulta", "Terapia", "Nutrición"]
profesionales = ["Dr. Ana", "Dr. Juan", "Dra. María"]

agenda_prueba = []

for i in range(30):
    paciente = f"{choice(nombres)} {choice(apellidos)}"
    hora = f"{randint(8,17):02d}:00"  # Horas entre 08:00 y 17:00
    tipo = choice(tipos)
    profesional = choice(profesionales)
    estado = "Pendiente"
    fecha = "2025-09-12"

    agenda_prueba.append({
        "paciente": paciente,
        "hora": hora,
        "tipo": tipo,
        "profesional": profesional,
        "estado": estado,
        "fecha": fecha
    })

# ====== Guardar en agenda.json ======
with open(agenda_file, "w", encoding="utf-8") as f:
    json.dump(agenda_prueba, f, indent=4, ensure_ascii=False)

print(f"Agenda de prueba creada con {len(agenda_prueba)} citas en: {agenda_file}")

