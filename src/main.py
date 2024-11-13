import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():
    app = QApplication(sys.argv)
    window = QWidget()  # Create a basic window
    window.setWindowTitle("RickRoll App")  # Set window title
    window.resize(400, 300)  # Set window size (width, height)
    window.show()  # Display the window
    sys.exit(app.exec_())  # Run the application's event loop

if __name__ == "__main__":
    main()
