"""
scripts/integraciones.py
Simulación de publicación automática de posts en redes sociales.
Actualmente no conecta con APIs reales, solo imprime la acción.
"""

import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "posts.json")

def cargar_posts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def publicar_post(post_id):
    """
    Simula la publicación de un post por ID.
    Cambia el estado a 'publicado' en el JSON.
    """
    posts = cargar_posts()
    for post in posts:
        if post["id"] == post_id:
            post["estado"] = "publicado"
            print(f"✅ Publicado: {post['tema']} - {post['copy']}")
            break
    else:
        print(f"❌ No se encontró post con id {post_id}")
        return
    # Guardar cambios
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)

def publicar_todos():
    """
    Publica todos los posts que están en estado 'borrador'
    """
    posts = cargar_posts()
    for post in posts:
        if post["estado"] == "borrador":
            publicar_post(post["id"])

if __name__ == "__main__":
    print("🔹 Publicando todos los posts en borrador...")
    publicar_todos()
