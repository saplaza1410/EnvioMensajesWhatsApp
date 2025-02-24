import pywhatkit as kit
import json
import time

def limpiar_numero(numero):
    """ Asegura que el número tenga el formato correcto con '+' """
    numero = numero.lstrip("0")  # Elimina ceros al inicio
    return f"+{numero}"  # Añade el '+' al número

# Cargar los mensajes desde el archivo JSON
with open("mensajes.json", "r", encoding="utf-8") as file:
    mensajes = json.load(file)

# Enviar mensajes a cada número
for msg in mensajes:
    numero = limpiar_numero(msg["numero"])  # Limpia y ajusta el número
    mensaje = msg["mensaje"]

    print(f"Enviando mensaje a {numero}: {mensaje}")
    try:
        kit.sendwhatmsg_instantly(numero, mensaje, wait_time=20)  # Aumenta el tiempo de espera (20 segundos)
        time.sleep(15)  # Aumenta el tiempo de espera entre los mensajes para dar más tiempo a WhatsApp
    except Exception as e:
        print(f"Error al enviar a {numero}: {e}")

print("✅ Todos los mensajes han sido enviados.")
