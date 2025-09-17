# panel_medico.py
import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px
import requests
from datetime import datetime
st.set_page_config(
    page_title="PANEL ProIA - Proceso terapéutico",
    layout="wide",  # Esto hace que la página use todo el ancho
    initial_sidebar_state="auto"
)
st.markdown(
    """
    <style>
    /* Ocultar botón "Desplegar" / barra superior */
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Rutas de archivos
# -----------------------------
LOGO_PATH = os.path.join(os.path.dirname(__file__), "../assets/logo.png")
DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/agenda.json")
ZAPIER_WEBHOOK = "https://hooks.zapier.com/hooks/catch/24470605/umbxjrv/"

# -----------------------------
# CSS personalizado
# -----------------------------
st.markdown(
    """
    <style>
        /* Fondo de toda la página */
        body, .block-container, .main, .stApp {
            background-color: #DFFFE0;  /* Verde minfunde */
        }

        /* Quitar margen superior para que el logo esté arriba */
        .block-container {
            padding-top: 0rem;
        }

        /* Títulos centrados */
        h1, h2, h3 {
            text-align: center;
            color: #1a1a1a;  /* Gris oscuro */
        }

        /* Tarjetas y tablas rosas */
        .stDataFrame, .stMarkdown {
            background-color: #FFDDEE;  /* Rosa minfunde */
            border-radius: 10px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Mostrar logo al inicio
# -----------------------------
if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=150)
else:
    st.warning("⚠️ Logo no encontrado en 'assets/logo.png'.")

# -----------------------------
# Título principal y subtítulos
# -----------------------------

st.markdown(
    "<h1 style='text-align: center; color: #1E3A8A; font-size: 70px;'>🧘‍♂️ Panel ProIA - Proceso terapéutico</h1>",
    unsafe_allow_html=True
)


st.markdown(
    "<h3 style='text-align: center; color: #1E3A8A; font-size: 50px;'>💻 Gestión profesional de pacientes y citas 📋</h3>",
    unsafe_allow_html=True
)


st.markdown(
    "<h3 style='text-align: center; color: #1E3A8A; font-size: 38px;'>🗓️  Citas bajo control</h3>",
    unsafe_allow_html=True
)


st.markdown(
    "<h3 style='text-align: center; color: #1E3A8A; font-size: 38px;'>📈 Progreso visible</h3>",
    unsafe_allow_html=True
)

# -----------------------------
# Función para cargar agenda
# -----------------------------
def cargar_agenda():
    try:
        with open(DATA_PATH, "r") as f:
            agenda = json.load(f)
        return pd.DataFrame(agenda)
    except FileNotFoundError:
        return pd.DataFrame()

# Cargar agenda
df_agenda = cargar_agenda()
if df_agenda.empty:
    st.info("No se encontró agenda.json. La agenda está vacía.")

st.markdown(
    """
    <style>
    /* Fondo de toda la página */
    body, .block-container, .main, .stApp {
        background-color: #DCEEFB;  /* azul relajante */
    }

    /* Títulos centrados */
    h1, h2, h3 {
        text-align: center;
        color: #333333;  /* Color gris para los títulos */
    }

    /* Tarjetas y tablas rosas */
    .stDataFrame, .stMarkdown {
        background-color: #E6D0FA;  /* violeta minfunde claro */
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

 

# -----------------------------
# Resto de tu código
# -----------------------------


# -----------------------------
# Rutas de archivos
# -----------------------------
DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/agenda.json")
LOGO_PATH = os.path.join(os.path.dirname(__file__), "../assets/logo.png")
ZAPIER_WEBHOOK = "https://hooks.zapier.com/hooks/catch/24470605/umbxjrv/"

from datetime import datetime


# -----------------------------
# Página principal
# -----------------------------
# Logo
# -----------------------------


if "mostrar_agenda" not in st.session_state:
    st.session_state["mostrar_agenda"] = False  # <- nota los corchetes

if "mostrar_tarjetas" not in st.session_state:
    st.session_state["mostrar_tarjetas"] = False
    
# -----------------------------
# Estilos de colores y fondo
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FAFAFA;  /* fondo muy claro */
        color: #111827;             /* texto principal */
    }
    .stButton>button {
        background-color: #FFDDEE;  /* azul muy suave */
        color: #1E3A8A;             /* texto azul oscuro */
    }
    .stSelectbox>div>div>div {
        background-color: #FFDDEE;  /* dropdown gris muy claro */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Funciones
# -----------------------------
def cargar_agenda():
    try:
        with open(DATA_PATH, "r") as f:
            agenda = json.load(f)
        return pd.DataFrame(agenda)
    except FileNotFoundError:
        return pd.DataFrame()


# -----------------------------
# Cargar agenda
# -----------------------------
df_agenda = cargar_agenda()
if df_agenda.empty:
    st.info("No se encontró agenda.json. La agenda está vacía.")

# Botones superiores

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📅 Agenda Completa"):
        st.session_state["agenda_view"] = "completa"
with col2:
    if st.button("📆 Agenda Diaria"):
        st.session_state["agenda_view"] = "diaria"
with col3:
    if st.button("🗓️ Agenda Semanal"):
        st.session_state["agenda_view"] = "semanal"
col1, col2, col3 = st.columns([2,1,1])

with col1:
    if st.button("➕ Crear nueva cita"):
        st.session_state.mostrar_formulario = not st.session_state.mostrar_formulario

with col2:
    st.markdown(
        """
        <a href="https://wa.me/34123456789" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35">
        </a>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <a href="https://t.me/usuario" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="35">
        </a>
        """,
        unsafe_allow_html=True
    )



# -----------------------------
# Funciones
# -----------------------------
def cargar_agenda():
    try:
        with open(DATA_PATH, "r") as f:
            agenda = json.load(f)
        return pd.DataFrame(agenda)
    except FileNotFoundError:
        return pd.DataFrame()

def agregar_cita(paciente, tipo, fecha, hora, profesional):
    df = cargar_agenda()
    fecha_hora = f"{fecha} {hora}"
    nueva = {
        "paciente": paciente,
        "tipo": tipo,
        "hora": fecha_hora,
        "profesional": profesional,
        "estado": "Pendiente"
    }
    df = pd.concat([df, pd.DataFrame([nueva])], ignore_index=True)
    df.to_json(DATA_PATH, orient="records", indent=4)
    return df

def enviar_citas_zapier(agenda_filtrada):
    resultados = []
    for _, row in agenda_filtrada.iterrows():
        try:
            r = requests.post(ZAPIER_WEBHOOK, json=row.to_dict())
            if r.status_code == 200:
                resultados.append(f"✅ {row['paciente']}")
            else:
                resultados.append(f"❌ {row['paciente']} (Código: {r.status_code})")
        except Exception as e:
            resultados.append(f"❌ {row['paciente']} (Error: {e})")
    return resultados

def tarjeta_paciente(paciente, tipo, estado):
    st.markdown(f"**{paciente}**")
    st.markdown(f"Tipo: {tipo}")
    st.markdown(f"Estado: {estado}")
    st.markdown("---")


# ----------------------------- 
# Filtros dentro de la página
# -----------------------------
st.markdown("### Filtros")

col1, col2, col3, col4, col5 = st.columns([2,2,2,2,3])

with col1:
    tipo = st.selectbox(
        "📌 Tipo de cita", 
        ["Todos"] + df_agenda["tipo"].dropna().unique().tolist() if not df_agenda.empty else ["Todos"], 
        key="tipo_btn"
    )

with col2:
    estado = st.selectbox(
        "🟢 Estado general", 
        ["Todos"] + df_agenda["estado"].dropna().unique().tolist() if not df_agenda.empty else ["Todos"], 
        key="estado_btn"
    )

with col3:
    horas = ["Todas"] + sorted(df_agenda["hora"].dropna().apply(lambda x: x.split(" ")[1]).unique().tolist()) if not df_agenda.empty else ["Todas"]
    hora = st.selectbox("⏰ Hora de cita", horas, key="hora_btn")

with col4:
    profesionales = ["Todos"] + df_agenda["profesional"].dropna().unique().tolist() if not df_agenda.empty else ["Todos"]
    profesional = st.selectbox("👩‍⚕️ Profesional", profesionales, key="profesional_btn")

with col5:
    buscar = st.text_input("🔍 Buscar paciente", key="buscar_btn")


# Filtrar
agenda_filtrada = df_agenda.copy()
agenda_filtrada["estado_emoji"] = agenda_filtrada["estado"].apply(
    lambda x: "✅ Completada" if x == "Completada" else "⏳ Pendiente"
)


if not df_agenda.empty:
    if tipo != "Todos":
        agenda_filtrada = agenda_filtrada[agenda_filtrada["tipo"] == tipo]
    if estado != "Todos":
        agenda_filtrada = agenda_filtrada[agenda_filtrada["estado"] == estado]
    if hora != "Todas":
        agenda_filtrada = agenda_filtrada[agenda_filtrada["hora"].str.contains(hora)]
    if profesional != "Todos":
        agenda_filtrada = agenda_filtrada[agenda_filtrada["profesional"] == profesional]
    if buscar:
        agenda_filtrada = agenda_filtrada[agenda_filtrada["paciente"].str.contains(buscar, case=False)]

# -----------------------------
# Botón Historial de Pacientes
# -----------------------------
if "mostrar_historial" not in st.session_state:
    st.session_state.mostrar_historial = False

if st.button("📜 Historial de Pacientes"):
    st.session_state.mostrar_historial = not st.session_state.mostrar_historial


if st.session_state.mostrar_historial and not agenda_filtrada.empty:
    st.markdown("### Historial de Pacientes")
    for _, row in agenda_filtrada.iterrows():
        paciente = row["paciente"]
        with st.expander(paciente):
            # Aquí podrías iterar sobre varias consultas si tuvieras historial real
            st.markdown(f"**Fecha de consulta:** {row['hora']}")
            st.markdown(f"**Evolución:** {row.get('evolucion', 'No registrada')}")


# -----------------------------
st.markdown("### Agenda filtrada")

if st.button("🔍 Agenda Filtrada"):
    st.session_state.mostrar_agenda = not st.session_state.mostrar_agenda
if st.session_state.mostrar_agenda:
    if not agenda_filtrada.empty:
        st.dataframe(agenda_filtrada)
    else:
        st.info("No hay citas para mostrar con los filtros aplicados.")



# -----------------------------
# Botón enviar a Zapier
# -----------------------------
if st.button("🚀 Enviar citas filtradas"):
    resultados = enviar_citas_zapier(agenda_filtrada)
    st.write("Resultados del envío:")
    for r in resultados:
        st.write(r)

# -----------------------------
# Tarjetas opcionales por paciente
# ----------------------------
# -----------------------------
# Botón para mostrar/ocultar tarjetas
# -----------------------------
if st.button("🏷️ Tarjetas de Pacientes"):
    st.session_state.mostrar_tarjetas = not st.session_state.mostrar_tarjetas

# -----------------------------
# Tarjetas opcionales por paciente
# -----------------------------
if st.session_state.mostrar_tarjetas and not agenda_filtrada.empty:
    st.markdown("### Tarjetas de pacientes")
    for _, row in agenda_filtrada.iterrows():
        tarjeta_paciente(row["paciente"], row["tipo"], row["estado"])

if st.session_state.mostrar_tarjetas:
    st.markdown("### Tarjetas de pacientes")
    for _, row in agenda_filtrada.iterrows():
        st.markdown(f"**{row['paciente']}**")
        st.markdown(f"Tipo: {row['tipo']}")
        st.markdown(f"Estado: {row['estado']}")
        st.markdown("---")

# -----------------------------
# Métricas
# -----------------------------
st.markdown("### 📊 Métricas principales")
total_citas = len(agenda_filtrada)
completadas = len(agenda_filtrada[agenda_filtrada["estado"]=="Completada"]) if "estado" in agenda_filtrada.columns else 0
pendientes = len(agenda_filtrada[agenda_filtrada["estado"]=="Pendiente"]) if "estado" in agenda_filtrada.columns else 0
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de citas", total_citas)

with col2:
    st.metric("Citas completadas", completadas)

with col3:
    st.metric("Citas pendientes", pendientes)

# -----------------------------
import numpy as np

st.markdown("### 📈 Gráficos")

if not df_agenda.empty:
    col1, col2, col3 = st.columns(3)

    # Crear rango de horas de ejemplo
    horas = sorted(df_agenda['hora'].dropna().apply(lambda x: x.split(' ')[1]).unique().tolist())
    if not horas:
        horas = [f"{h:02d}:00" for h in range(9, 18)]  # Horas de 9 a 17

    # Gráfico 1: Citas por tipo
    with col1:
        tipos = df_agenda['tipo'].dropna().unique().tolist()
        if not tipos:
            tipos = ["Consulta", "Terapia", "Control"]
        data_tipo = []
        for t in tipos:
            cantidades = np.random.randint(0, 5, size=len(horas))
            for h, c in zip(horas, cantidades):
                data_tipo.append({"hora": h, "tipo": t, "cantidad": c})
        df_tipo = pd.DataFrame(data_tipo)
        fig_tipo = px.line(
            df_tipo,
            x="hora",
            y="cantidad",
            color="tipo",
            markers=True,
            title="Citas por tipo",
            color_discrete_sequence=["#4DA8DA", "#D0F0C0", "#E6D0FA"]
        )
        fig_tipo.update_layout(height=300)
        st.plotly_chart(fig_tipo, use_container_width=True)

    # Gráfico 2: Citas por estado
    with col2:
        estados = df_agenda['estado'].dropna().unique().tolist()
        if not estados:
            estados = ["Pendiente", "Completada"]
        data_estado = []
        for e in estados:
            cantidades = np.random.randint(0, 5, size=len(horas))
            for h, c in zip(horas, cantidades):
                data_estado.append({"hora": h, "estado": e, "cantidad": c})
        df_estado = pd.DataFrame(data_estado)
        fig_estado = px.line(
            df_estado,
            x="hora",
            y="cantidad",
            color="estado",
            markers=True,
            title="Citas por estado",
            color_discrete_sequence=["#77DD77", "#FF6961"]
        )
        fig_estado.update_layout(height=300)
        st.plotly_chart(fig_estado, use_container_width=True)

    # Gráfico 3: Total de citas
    with col3:
        total_citas = np.random.randint(0, 10, size=len(horas))
        df_total = pd.DataFrame({"hora": horas, "cantidad": total_citas})
        fig_total = px.line(
            df_total,
            x="hora",
            y="cantidad",
            markers=True,
            title="Total de citas por hora",
            color_discrete_sequence=["#F3C6F1"]
        )
        fig_total.update_layout(height=300)
        st.plotly_chart(fig_total, use_container_width=True)

# -----------------------------
# Tabla scrollable
# -----------------------------


