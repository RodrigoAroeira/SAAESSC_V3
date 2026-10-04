import time

import serial
import serial.tools.list_ports


class DeviceConnectionController:
    def __init__(
        self, baudrate: int = 115200, timeout: int = 1, target_port: str | None = None
    ):
        self.baudrate = baudrate
        self.timeout = timeout
        self.target_port = target_port

    def find_bluetooth_port(self) -> dict:
        ports = serial.tools.list_ports.comports()
        if not ports:
            return {"success": False}

        for port in ports:
            if self.target_port and port.device != self.target_port:
                continue
            if "Bluetooth" not in port.description and "Bluetooth" not in port.hwid:
                continue
            try:
                with serial.Serial(
                    port=port.device,
                    baudrate=self.baudrate,
                    timeout=self.timeout,
                    write_timeout=2,
                ) as ser:
                    for _ in range(10):
                        if self.test_connection(ser):
                            return {"success": True, "port": port.device}
                        time.sleep(0.5)
                    print(f"Conexão não estabelecida na porta {port.device}.")
            except serial.SerialException as e:
                print(f"Erro ao acessar a porta {port.device}: {e}")
        return {"success": False}

    def connect(self, port: str) -> serial.Serial | None:
        try:
            with serial.Serial(
                port=port,
                baudrate=self.baudrate,
                timeout=self.timeout,
                write_timeout=2,
            ) as ser:
                if self.test_connection(ser):
                    return ser
        except serial.SerialException as e:
            print(f"Erro ao conectar: {e}")
        return None

    @staticmethod
    def disconnect(ser: serial.Serial) -> None:
        if ser and ser.is_open:
            ser.close()

    @staticmethod
    def send_data(ser: serial.Serial, data: float | str) -> dict:
        if isinstance(data, (int, float)):
            data = str(data)
        if isinstance(data, str):
            ser.write(data.encode() + b"\n")
            return {"success": True, "data": data}
        return {"success": False}

    @staticmethod
    def read_data(ser: serial.Serial) -> str:
        return ser.readline().decode("utf-8").strip()

    @staticmethod
    def test_connection(ser: serial.Serial) -> bool:
        try:
            ser.write(b"Ping\n")
            return ser.readline().decode("utf-8").strip() == "Pong"
        except (serial.SerialException, UnicodeDecodeError):
            return False
