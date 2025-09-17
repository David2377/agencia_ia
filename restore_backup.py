import os
import shutil

# Rutas base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "eventos.json")
LOG_FILE = os.path.join(BASE_DIR, "logs", "bot_logs.log")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")

def restore_latest(file_suffix, target_file):
    # Buscar backups que terminan en ese archivo
    backups = sorted(
        [f for f in os.listdir(BACKUP_DIR) if f.endswith(file_suffix)],
        reverse=True
    )
    if backups:
        latest = os.path.join(BACKUP_DIR, backups[0])
        shutil.copy(latest, target_file)
        print(f"✅ Restaurado {target_file} desde {latest}")
    else:
        print(f"⚠️ No se encontró backup para {file_suffix}")

if __name__ == "__main__":
    print("Iniciando restauración de backups...")
    restore_latest("eventos.json", DATA_FILE)
    restore_latest("bot_logs.log", LOG_FILE)
    print("Restauración finalizada.")

