import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Publication Counts Graph")
        self.setGeometry(100, 100, 800, 600)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_action = file_menu.addAction("Open CSV")
        open_action.triggered.connect(self.open_csv)

        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.figure = plt.figure(figsize=(10, 6))
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.capture_button = QPushButton("Capture Image")
        self.capture_button.clicked.connect(self.capture_image)
        self.layout.addWidget(self.capture_button)

    def open_csv(self):
        file_dialog = QFileDialog()
        filename, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")

        if filename:
            self.plot_graph(filename)

    def plot_graph(self, filename):
        df = pd.read_csv(filename)
        years = df['Year']
        query_data = df.drop('Year', axis=1)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        colors = ['blue', 'green', 'red', 'purple']
        labels = query_data.columns

        for i, query in enumerate(query_data.columns):
            ax.plot(years, query_data[query], color=colors[i], label=labels[i])

        ax.set_title('Publication Counts over Time')
        ax.set_xlabel('Year')
        ax.set_ylabel('Number of Publications')
        ax.legend()


        self.canvas.draw()

    def capture_image(self):
        file_dialog = QFileDialog()
        filename, _ = file_dialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png)")

        if filename:
            self.figure.savefig(filename)
            print(f"Image captured and saved as '{filename}'.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
