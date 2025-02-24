# EnvioMensajesWhatsApp
EnvioMensajesWhatsApp
Este proyecto permite enviar mensajes de WhatsApp a múltiples números de teléfono automáticamente, utilizando el servicio de WhatsApp Web a través de un script en Python.

Requisitos
Python 3.6+
Módulos de Python: pywhatkit, json
Instalación
1. Clonar el repositorio
Primero, clona este repositorio en tu máquina:

bash
Copiar
Editar
git clone https://github.com/TU-USER/EnvioMensajesWhatsApp.git
2. Instalar dependencias
Dentro del directorio del proyecto, instala las dependencias necesarias usando pip:

bash
Copiar
Editar
cd EnvioMensajesWhatsApp
pip install pywhatkit
Archivos requeridos
El script requiere un archivo mensajes.json donde deberás ingresar los números de teléfono y los mensajes que quieres enviar.

Ejemplo de archivo mensajes.json:
json
Copiar
Editar
[
    {"numero": "34613715884", "mensaje": "Hola, ¿cómo estás?"},
    {"numero": "34613732489", "mensaje": "Recuerda nuestra reunión mañana."},
    {"numero": "573203171563", "mensaje": "Este es un mensaje automatizado."}
]
Formato de los números: Los números deben tener el código de país sin el signo + ni ceros iniciales. Ejemplo para España: 34613715884.
Uso
1. Abre WhatsApp Web
El script abrirá WhatsApp Web automáticamente en tu navegador. Asegúrate de haber iniciado sesión en WhatsApp Web antes de ejecutar el script y escaneado el código QR con tu teléfono.

2. Ejecuta el script
Ejecuta el script con el siguiente comando:

bash
Copiar
Editar
python whatsapp.py
El script enviará los mensajes automáticamente a los números especificados en el archivo mensajes.json. La ventana de WhatsApp Web se abrirá y enviará cada mensaje a su respectivo número.

Importante: Si WhatsApp Web no ha cargado correctamente, puedes aumentar el tiempo de espera en el script ajustando el parámetro wait_time y los tiempos de sleep.

3. Personalización
Número de teléfono: Asegúrate de que los números en el archivo mensajes.json estén en el formato correcto.
Mensajes: Personaliza el mensaje que deseas enviar modificando el valor en el campo "mensaje" en el archivo mensajes.json.
Solución de problemas
Error: Country Code Missing in Phone Number!
Este error puede ocurrir si los números de teléfono no están en el formato correcto. Asegúrate de que el número esté escrito como el código de país seguido del número de teléfono (sin el signo + ni ceros iniciales).

Ejemplo correcto para España: 34613715884
Ejemplo correcto para Colombia: 573203171563

Error: Error al enviar
Esto puede ser causado por una falta de conexión de WhatsApp Web o problemas de tiempo de espera. Asegúrate de que WhatsApp Web esté cargado correctamente y ajusta los tiempos de espera en el script.

Contribuciones
Si deseas contribuir al proyecto, por favor sigue estos pasos:

Haz un fork del proyecto.
Crea una nueva rama (git checkout -b feature-XYZ).
Realiza tus cambios y haz commit (git commit -am 'Add new feature').
Haz push de tus cambios a tu rama (git push origin feature-XYZ).
Abre un pull request.
Licencia
Este proyecto está licenciado bajo la MIT License.
