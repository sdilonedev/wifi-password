import qrcode

def generate_qr(wifi_name, wifi_password):
    data = f"WIFI:S:{wifi_name};T:WPA;P:{wifi_password};;"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=3, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.get_matrix()

    for row in qr_image:
        print("".join(["█" if col else " " for col in row]))
