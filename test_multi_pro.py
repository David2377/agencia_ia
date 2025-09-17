import sys
import os

# Agregar la carpeta raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot_calendar_final import add_event, show_agenda
from utils import log_info
import backup

# Definir profesionales de prueba
profesionales = [
    {"id": 987654321, "nombre": "Profesional 1"},
    {"id": 112233445, "nombre": "Profesional 2"},
    {"id": 555666777, "nombre": "Asistente"}
]

# Definir eventos de prueba
eventos = [
    {"fecha": "2025-09-12 09:00", "cliente": "Juan", "tipo": "consulta"},
    {"fecha": "2025-09-12 10:00", "cliente": "Ana", "tipo": "nutricion"},
    {"fecha": "2025-09-12 11:00", "cliente": "Luis", "tipo": "psicologia"}
]

# Agregar eventos a cada profesional
for prof, evento in zip(profesionales, eventos):
    add_event(prof["id"], evento)

# Mostrar agendas de todos
for prof in profesionales:
    show_agenda(prof["id"])

# Hacer backup al final
log_info("Ejecutando backup de datos y logs...")
backup.backup_file("../data/eventos.json", "../backups")
backup.backup_file("../logs/bot_logs.log", "../backups")
log_info("Test multi-profesional finalizado ✅")
