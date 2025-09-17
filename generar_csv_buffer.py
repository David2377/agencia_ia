import json
import pandas as pd
import os

# --- Rutas ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # AGENCIA_IA
JSON_PATH = os.path.join(BASE_DIR, "data", "posts.json")
CSV_PATH = os.path.join(BASE_DIR, "data", "posts_buffer.csv")

# --- Cargar posts ---
try:
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        posts = json.load(f)
except Exception as e:
    print(f"❌ Error leyendo posts.json: {e}")
    posts = []

if not posts:
    print("❌ No hay posts en posts.json")
    exit()

# --- Crear DataFrame para Buffer ---
data = []
for post in posts:
    texto = f"{post.get('titulo','')} - {post.get('contenido','')}"
    imagen = post.get('imagen','')
    data.append({
        "Texto": texto,
        "Imagen": imagen
    })

df = pd.DataFrame(data)

# --- Guardar CSV ---
df.to_csv(CSV_PATH, index=False, encoding="utf-8")
print(f"✅ CSV generado correctamente en: {CSV_PATH}")
print(df.head())

