import matplotlib.pyplot as plt
from matplotlib import animation


class DataVisualizationView:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.fig = plt.figure()
        self.graph = self.fig.add_subplot(111)

    def update_graph(self, i: int) -> None:
        with open(self.file_path, "r") as f:
            lines = f.read().splitlines()

        time, voltage, current = [], [], []
        for line in lines:
            values = line.split()
            if len(values) == 3:
                voltage.append(float(values[0]))
                current.append(float(values[1]))
                time.append(float(values[2]))

        self.graph.cla()
        self.graph.plot(time, voltage, label="Voltage")
        self.graph.plot(time, current, label="Current")
        self.graph.legend(loc="upper left")
        self.fig.tight_layout()

    def plot_figure(self) -> None:
        animation.FuncAnimation(self.fig, self.update_graph, interval=1000)
        plt.tight_layout()
        plt.show()
