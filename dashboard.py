# dashboard.py
import streamlit as st
import pandas as pd
import json
import os
import sys
import plotly.express as px
import random
import time
from datetime import datetime

# --- Ruta para telegram_utils (opcional) ---
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
    from telegram_utils import enviar_alerta_post
    TELEGRAM_OK = True
except ModuleNotFoundError:
    TELEGRAM_OK = False

# ---------------------------
# Helpers
# ---------------------------
def load_logo():
    logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
    return logo_path if os.path.exists(logo_path) else None

def normalize_hashtags_field(h):
    """ Normaliza hashtags a lista sin usar eval """
    if h is None: return []
    if isinstance(h, list): return h
    if isinstance(h, str):
        s = h.strip()
        if s.startswith("[") and s.endswith("]"):
            try:
                return json.loads(s.replace("'", '"'))
            except:
                inner = s[1:-1]
                return [it.strip().strip("'\"") for it in inner.split(",") if it.strip()]
        return [s]
    return []

# ---------------------------
# Configuración general
# ---------------------------
logo_path = load_logo()
st.set_page_config(page_title="Dashboard UltraPro IA", page_icon=logo_path, layout="wide")

# ---------------------------
# Estilos
# ---------------------------
st.markdown("""
<style>
body { background: linear-gradient(160deg, #e0f7fa, #e8f5e9, #f3e5f5); color: #37474f; font-family: 'Lato', sans-serif; }
h1 { font-family: 'Montserrat', sans-serif; font-weight: 700; font-size: 44px; color: #4db6ac; text-shadow: 1px 1px 5px rgba(77,182,172,0.35); margin:0; }
.stButton>button { background: linear-gradient(135deg, #4db6ac, #26a69a); color:white; padding:8px 18px; border-radius:10px; font-weight:600; box-shadow:0 0 8px rgba(77,182,172,0.45); transition: all 0.25s ease; }
.stButton>button:hover { background: linear-gradient(135deg, #26a69a, #00897b); box-shadow:0 0 16px rgba(38,166,154,0.5); }
.filter-card { background: linear-gradient(135deg, #b2dfdb, #c8e6c9); padding:12px; border-radius:12px; box-shadow:2px 2px 10px rgba(0,0,0,0.08); margin-bottom:16px; transition: all 0.25s ease; }
.card { padding:14px; border-radius:12px; margin-bottom:12px; background: linear-gradient(135deg, #ffffff, #e0f2f1); box-shadow: 2px 2px 12px rgba(0,0,0,0.06); transition: all 0.4s ease; color:#37474f; }
.card:hover { transform: translateY(-6px); box-shadow: 8px 8px 30px rgba(0,0,0,0.09); }
.small-muted { color: #607d8b; font-size:13px; }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Cabecera
# ---------------------------
def render_header(logo_path):
    col1, col2 = st.columns([1,6])
    with col1:
        if logo_path:
            st.image(logo_path, width=140)
    with col2:
        st.markdown(f"""
        <div style="padding:18px; border-radius:12px;">
            <h1>Dashboard UltraPro IA</h1>
            <div class="small-muted">Gestión inteligente de posts, previsualización y exportación para Meta Business Suite</div>
        </div>
        """, unsafe_allow_html=True)

render_header(logo_path)

# ---------------------------
# Cargar posts
# ---------------------------
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "posts.json")
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            posts = json.load(f)
    except:
        st.error("❌ Error leyendo posts.json")
        posts = []
else:
    st.warning("❌ No se encontró posts.json")
    posts = []

for p in posts:
    p["hashtags"] = normalize_hashtags_field(p.get("hashtags", []))
    p.setdefault("estado","borrador")
    p.setdefault("fecha","1900-01-01")
    p.setdefault("imagen","")

# ---------------------------
# Simulación de engagement
# ---------------------------
if "eng_init" not in st.session_state:
    for p in posts:
        p.setdefault("likes_sim", random.randint(20,300))
        p.setdefault("comments_sim", random.randint(0,30))
        p.setdefault("shares_sim", random.randint(0,10))
    st.session_state["posts_data"] = posts
    st.session_state["eng_init"] = True
else:
    posts = st.session_state.get("posts_data", posts)

# ---------------------------
# Métricas superiores
# ---------------------------
total_posts = len(posts)
borrador = sum(1 for p in posts if p.get("estado")=="borrador")
publicado = sum(1 for p in posts if p.get("estado")=="publicado")
programado = sum(1 for p in posts if p.get("estado")=="programado")
m1,m2,m3,m4 = st.columns(4)
m1.metric("Total de posts", total_posts)
m2.metric("Borradores", borrador)
m3.metric("Publicados", publicado)
m4.metric("Programados", programado)

# ---------------------------
# Filtros y DataFrame filtrado
# ---------------------------
if posts:
    df_posts = pd.DataFrame(posts)
    df_posts["tema"] = df_posts["tema"].fillna("General")
    temas = sorted(df_posts["tema"].unique().tolist())
    estados = ["borrador","publicado","programado"]

    with st.container():
        st.markdown('<div class="filter-card">', unsafe_allow_html=True)
        f1,f2,f3 = st.columns([2,2,2])
        filtro_tema = f1.selectbox("Filtrar por tema", ["Todos"]+temas)
        filtro_estado = f2.selectbox("Filtrar por estado", ["Todos"]+estados)
        df_posts["fecha"] = pd.to_datetime(df_posts["fecha"], errors="coerce")
        fechas = df_posts["fecha"].dropna()
        if not fechas.empty:
            min_fecha,max_fecha = fechas.min().date(),fechas.max().date()
            fecha_inicio,fecha_fin = f3.date_input("Rango de fechas",[min_fecha,max_fecha])
        else:
            fecha_inicio,fecha_fin = None,None
        st.markdown('</div>', unsafe_allow_html=True)

    df_filtrado = df_posts.copy()
    if filtro_tema!="Todos":
        df_filtrado = df_filtrado[df_filtrado["tema"]==filtro_tema]
    if filtro_estado!="Todos":
        df_filtrado = df_filtrado[df_filtrado["estado"]==filtro_estado]
    if fecha_inicio and fecha_fin:
        df_filtrado = df_filtrado[(df_filtrado["fecha"].dt.date>=fecha_inicio) & (df_filtrado["fecha"].dt.date<=fecha_fin)]

    # Reconstruir engagement
    posts_all = st.session_state.get("posts_data", posts)
    def find_post(row):
        for pp in posts_all:
            if pp.get("titulo")==row.get("titulo") and str(pp.get("fecha"))==str(row.get("fecha")):
                return pp
        return row
    rows=[]
    for _,r in df_filtrado.iterrows():
        matched = find_post(r.to_dict())
        rec = r.to_dict()
        rec["likes_sim"] = matched.get("likes_sim", rec.get("likes_sim",0))
        rec["comments_sim"] = matched.get("comments_sim", rec.get("comments_sim",0))
        rec["shares_sim"] = matched.get("shares_sim", rec.get("shares_sim",0))
        rec["hashtags"] = normalize_hashtags_field(rec.get("hashtags",[]))
        rows.append(rec)
    df_filtrado = pd.DataFrame(rows)
    if not df_filtrado.empty:
        df_filtrado["engagement_total"] = df_filtrado["likes_sim"] + 2*df_filtrado["comments_sim"] + 3*df_filtrado["shares_sim"]
        posts_filtrados = df_filtrado.to_dict("records")
    else:
        posts_filtrados = []
else:
    posts_filtrados = []

# ---------------------------
# Gráficos
# ---------------------------
if posts_filtrados:
    # Hashtags
    df_hashtags = df_filtrado.explode("hashtags")
    if not df_hashtags.empty:
        hashtags_count = df_hashtags.groupby(["tema","hashtags"]).size().reset_index(name="Cantidad")
    else:
        hashtags_count = pd.DataFrame(columns=["tema","hashtags","Cantidad"])
    fig_hashtags = px.bar(hashtags_count,x="hashtags",y="Cantidad",color="tema",title="📌 Conteo de hashtags por tema",height=320,text_auto=True)
    fig_hashtags.update_layout(transition={'duration':450})
    st.plotly_chart(fig_hashtags,use_container_width=True,config={'displayModeBar':False})

    # Estado
    estado_count = df_filtrado["estado"].value_counts().reset_index()
    estado_count.columns = ["Estado","Cantidad"]
    fig_estado = px.pie(estado_count,names="Estado",values="Cantidad",title="📊 Posts por estado",height=320)
    fig_estado.update_layout(transition={'duration':450})
    st.plotly_chart(fig_estado,use_container_width=True,config={'displayModeBar':False})

    # Evolución engagement
    df_fecha = df_filtrado.groupby("fecha")[["engagement_total","likes_sim","comments_sim","shares_sim"]].sum().reset_index()
    fig_eng = px.line(df_fecha,x="fecha",y="engagement_total",markers=True,title="📈 Evolución del engagement",line_shape='spline',hover_data={"likes_sim":True,"comments_sim":True,"shares_sim":True})
    fig_eng.update_layout(transition={'duration':450})
    st.plotly_chart(fig_eng,use_container_width=True,config={'displayModeBar':False})

# ---------------------------
# Previsualización posts
# ---------------------------
tema_colors = {
    "mindfulness": "#81d4fa",
    "terapia": "#b39ddb",
    "bienestar": "#ffcc80",
    "nutrición": "#f48fb1",
    "general": "#90a4ae"
}
tema_iconos = {
    "mindfulness": "🧘‍♂️",
    "terapia": "🛋️",
    "bienestar": "🌿",
    "nutrición": "🥗",
    "general": "📌"
}

if posts_filtrados:
    st.header("📱 Previsualización de posts y engagement (simulado)")
    for sidx, sp in enumerate(st.session_state["posts_data"]):
        if sp.get("estado")=="publicado":
            sp["likes_sim"] += random.randint(0,2)
            sp["comments_sim"] += random.randint(0,1)
            sp["shares_sim"] += random.randint(0,1)

    posts_all = st.session_state["posts_data"]
    for idx,p in enumerate(posts_filtrados):
        tema = str(p.get("tema","general")).lower()
        color = tema_colors.get(tema,"#90a4ae")
        emoji = tema_iconos.get(tema,"📌")
        estado_icono = "✅" if p.get("estado")=="publicado" else "📝"
        matched = next((pp for pp in posts_all if pp.get("titulo")==p.get("titulo") and str(pp.get("fecha"))==str(p.get("fecha"))),p)
        likes = matched.get("likes_sim",0)
        comments = matched.get("comments_sim",0)
        shares = matched.get("shares_sim",0)

        placeholder = st.empty()
        max_count = max(likes,comments,shares,1)
        steps = min(30,max_count)
        for step in range(steps+1):
            display_likes = int(likes*step/steps)
            display_comments = int(comments*step/steps)
            display_shares = int(shares*step/steps)
            placeholder.markdown(f"""
                <div class="card" style="border-left:5px solid {color}">
                    <h4 style="margin-bottom:6px">{estado_icono} {emoji} {tema.capitalize()}</h4>
                    <p style="margin:6px 0 8px 0;">{p.get('copy','')}</p>
                    <p style="margin:6px 0 8px 0;">{" ".join([f"<span style='color:#1976d2'>{h}</span>" for h in p.get('hashtags',[])])}</p>
                    <p style="margin-top:8px; font-weight:600;">❤️ Likes: {display_likes} &nbsp;&nbsp; 💬 Comentarios: {display_comments} &nbsp;&nbsp; 🔄 Shares: {display_shares}</p>
                </div>
            """,unsafe_allow_html=True)
            time.sleep(0.01)

        with st.expander("🔍 Ver detalles"):
            st.write(f"**Copy completo:** {p.get('copy','')}")
            st.write(f"**Hashtags:** {', '.join(p.get('hashtags',[]))}")
            st.write(f"**Estado:** {p.get('estado')}")
            st.write(f"**Fecha:** {p.get('fecha')}")
            st.write(f"**Likes:** {likes}, **Comentarios:** {comments}, **Shares:** {shares}")

# ---------------------------
# Export CSV Meta
# ---------------------------
if posts_filtrados:
    df_meta = pd.DataFrame(posts_filtrados)
    df_meta["Texto de la publicación"] = df_meta.apply(lambda row: f"{row.get('copy','')}\n\n{' '.join(row.get('hashtags',[]))}", axis=1)
    columnas_meta = ["Texto de la publicación","fecha","imagen"]
    df_meta_ready = df_meta[columnas_meta].rename(columns={"fecha":"Fecha programada","imagen":"URL de imagen"})
    csv_meta = df_meta_ready.to_csv(index=False, encoding="utf-8")
    st.download_button("📤 Generar CSV listo para Meta", csv_meta,"posts_meta.csv","text/csv")

# ---------------------------
# Export Google Drive
# ---------------------------
try:
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    if posts_filtrados:
        file_drive = drive.CreateFile({'title':'posts_meta.csv','mimeType':'text/csv'})
        file_drive.SetContentString(csv_meta)
        file_drive.Upload()
        st.success("✅ CSV subido a Google Drive con éxito")
except ModuleNotFoundError:
    st.warning("⚠️ pydrive no está instalado, no se puede exportar a Google Drive")
except Exception as e:
    st.error(f"❌ Error al subir a Google Drive: {str(e)}")

# ---------------------------
# Footer
# ---------------------------
st.markdown("<hr/>",unsafe_allow_html=True)
st.markdown('<div class="small-muted">Dashboard generado localmente — usa "Generar CSV listo para Meta" para descargar y subir a Meta Business Suite (sin API).</div>',unsafe_allow_html=True)
