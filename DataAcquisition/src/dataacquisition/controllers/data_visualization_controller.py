import os

import serial

from dataacquisition.controllers.device_connection_controller import (
    DeviceConnectionController,
)


class DataVisualizationController:
    def __init__(self, device_conn: DeviceConnectionController):
        self.device_conn = device_conn

    @staticmethod
    def next_available_path(
        base_name: str, path: str = "Assets/data", extension: str = ".txt"
    ) -> str:
        destination_folder = os.path.abspath(path)
        os.makedirs(destination_folder, exist_ok=True)
        base = os.path.join(destination_folder, base_name)

        counter = 0
        while True:
            file_name = (
                f"{base}{extension}" if counter == 0 else f"{base}_{counter}{extension}"
            )
            if not os.path.exists(file_name):
                return file_name
            counter += 1

    def read_data(self, ser: serial.Serial) -> dict:
        raw = self.device_conn.read_data(ser)
        if raw == "end":
            return {"done": True, "success": True}

        values = raw.split()
        if len(values) == 3:
            return {
                "done": False,
                "success": True,
                "voltage": values[0],
                "current": values[1],
                "time": values[2],
            }
        return {"done": False, "success": False}

    @staticmethod
    def plot_command(ser: serial.Serial) -> None:
        ser.write(b"1\n")
