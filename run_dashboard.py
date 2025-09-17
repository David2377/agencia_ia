#!/bin/bash

# Inicia Streamlit en segundo plano
streamlit run dashboard.py --server.port 8501 &

# Guarda el PID para poder matarlo luego si quieres
STREAMLIT_PID=$!

# Espera unos segundos para que arranque Streamlit
sleep 5

# Lanza ngrok y obtiene la URL pública
ngrok http 8501 > ngrok.log &

# Espera a que ngrok arranque
sleep 5

# Extrae la URL de ngrok del log
URL=$(grep -o "https://[0-9a-z]*\.ngrok-free\.app" ngrok.log | head -n1)

echo "✅ Tu dashboard está disponible en:"
echo "$URL"

# Mantener script vivo hasta que pares con CTRL+C
wait $STREAMLIT_PID
