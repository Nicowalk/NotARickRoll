import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class RickRollApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("RickRoll App")
        self.resize(400, 300)

        # Create a button
        self.button = QPushButton("Click me!", self)
        self.button.clicked.connect(self.rickroll)  # Connect button click to the rickroll function

        # Add the button to a layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def rickroll(self):
        # url of never gonna give you up
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open(url) #open in default browser

def main():
    app = QApplication(sys.argv)
    window = RickRollApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
