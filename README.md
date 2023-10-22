## Documentación: Obtener contraseñas de redes Wi-Fi

![Snap](https://github.com/nevek-btw/wifi-password/assets/138080914/e0c23f6e-177e-4ca2-ba54-04a5dcec1b56)

Este script en Python permite obtener las contraseñas de las redes Wi-Fi almacenadas en un sistema Windows. De una manera fácil y segura, siempre teniendo en cuenta que estás son funciones de **Administrador**. Tener en cuenta quien hará su uso.

## Funciones:

- **get_wifi_password(ssid)**: Esta función recibe el SSID (nombre de la red Wi-Fi) como argumento y devuelve la contraseña correspondiente. Utiliza el comando netsh wlan show profile para obtener información sobre la red Wi-Fi y extrae la contraseña de la salida del comando.

- **get_wifi_networks():** Esta función obtiene la lista de redes Wi-Fi disponibles en el sistema. Utiliza el comando netsh wlan show profiles para obtener la información de los perfiles de redes Wi-Fi y devuelve una lista con los nombres de las redes.

## Uso:

- Ejecuta el script en Python.

- Se mostrará una lista de redes Wi-Fi disponibles.

- Ingresa el nombre de la red Wi-Fi de la que deseas obtener la contraseña.

- Si la contraseña se encuentra disponible, se mostrará en pantalla.

- Si no se puede obtener la contraseña, se mostrará un mensaje indicando que no fue posible obtenerla.

## Licencia

MIT
