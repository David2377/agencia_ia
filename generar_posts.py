import json
import os
from datetime import date

# Ruta al archivo posts.json
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)
DATA_FILE = os.path.join(DATA_DIR, "posts.json")

# Posts profesionales sobre proceso terapéutico
posts = [
    {
        "titulo": "Mindfulness para reducir el estrés",
        "contenido": "Exploramos cómo la práctica de la atención plena puede ayudarte a vivir en el presente y reducir la ansiedad diaria.",
        "imagen": "https://via.placeholder.com/1080x1080.png?text=Mindfulness",
        "estado": "borrador",
        "tema": "mindfulness",
        "fecha": str(date.today()),
        "copy": "La atención plena nos enseña a observar sin juzgar. Dedicar unos minutos al día a la respiración consciente puede mejorar tu bienestar.",
        "hashtags": ["#mindfulness", "#atencionplena", "#bienestar"]
    },
    {
        "titulo": "Gestión emocional en terapia",
        "contenido": "Descubre estrategias terapéuticas para identificar, aceptar y regular tus emociones en momentos difíciles.",
        "imagen": "https://via.placeholder.com/1080x1080.png?text=Gestion+Emocional",
        "estado": "borrador",
        "tema": "gestión emocional",
        "fecha": str(date.today()),
        "copy": "Identificar nuestras emociones es el primer paso hacia la sanación. La terapia ayuda a transformar la ira, tristeza o miedo en recursos internos.",
        "hashtags": ["#emociones", "#terapia", "#saludmental"]
    },
    {
        "titulo": "El poder del autocuidado",
        "contenido": "Aprende cómo pequeños hábitos de autocuidado fortalecen tu proceso terapéutico y tu bienestar general.",
        "imagen": "https://via.placeholder.com/1080x1080.png?text=Autocuidado",
        "estado": "borrador",
        "tema": "autocuidado",
        "fecha": str(date.today()),
        "copy": "El autocuidado no es un lujo, es una necesidad. Dedicar tiempo a ti mismo mejora tu equilibrio emocional y mental.",
        "hashtags": ["#autocuidado", "#saludmental", "#equilibrio"]
    },
    {
        "titulo": "Construyendo resiliencia",
        "contenido": "La resiliencia es la capacidad de levantarse tras la adversidad. Conoce técnicas para desarrollarla en tu día a día.",
        "imagen": "https://via.placeholder.com/1080x1080.png?text=Resiliencia",
        "estado": "borrador",
        "tema": "resiliencia",
        "fecha": str(date.today()),
        "copy": "Cada dificultad es una oportunidad de crecimiento. La resiliencia nos permite transformar la adversidad en fortaleza.",
        "hashtags": ["#resiliencia", "#fortaleza", "#crecimiento"]
    },
    {
        "titulo": "Terapia cognitiva: cambiando pensamientos",
        "contenido": "Explora cómo la terapia cognitivo-conductual ayuda a identificar pensamientos negativos y reemplazarlos por otros más saludables.",
        "imagen": "https://via.placeholder.com/1080x1080.png?text=Terapia+Cognitiva",
        "estado": "borrador",
        "tema": "terapia cognitiva",
        "fecha": str(date.today()),
        "copy": "Tus pensamientos influyen en cómo te sientes y actúas. La terapia cognitiva ofrece herramientas prácticas para transformarlos.",
        "hashtags": ["#terapia", "#psicologia", "#bienestarmental"]
    },
    {
        "titulo": "Viviendo con menos ansiedad",
        "contenido": "Consejos prácticos para reconocer los síntomas de la ansiedad y enfrentarlos desde un enfoque terapéutico.",
        "imagen": "https://via.placeholder.com/1080x1080.png?text=Ansiedad",
        "estado": "borrador",
        "tema": "ansiedad",
        "fecha": str(date.today()),
        "copy": "Respirar profundo, reconocer tus miedos y buscar apoyo son claves en el manejo de la ansiedad.",
        "hashtags": ["#ansiedad", "#pazmental", "#psicologia"]
    },
    {
        "titulo": "Fortaleciendo la autoestima",
        "contenido": "Técnicas terapéuticas para construir una autoestima sólida y una relación positiva contigo mismo.",
        "imagen": "https://via.placeholder.com/1080x1080.png?text=Autoestima",
        "estado": "borrador",
        "tema": "autoestima",
        "fecha": str(date.today()),
        "copy": "La autoestima no es un destino, es un proceso. Aceptarte y valorarte es parte esencial del crecimiento personal.",
        "hashtags": ["#autoestima", "#amorpropio", "#confianza"]
    },
    {
        "titulo": "Hábitos saludables para el bienestar integral",
        "contenido": "Integra ejercicio, descanso y nutrición consciente como parte de tu proceso terapéutico.",
        "imagen": "https://via.placeholder.com/1080x1080.png?text=Bienestar+Integral",
        "estado": "borrador",
        "tema": "bienestar integral",
        "fecha": str(date.today()),
        "copy": "El bienestar integral combina cuerpo, mente y emociones. Cada hábito positivo suma en tu proceso terapéutico.",
        "hashtags": ["#bienestarintegral", "#habitos", "#vidasana"]
    }
]

# Guardar archivo
with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(posts, f, indent=4, ensure_ascii=False)

print(f"✅ posts.json generado en: {DATA_FILE}")
