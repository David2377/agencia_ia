#!/bin/bash
# Ejecutar Streamlit en segundo plano
streamlit run dashboard.py &

# Guardar el PID de Streamlit para poder matarlo después si queremos
STREAMLIT_PID=$!

# Esperar 5 segundos para que Streamlit arranque
sleep 5

# Ejecutar ngrok en la misma terminal
ngrok http 8501

# Cuando cierres ngrok, detener también Streamlit
kill $STREAMLIT_PID
