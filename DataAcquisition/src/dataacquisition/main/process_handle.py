import sys

from .constructor.data_visualization_constructor import data_visualization_constructor
from .constructor.device_connection_constructor import device_connection_constructor
from .constructor.introduction_process import Command, introduction_process


def start() -> None:
    while True:
        command = introduction_process()

        match command:
            case Command.TesteBluetooth:
                device_connection_constructor()
            case Command.Aquisicao:
                data_visualization_constructor()
            case Command.Sair:
                sys.exit()
            case _:
                print("\n Comando nao encontrado!! \n\n")
