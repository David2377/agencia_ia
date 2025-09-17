"""
scripts/marketing_ia.py
Generador avanzado de posts de texto para la Semana 4 del Proyecto Ultra-Pro IA.
Incluye múltiples plantillas y selección aleatoria de tema.
"""
import random, json, os
from datetime import datetime

# Ruta del archivo JSON donde se guardan los posts
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "posts.json")

# Función para generar hashtags según el tema
def generar_hashtags(tema, n=5):
    base = {
        "salud": ["#salud", "#bienestar", "#vidasana", "#energia", "#habitos"],
        "nutricion": ["#nutricion", "#comidasana", "#colageno", "#vitaminas", "#superfoods"],
        "motivacion": ["#motivacion", "#enfoque", "#constancia", "#logros", "#disciplina"],
        "faq": ["#tips", "#consejos", "#dudas", "#pacientes", "#respuestas"],
    }
    opciones = base.get(tema, ["#IA"])
    k = min(n, len(opciones))
    return random.sample(opciones, k=k)

# Función para generar un post aleatorio según tema
def generar_post(tema="salud"):
    plantillas = {
        "salud": [
            "Recuerda hidratarte: al menos 2 litros de agua al día 💧",
            "Un paseo de 30 min mejora tu salud cardiovascular 🚶‍♀️",
            "Haz ejercicios de estiramiento cada mañana para cuidar tu espalda 🧘‍♂️",
            "Dormir 7–8 horas al día es clave para tu bienestar 😴",
            "Incluye frutas y verduras en cada comida 🍎🥦",
        ],
        "nutricion": [
            "Incluye frutas ricas en antioxidantes 🍇",
            "Los cítricos apoyan tu colágeno 🍊",
            "Evita el exceso de azúcar para mantener energía estable 🍬❌",
            "Agrega semillas y frutos secos a tu dieta diaria 🌰",
            "Bebe agua antes de cada comida para mejorar digestión 💦",
        ],
        "motivacion": [
            "Tu progreso depende de tu constancia 💪",
            "Pequeños hábitos generan grandes resultados ✨",
            "Hoy es un buen día para empezar algo nuevo 🚀",
            "No te compares, enfócate en tu propio camino 🌱",
            "Celebra tus logros, por pequeños que sean 🎉",
        ],
        "faq": [
            "¿Sabías que dormir menos de 6h afecta tu memoria? 🧠",
            "¿El café deshidrata? ☕ Tomado con moderación no lo hace.",
            "¿Es bueno caminar después de comer? Sí, mejora digestión 🚶‍♂️",
            "¿Cuántos pasos al día son recomendables? Al menos 10,000 🏃‍♀️",
            "¿Beber agua ayuda a la concentración? Sí, hidratarse mejora foco 💧",
        ]
    }
    copy = random.choice(plantillas.get(tema, ["Hoy es un gran día para mejorar ✨"]))
    hashtags = generar_hashtags(tema)
    return {
        "id": int(datetime.now().timestamp() * 1000),
        "fecha": str(datetime.now().date()),
        "tema": tema,
        "copy": copy,
        "hashtags": hashtags,
        "estado": "borrador"
    }

# Función para guardar el post en data/posts.json
def guardar_post(post):
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    data.append(post)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return post["id"]

# Ejecución principal: elige un tema aleatorio y genera el post
if __name__ == "__main__":
    tema_elegido = random.choice(["salud","nutricion","motivacion","faq"])
    nuevo = generar_post(tema_elegido)
    guardar_post(nuevo)
    print("✅ Post generado y guardado:", nuevo)
