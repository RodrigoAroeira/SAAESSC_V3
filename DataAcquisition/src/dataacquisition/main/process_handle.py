import sys

from dataacquisition.controllers.data_visualization_controller import (
    DataVisualizationController,
)
from dataacquisition.controllers.device_connection_controller import (
    DeviceConnectionController,
)
from dataacquisition.views.device_connection_view import DeviceConnectionView
from dataacquisition.views.first_view import Command, introduction_page


def run_device_connection() -> None:
    view = DeviceConnectionView()
    controller = DeviceConnectionController()

    view.connecting_view()
    response = controller.find_bluetooth_port()

    if response["success"]:
        view.connected_view(response)
    else:
        view.unconnected_view()


def run_data_acquisition() -> None:
    view = DeviceConnectionView()
    controller = DeviceConnectionController()

    view.connecting_view()
    response = controller.find_bluetooth_port()

    if not response["success"]:
        view.unconnected_view()
        return

    view.connected_view(response)
    ser = controller.connect(response["port"])

    if not ser:
        print("Falha na conexão.")
        return

    data_controller = DataVisualizationController(controller)
    file_path = data_controller.next_available_path("data")

    with open(file_path, "w") as file:
        data_controller.plot_command(ser)
        while True:
            data = data_controller.read_data(ser)
            if data["done"]:
                break
            if not data["success"]:
                continue
            file.write(f"{data['voltage']} {data['current']} {data['time']}\n")
            print(f"{data['voltage']} {data['current']} {data['time']}")


def start() -> None:
    while True:
        command = introduction_page()

        if command is None:
            print("\nComando inválido!\n")
            continue

        match command:
            case Command.TesteBluetooth:
                run_device_connection()
            case Command.Aquisicao:
                run_data_acquisition()
            case Command.Sair:
                sys.exit()
            case _:
                print("\nComando nao encontrado!!\n\n")
