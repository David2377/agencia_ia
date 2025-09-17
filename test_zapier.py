# test_zapier.py
import sys
import os
from random import choice, randint
import json

# ====== Agregar carpeta scripts al path para importar conexiones.py ======
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from conexiones import enviar_cita_zapier

# ====== Generar 30 citas de prueba ======
nombres = ["Juan", "Ana", "Carlos", "Lucía", "Pedro", "Marta", "Luis", "Sofía", "Diego", "Elena"]
apellidos = ["Perez", "Lopez", "Ruiz", "Gomez", "Martinez", "Sanchez", "Diaz", "Fernandez", "Morales", "Castro"]
tipos = ["Consulta", "Terapia", "Nutrición"]
profesionales = ["Dr. Ana", "Dr. Juan", "Dra. María"]

citas_prueba = []

for i in range(30):
    paciente = f"{choice(nombres)} {choice(apellidos)}"
    hora = f"{randint(8,17):02d}:00"  # Horas entre 08:00 y 17:00
    tipo = choice(tipos)
    profesional = choice(profesionales)
    estado = "Pendiente"
    fecha = "2025-09-12"

    citas_prueba.append({
        "paciente": paciente,
        "hora": hora,
        "tipo": tipo,
        "profesional": profesional,
        "estado": estado,
        "fecha": fecha
    })

# ====== Enviar todas las citas al webhook de Zapier ======
for cita in citas_prueba:
    status = enviar_cita_zapier(cita)
    if status == 200:
        print(f"Cita de {cita['paciente']} enviada correctamente a Zapier.")
    else:
        print(f"Error al enviar la cita de {cita['paciente']}. Código de respuesta: {status}")
