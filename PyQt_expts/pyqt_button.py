import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class App(QWidget):
    """ Example of QPushButton sending signal with values.
    """
    test_value = None
    train_value = None

    def __init__(self):
        super(App, self).__init__()
        train_button = QPushButton("Train", self)
        test_button = QPushButton("Test", self)
        show_button = QPushButton("Show", self)
        train_button.move(100,70)
        test_button.move(250,70)
        show_button.move(400,70)

        test_button.clicked.connect(self.set_test_value)
        train_button.clicked.connect(self.set_train_value)
        show_button.clicked.connect(lambda : self.show_value(self.train_value, self.test_value)) # Connecting with self.show_value callable.

        self.show()

    def show_value(self, a, b):
        print(a,b)

    def set_train_value(self):
        self.train_value = 100

    def set_test_value(self):
        self.test_value = 200
    
if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())