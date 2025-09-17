import json
import pandas as pd
import os

# -------------------------------
# 1️⃣ Ruta del archivo JSON
# -------------------------------
json_file_path = "/Users/PUESTOV1/Desktop/AGENCIA_IA/data/posts.json"

# -------------------------------
# 2️⃣ Cargar posts
# -------------------------------
if not os.path.exists(json_file_path):
    print(f"❌ No se encontró posts.json en: {json_file_path}")
    exit()

with open(json_file_path, "r", encoding="utf-8") as f:
    posts = json.load(f)

# -------------------------------
# 3️⃣ Crear DataFrame para CSV
# -------------------------------
data_for_csv = []
for post in posts:
    # Solo posts que no estén publicados
    if post.get("estado", "borrador") == "borrador":
        data_for_csv.append({
            "Caption": post.get("contenido", ""),
            "Image URL": post.get("imagen", ""),
            "Title": post.get("titulo", ""),
            "Theme": post.get("tema", "")
        })

if not data_for_csv:
    print("❌ No hay posts borradores para exportar.")
    exit()

df = pd.DataFrame(data_for_csv)

# -------------------------------
# 4️⃣ Guardar CSV
# -------------------------------
csv_file_path = "/Users/PUESTOV1/Desktop/AGENCIA_IA/data/posts_metabusiness.csv"
df.to_csv(csv_file_path, index=False, encoding="utf-8-sig")

print(f"✅ CSV generado correctamente en: {csv_file_path}")
print("Sube este CSV a Meta Business Suite y solo tendrás que subir las imágenes manualmente.")

