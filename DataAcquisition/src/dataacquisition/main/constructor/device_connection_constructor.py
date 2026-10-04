from dataacquisition.controllers.device_connection_controller import (
    DeviceConnectionController,
)
from dataacquisition.views.device_connection_view import DeviceConnectionView


def device_connection_constructor():
    device_connection_view = DeviceConnectionView()
    device_connection_controller = DeviceConnectionController()

    device_connection_view.connecting_view()
    response = device_connection_controller.find_bluetooth_port()

    if response["success"]:
        device_connection_view.connected_view(response)
        return device_connection_controller
    else:
        device_connection_view.unconnected_view()
