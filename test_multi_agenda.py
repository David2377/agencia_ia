import sys
sys.path.append("..")  # Esto añade la carpeta raíz al path

from bot_calendar_final import add_event, show_agenda


# Eventos de prueba
event1 = {"fecha": "2025-09-11 10:00", "cliente": "Juan", "tipo": "consulta"}
event2 = {"fecha": "2025-09-11 11:00", "cliente": "Ana", "tipo": "nutricion"}

# Agregar eventos para distintos profesionales
add_event(987654321, event1)
add_event(112233445, event2)

# Mostrar agendas
show_agenda(987654321)
show_agenda(112233445)

