import logging
import os

# Crear carpeta de logs si no existe
LOG_DIR = "../logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Configurar logging
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "bot_logs.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Funciones de logging
def log_info(message):
    print(message)  # También se muestra en consola
    logging.info(message)

def log_error(message):
    print("ERROR:", message)
    logging.error(message)

