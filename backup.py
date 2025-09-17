import os
import shutil
from datetime import datetime

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "eventos.json")
LOG_FILE = os.path.join(BASE_DIR, "logs", "bot_logs.log")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")

# Crear carpeta backups si no existe
os.makedirs(BACKUP_DIR, exist_ok=True)

def backup_file(file_path, backup_dir):
    if os.path.exists(file_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.basename(file_path)
        backup_path = os.path.join(backup_dir, f"{timestamp}_{filename}")
        shutil.copy(file_path, backup_path)
        print(f"✅ Backup creado: {backup_path}")
    else:
        print(f"⚠️ Archivo no encontrado: {file_path}")

if __name__ == "__main__":
    print("Iniciando backup...")
    backup_file(DATA_FILE, BACKUP_DIR)
    backup_file(LOG_FILE, BACKUP_DIR)
    print("Backup finalizado.")

