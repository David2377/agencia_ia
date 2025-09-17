import streamlit as st
import json
from datetime import datetime
from conexiones import enviar_cita_zapier

DATA_PATH = "../data/agenda.json"

def agregar_cita(paciente, tipo, hora, profesional):
    try:
        with open(DATA_PATH, "r") as f:
            agenda = json.load(f)
    except FileNotFoundError:
        agenda = []

    nueva_cita = {
        "paciente": paciente,
        "tipo": tipo,
        "hora": hora,
        "profesional": profesional,
        "estado": "Pendiente",
        "creado": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    agenda.append(nueva_cita)
    with open(DATA_PATH, "w") as f:
        json.dump(agenda, f, indent=4)

    # Enviar automáticamente a Zapier
    return enviar_cita_zapier(nueva_cita)


# =========================
# 📌 PÁGINA CREAR CITA
# =========================
st.set_page_config(page_title="Crear Nueva Cita", layout="centered")
st.title("➕ Crear Nueva Cita")

with st.form("form_cita"):
    paciente = st.text_input("👤 Nombre del paciente")
    tipo = st.selectbox("📌 Tipo de cita", ["Consulta", "Terapia", "Nutrición", "Control"])
    hora = st.text_input("⏰ Fecha y hora (YYYY-MM-DD HH:MM)")
    profesional = st.text_input("👨‍⚕️ Profesional")

    submitted = st.form_submit_button("Crear cita")
    if submitted:
        if paciente and tipo and hora and profesional:
            status = agregar_cita(paciente, tipo, hora, profesional)
            if status == 200:
                st.success(f"✅ Cita creada para {paciente} y enviada a Zapier")
            else:
                st.warning(f"⚠️ Cita creada para {paciente}, pero error al enviar a Zapier")
        else:
            st.error("❌ Completa todos los campos.")

