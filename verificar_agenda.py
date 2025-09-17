# verificar_agenda.py
import os
import json
import re
import requests

# Ruta del archivo agenda.json
ruta_agenda = "../data/agenda.json"

# Webhook real de Zapier (tu URL actualizado)
WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/24470605/umbxjrv/"

# Estados válidos
estados_validos = ["Pendiente", "Completada", "Cancelada"]

# Tipos válidos de cita
tipos_validos = ["Consulta", "Terapia", "Nutrición"]

# Profesionales válidos (ejemplo)
profesionales_validos = ["Dr. Ana", "Dr. Juan", "Dra. María"]

def verificar_agenda():
    if not os.path.exists(ruta_agenda):
        print(f"❌ ERROR: No existe el archivo {ruta_agenda}")
        return

    with open(ruta_agenda, "r", encoding="utf-8") as f:
        try:
            agenda = json.load(f)
        except json.JSONDecodeError:
            print("❌ ERROR: El archivo agenda.json no tiene un formato JSON válido")
            return

    print(f"✅ Archivo encontrado: {ruta_agenda}")
    print(f"📊 Total de citas: {len(agenda)}")

    if len(agenda) < 30:
        print("⚠️ Advertencia: Hay menos de 30 citas en la agenda")

    errores = 0
    for i, cita in enumerate(agenda, start=1):
        for campo in ["paciente", "hora", "tipo", "profesional", "estado", "fecha"]:
            if campo not in cita:
                print(f"❌ ERROR en cita {i}: Falta el campo '{campo}'")
                errores += 1

        if "hora" in cita and not re.match(r"^\d{2}:\d{2}$", cita["hora"]):
            print(f"❌ ERROR en cita {i}: Hora inválida '{cita['hora']}'")
            errores += 1

        if "estado" in cita and cita["estado"] not in estados_validos:
            print(f"❌ ERROR en cita {i}: Estado inválido '{cita['estado']}'")
            errores += 1

        if "tipo" in cita and cita["tipo"] not in tipos_validos:
            print(f"❌ ERROR en cita {i}: Tipo inválido '{cita['tipo']}'")
            errores += 1

        if "profesional" in cita and cita["profesional"] not in profesionales_validos:
            print(f"⚠️ Advertencia en cita {i}: Profesional '{cita['profesional']}' no está en la lista")

    if errores == 0:
        print("🎉 Verificación de agenda completada: Todas las citas son válidas.")
    else:
        print(f"⚠️ Verificación terminada con {errores} errores encontrados.")

    # --- Enviar todas las citas al webhook de Zapier ---
    if agenda:
        print("\n🚀 Enviando TODAS las citas a Zapier...")
        exitos = 0
        fallos = 0
        for cita in agenda:
            try:
                response = requests.post(WEBHOOK_URL, json=cita, timeout=10)
                if response.status_code == 200:
                    print(f"✅ Cita de {cita.get('paciente', 'sin nombre')} enviada correctamente.")
                    exitos += 1
                else:
                    print(f"❌ Error al enviar la cita de {cita.get('paciente', 'sin nombre')}. Código: {response.status_code}")
                    fallos += 1
            except Exception as e:
                print(f"❌ Error al enviar la cita de {cita.get('paciente', 'sin nombre')}: {e}")
                fallos += 1

        print(f"\n📊 Resumen del envío a Zapier: {exitos} exitosas, {fallos} fallidas.")

if __name__ == "__main__":
    verificar_agenda()
