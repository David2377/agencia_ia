import sys
import os
import streamlit as st
import json
from datetime import datetime

# 🔹 Agregar la carpeta raíz al path para encontrar bot_calendar_final.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot_calendar_final import get_user_role

# 🔹 Cargar eventos con manejo de error si no existe
try:
    with open("../data/eventos.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    st.warning("⚠️ No se encontró eventos.json. Se cargará una agenda vacía.")
    data = {"profesionales": {}}

# 🔹 Simular que el médico está logueado
USER_ID = 987654321
role = get_user_role(USER_ID)
agenda = data["profesionales"].get(str(USER_ID), [])

st.set_page_config(page_title=f"Dashboard Médico - {role}", layout="wide")
st.title(f"Dashboard Médico - {role}")

# 🔹 Filtro por fecha
fecha_seleccionada = st.date_input("Selecciona la fecha", datetime.today())
agenda_filtrada = [e for e in agenda if e["fecha"].startswith(str(fecha_seleccionada))]

# 🔹 Mostrar agenda con colores según tipo y estado
st.subheader("Agenda del día")
for idx, e in enumerate(agenda_filtrada):
    tipo = e['tipo']
    if tipo.lower() == "consulta":
        color = "lightblue"
    elif tipo.lower() == "nutricion":
        color = "lightgreen"
    elif tipo.lower() == "psicologia":
        color = "lightpink"
    else:
        color = "lightgray"
    
    estado = e.get("estado", "pendiente")  # pendiente por defecto
    st.markdown(
        f"<div style='background-color:{color}; padding:10px; border-radius:5px;'>"
        f"<b>{e['fecha'].split()[1]}</b> | {e['cliente']} | {tipo.capitalize()} | Estado: {estado.capitalize()}</div>",
        unsafe_allow_html=True
    )

# 🔹 Resumen por paciente con key único para evitar errores de Streamlit
st.subheader("Resumen por paciente")
for idx, e in enumerate(agenda_filtrada):
    if st.button(f"Ver resumen: {e['cliente']}", key=f"{e['cliente']}_{idx}"):
        st.write(f"Resumen de {e['cliente']}: … (IA)")

# 🔹 Indicadores rápidos
st.subheader("Indicadores")
st.write(f"Total citas hoy: {len(agenda_filtrada)}")
completadas = len([e for e in agenda_filtrada if e.get("estado") == "completada"])
pendientes = len([e for e in agenda_filtrada if e.get("estado") != "completada"])
st.write(f"Citas completadas: {completadas}")
st.write(f"Citas pendientes: {pendientes}")
