class DeviceConnectionView:
    def connecting_view(self) -> None:
        print("Conectando...")

    def connected_view(self, response: dict) -> None:
        print(f"Conectado na porta {response['port']}")

    def unconnected_view(self) -> None:
        print("Falha na conexão.")
