from enum import Enum, auto


class Command(Enum):
    TesteBluetooth = auto()
    Aquisicao = auto()
    Sair = 5


def introduction_page():
    message = """
        SAAESSC

        * Teste de conexão via bluetooth - 1
        * Adquirir dados - 2
        * Sair - 5
    """

    print(message)
    command = int(input("Comando: "))

    return Command(command)
