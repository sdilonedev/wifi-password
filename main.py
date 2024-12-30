import argparse
from core.wifi_manager import get_networks, get_wifi_password
from core.qr_generator import generate_qr
from core.utils import interactive_selector


def list_networks():
    """Función para listar redes disponibles."""
    networks = get_networks()
    if not networks:
        print("No hay redes disponibles.")
    else:
        print("Redes disponibles:")
        for net in networks:
            print(f"- {net}")


def get_password_for_network(network_name):
    """Función para obtener la contraseña de una red Wi-Fi."""
    password = get_wifi_password(network_name)
    if password:
        print(f"Clave de {network_name}: {password}")
    else:
        print(f"No se pudo obtener la clave para {network_name}.")


def generate_and_show_qr():
    """Función para generar y mostrar el código QR de una red seleccionada."""
    networks = get_networks()
    if not networks:
        print("No hay redes disponibles.")
        return

    # Selección de red interactiva
    network_name = interactive_selector(list(networks))
    if network_name:
        password = get_wifi_password(network_name)
        if password:
            generate_qr(network_name, password)
        else:
            print(f"No se pudo generar el QR para {network_name}.")
    else:
        print("No se seleccionó ninguna red.")


def interactive_mode():
    """Modo interactivo: seleccionar una red y mostrar su clave."""
    networks = get_networks()
    if not networks:
        print("No hay redes disponibles.")
        return

    # Selección de red interactiva
    selected_network = interactive_selector(list(networks))
    if selected_network:
        get_password_for_network(selected_network)
    else:
        print("No se seleccionó ninguna red.")


def main():
    """Función principal para procesar los argumentos y ejecutar la aplicación."""
    parser = argparse.ArgumentParser(description="Herramienta de Wi-Fi")
    parser.add_argument("--list", action="store_true", help="Listar redes disponibles")
    parser.add_argument("--password", type=str, help="Obtener la clave de una red")
    parser.add_argument("--qr", action="store_true", help="Genera QR para obtener la red")
    parser.add_argument("--interactive", action="store_true", help="Modo interactivo")
    args = parser.parse_args()

    # Lógica de los argumentos
    if args.list:
        list_networks()
    elif args.password:
        if args.password:
            get_password_for_network(args.password)
        else:
            print("Por favor, proporciona el nombre de la red Wi-Fi con --password.")
    elif args.qr:
        generate_and_show_qr()
    elif args.interactive:
        interactive_mode()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
