import os
import json

# -------------------------------
# Rutas
# -------------------------------
DATA_JSON = os.path.join(os.path.dirname(__file__), "..", "data", "posts.json")
IMAGES_FOLDER = os.path.join(os.path.dirname(__file__), "..", "assets")  # Carpeta con imágenes reales

# -------------------------------
# Cargar posts
# -------------------------------
with open(DATA_JSON, "r", encoding="utf-8") as f:
    posts = json.load(f)

# -------------------------------
# Reemplazar placeholders con imágenes reales
# -------------------------------
for post in posts:
    # Nombre de archivo de imagen esperado: título en minúsculas + .png, reemplazando espacios por _
    filename = post["titulo"].lower().replace(" ", "_") + ".png"
    filepath = os.path.join(IMAGES_FOLDER, filename)
    
    if os.path.exists(filepath):
        # Si existe la imagen, reemplaza la URL del placeholder
        post["imagen"] = filepath
        print(f"✅ {post['titulo']} actualizado con imagen: {filename}")
    else:
        print(f"⚠️ Imagen no encontrada para: {post['titulo']}, sigue usando placeholder")

# -------------------------------
# Guardar posts actualizados
# -------------------------------
with open(DATA_JSON, "w", encoding="utf-8") as f:
    json.dump(posts, f, indent=4, ensure_ascii=False)

print("🎉 Posts actualizados correctamente.")

