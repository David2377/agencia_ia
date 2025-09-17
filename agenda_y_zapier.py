# agenda_y_zapier.py
import json
import os
from random import choice, randint
import sys

# ====== Agregar carpeta scripts al path para importar conexiones.py ======
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from conexiones import enviar_cita_zapier

# ====== Carpeta data ======
data_dir = os.path.join(current_dir, "../data")
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

    cita = {
        "paciente": paciente,
        "hora": hora,
        "tipo": tipo,
        "profesional": profesional,
        "estado": estado,
        "fecha": fecha
    }
    agenda_prueba.append(cita)

# ====== Guardar agenda en agenda.json ======
with open(agenda_file, "w", encoding="utf-8") as f:
    json.dump(agenda_prueba, f, indent=4, ensure_ascii=False)

print(f"Agenda de prueba creada con {len(agenda_prueba)} citas en: {agenda_file}")

# ====== Enviar todas las citas al webhook de Zapier ======
print("\nEnviando citas a Zapier...")
for cita in agenda_prueba:
    status = enviar_cita_zapier(cita)
    if status == 200:
        print(f"Cita de {cita['paciente']} enviada correctamente a Zapier.")
    else:
        print(f"Error al enviar la cita de {cita['paciente']}. Código de respuesta: {status}")

