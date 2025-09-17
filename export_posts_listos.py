import pandas as pd
import os

# ---------------------------
# Ruta del CSV exportado desde Streamlit
# ---------------------------
csv_file = os.path.join(os.path.dirname(__file__), "..", "data", "posts.csv")

# Verificar que existe
if not os.path.exists(csv_file):
    print("❌ No se encontró posts.csv. Genera primero los posts desde Streamlit.")
    exit()

# Cargar CSV
df = pd.read_csv(csv_file)

# ---------------------------
# Crear archivo de salida con posts listos
# ---------------------------
output_file = os.path.join(os.path.dirname(__file__), "..", "data", "posts_listos.txt")

with open(output_file, "w", encoding="utf-8") as f:
    for i, row in df.iterrows():
        titulo = row.get("titulo", "")
        copy = row.get("copy", "")
        hashtags = row.get("hashtags", "").strip("[]").replace("'", "")
        imagen = row.get("imagen", "")

        f.write(f"📌 {titulo}\n")
        f.write(f"{copy}\n\n")
        f.write(f"🌱 {hashtags}\n")
        f.write(f"🖼️ Imagen: {imagen}\n")
        f.write("-" * 50 + "\n\n")

print(f"✅ Posts listos guardados en {output_file}")

