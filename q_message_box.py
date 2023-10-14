from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")

        self.container = QWidget()
        self.main_layout = QVBoxLayout()

        self.name = QLabel("Content")
        self.button1 = QPushButton("Push for Window")

        self.button1.clicked.connect(self.create_new_window)

        self.main_layout.addWidget(self.name)
        self.main_layout.addWidget(self.button1)

        self.container.setLayout(self.main_layout)
        self.setCentralWidget(self.container)

    def create_new_window(self):
        self.new_window = SecondWindow()
        self.new_window.show()

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        label = QLabel("Second Window")

        self.setCentralWidget(label)
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec()