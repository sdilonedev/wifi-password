import subprocess
import locale

def get_wifi_networks():
    networks = []
    try:
        output = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'networks']).decode(locale.getpreferredencoding())
        lines = output.split('\n')
        for line in lines:
            if 'SSID' in line:
                ssid = line.split(':')[1].strip()
                networks.append(ssid)
    except subprocess.CalledProcessError:
        print("Error al obtener las redes Wi-Fi.")
    return networks


def get_wifi_password(ssid):
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', 'name=' + ssid, 'key=clear']).decode(locale.getpreferredencoding())
        lines = output.split('\n')
        for line in lines:
            if 'Contenido de la clave' in line:  # En español
                password = line.split(':')[1].strip()
                return password
            elif 'Key Content' in line:  # En inglés
                password = line.split(':')[1].strip()
                return password
    except subprocess.CalledProcessError:
        print("Error al obtener la contraseña de la red Wi-Fi.")

# Obtener y mostrar las redes Wi-Fi disponibles
wifi_networks = get_wifi_networks()
print("Redes Wi-Fi disponibles:")
for network in wifi_networks:
    print(network)

# Obtener y mostrar la contraseña de una red específica
network_ssid = input("Ingrese el nombre de la red Wi-Fi: ")
password = get_wifi_password(network_ssid)
if password:
    print("Contraseña de la red {}: {}".format(network_ssid, password))
else:
    print("No se pudo obtener la contraseña de la red {}.".format(network_ssid))