import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os

# -------------------------------
# Rutas
# -------------------------------
csv_file = os.path.join(os.path.dirname(__file__), "../data/posts.csv")
creds_file = os.path.join(os.path.dirname(__file__), "credentials.json")

# -------------------------------
# Configuración Google API
# -------------------------------
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
client = gspread.authorize(creds)

# -------------------------------
# Abrir hoja existente
# -------------------------------
spreadsheet_name = "Posts Dashboard"

try:
    spreadsheet = client.open(spreadsheet_name)
except gspread.SpreadsheetNotFound:
    raise Exception(
        f"❌ La hoja '{spreadsheet_name}' no existe. Crea la hoja en Google Drive y comparte con la Service Account."
    )

sheet = spreadsheet.sheet1

# -------------------------------
# Leer CSV y subir a Google Sheets
# -------------------------------
df = pd.read_csv(csv_file)

# Limpiar hoja antes de subir
sheet.clear()
sheet.update([df.columns.values.tolist()] + df.values.tolist())

print("✅ CSV subido a Google Drive con éxito")
