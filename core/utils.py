import inquirer

def interactive_selector(options):
    if not options:
        print("No hay opciones disponibles para seleccionar.")
        return None

    question = [
        inquirer.List(
            "selection",
            message="Selecciona una red Wi-Fi:",
            choices=options,
        )
    ]
    answer = inquirer.prompt(question)
    return answer["selection"] if answer else None
