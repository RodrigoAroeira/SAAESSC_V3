from enum import Enum, auto


class Command(Enum):
    TesteBluetooth = auto()
    Aquisicao = auto()
    Sair = 5


def introduction_page() -> Command | None:
    message = """
        SAAESSC

        * Teste de conexão via bluetooth - 1
        * Adquirir dados - 2
        * Sair - 5
    """

    print(message)

    try:
        command = int(input("Comando: "))
        return Command(command)
    except ValueError, KeyError:
        return None
