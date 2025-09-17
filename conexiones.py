# conexiones.py
import requests
import json
import os

def enviar_cita_zapier(cita):
    """
    Envía los datos de una cita a un webhook de Zapier.

    Parámetro:
        cita: dict con los datos de la cita
            Ejemplo:
            {
                "paciente": "Juan Perez",
                "hora": "09:00",
                "tipo": "Consulta",
                "profesional": "Dr. Ana",
                "estado": "Pendiente",
                "fecha": "2025-09-12"
            }

    Retorna:
        status_code de la respuesta HTTP o None si hay error
    """
    webhook_url = "https://hooks.zapier.com/hooks/catch/24470605/umbxjrv/"
    try:
        response = requests.post(webhook_url, json=cita)
        return response.status_code
    except Exception as e:
        print("Error al enviar la cita a Zapier:", e)
        return None

def enviar_todas_citas():
    """
    Envía todas las citas del archivo agenda.json al webhook de prueba.
    Útil para probar la integración completa.
    """
    data_file = os.path.join(os.path.dirname(__file__), "../data/agenda.json")
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            agenda = json.load(f)
        for cita in agenda:
            status = enviar_cita_zapier(cita)
            print(f"Cita {cita.get('paciente', 'sin nombre')} enviada con status: {status}")
    except Exception as e:
        print("Error al cargar o enviar las citas:", e)
