from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 

        self.setWindowTitle("Python ")
 
   
        self.setGeometry(100, 100, 340, 350)
 

        self.UiComponents()
 

        self.show()
 
      
        self.number = 0
 

    def UiComponents(self):
 

        head = QLabel("Угадай число", self)
 

        head.setGeometry(20, 10, 300, 60)
 
  
        font = QFont('Times', 14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
 

        head.setFont(font)
 

        head.setAlignment(Qt.AlignCenter)
 

        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        head.setGraphicsEffect(color)
 
        self.info = QLabel("Добро пожаловать", self)
 

        self.info.setGeometry(40, 85, 260, 60)
 

        self.info.setWordWrap(True)
 

        self.info.setFont(QFont('Times', 13))
        self.info.setAlignment(Qt.AlignCenter)
 

        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black;"
                                "background : lightgrey;"
                                "}")
 

        self.spin = QSpinBox(self)
 

        self.spin.setRange(1, 20)
 

        self.spin.setGeometry(120, 170, 100, 60)
 

        self.spin.setAlignment(Qt.AlignCenter)
        self.spin.setFont(QFont('Times', 15))
 

        check = QPushButton("Проверить", self)
 

        check.setGeometry(130, 235, 80, 30)
 

        check.clicked.connect(self.check_action)
 

        start = QPushButton("Старт", self)
        start.setGeometry(65, 280, 100, 40)
 

        reset_game = QPushButton("Попробовать снова", self)
 
        reset_game.setGeometry(175, 280, 100, 40)
 
        color_red = QGraphicsColorizeEffect()
        color_red.setColor(Qt.red)
        reset_game.setGraphicsEffect(color_red)
 
        color_green = QGraphicsColorizeEffect()
        color_green.setColor(Qt.darkBlue)
        start.setGraphicsEffect(color_green)
 
        start.clicked.connect(self.start_action)
        reset_game.clicked.connect(self.reset_action)
 
    def start_action(self):
 
        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black;"
                                "background : lightgrey;"
                                "}")
 
        self.number = random.randint(1, 20)
        self.info.setText("Попробуй отгадать число от 1 до 20")
 
 
    def check_action(self):
 
        user_number = self.spin.value()
 
        if user_number == self.number:
 
            self.info.setText("Правиль! Ты угадал!")
            self.info.setStyleSheet("QLabel"
                                    "{"
                                    "border : 2px solid black;"
                                    "background : lightgreen;"
                                    "}")
 
        elif user_number < self.number:
 
            self.info.setText("Твое число слишком маленькое")
 
        else:

            self.info.setText("Твое число слишком большое")
 
 
    def reset_action(self):
        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black;"
                                "background : lightgrey;"
                                "}")
        self.info.setText("Добро пожаловать")
 
App = QApplication(sys.argv)
 

window = Window()
 

sys.exit(App.exec())
