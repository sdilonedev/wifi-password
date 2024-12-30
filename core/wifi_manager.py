import subprocess
import locale

def get_networks():
    networks = set()
    try:
        output = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'networks'],
            stderr=subprocess.STDOUT,
            text=True,
            encoding=locale.getpreferredencoding()
        )
        lines = output.split('\n')
        for line in lines:
            if 'SSID' in line:
                ssid = line.split(':')[1].strip()
                networks.add(ssid)
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
