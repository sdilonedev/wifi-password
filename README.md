# Herramienta para obtener contraseñas de redes Wi-Fi

![Wi-Fi](https://github.com/nevek-btw/wifi-password/assets/138080914/e0c23f6e-177e-4ca2-ba54-04a5dcec1b56)

Esta herramienta en Python está diseñada para ayudar a obtener las contraseñas de las redes Wi-Fi almacenadas en un sistema Windows. Es ideal para usuarios que necesitan recuperar contraseñas de redes previamente conectadas, siempre y cuando se cuente con permisos de **Administrador**. Asegúrate de que su uso sea responsable y autorizado.

## Características principales:

- **Recuperación de contraseñas**: Permite recuperar la contraseña de cualquier red Wi-Fi previamente conectada en tu sistema Windows, utilizando el comando `netsh`.
- **Listar redes disponibles**: Muestra una lista interactiva de las redes Wi-Fi disponibles, con la opción de seleccionar una para obtener la contraseña correspondiente.

- **Generación de QR**: Genera un código QR con los datos de la red Wi-Fi seleccionada, facilitando la conexión desde dispositivos móviles sin tener que introducir la contraseña manualmente.

## Funciones clave:

- **`get_wifi_password(ssid)`**: Obtiene la contraseña de una red Wi-Fi específica proporcionada su SSID (nombre de la red). Usa el comando `netsh wlan show profile` para recuperar la información de la red y extrae la contraseña si está disponible.

- **`get_wifi_networks()`**: Devuelve una lista de redes Wi-Fi disponibles en el sistema, extraídas de los perfiles almacenados utilizando `netsh wlan show profiles`.

- **`generate_qr(data)`**: Genera un código QR con los datos de la red Wi-Fi (nombre y contraseña). Se puede mostrar en consola o guardar como imagen, facilitando la conexión a otros dispositivos.

- **`interactive_selector(options)`**: Muestra un menú interactivo para seleccionar de manera fácil y rápida la red Wi-Fi de la cual se desea obtener la contraseña.

## Requisitos:

- Python 3.x
- Librerías:
  - `qrcode`: Para generar el código QR.
  - `PyInquirer`: Para crear un menú interactivo.

## Instalación:

1. Clona este repositorio o descarga los archivos:
   ```bash
   git clone https://github.com/sdilonedev/wifi-password.git
   ```
