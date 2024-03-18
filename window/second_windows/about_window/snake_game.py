from PySide6 import QtWidgets, QtCore, QtGui
import random

from functions.settings.settings import load_theme

class SnakeGame(QtWidgets.QDialog):
    def __init__(self, user_id):
        super().__init__()

        self.setWindowTitle("Змейка")
        self.setGeometry(100, 100, 600, 400)
        load_theme(self, user_id)

        self.timer = QtCore.QBasicTimer()
        self.speed = 100
        self.score = 0
        self.direction = "Right"

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = (random.randint(0, 29) * 20, random.randint(0, 19) * 20)

        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.score_label = QtWidgets.QLabel("Score: 0", self)
        self.score_label.setGeometry(400, 10, 200, 50)
        font = self.score_label.font()
        font.setPointSize(20)
        self.score_label.setFont(font)

        self.restart_button = QtWidgets.QPushButton("Начать заново", self)
        self.restart_button.setGeometry(400, 70, 200, 30)
        self.restart_button.clicked.connect(self.startGame)
        self.restart_button.hide()

        self.start_button = QtWidgets.QPushButton("Начать игру", self)
        self.start_button.setGeometry(400, 110, 200, 30)
        self.start_button.clicked.connect(self.startGame)
        self.start_button.setFocus(QtCore.Qt.OtherFocusReason)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for segment in self.snake:
            painter.fillRect(segment[0], segment[1], 20, 20, QtGui.QColor(0, 255, 0))
        painter.fillRect(self.food[0], self.food[1], 20, 20, QtGui.QColor(255, 0, 0))

    def updateScoreLabel(self):
        self.score_label.setText(f"Score: {self.score}")

    def timerEvent(self, event):
        self.move()
        self.checkCollision()
        self.checkFood()
        self.update()
        self.updateScoreLabel()

    def move(self):
        head = self.snake[0]
        if self.direction == "Right":
            new_head = (head[0] + 20, head[1])
        elif self.direction == "Left":
            new_head = (head[0] - 20, head[1])
        elif self.direction == "Up":
            new_head = (head[0], head[1] - 20)
        else:
            new_head = (head[0], head[1] + 20)

        self.snake = [new_head] + self.snake[:-1]

    def checkCollision(self):
        head = self.snake[0]
        if head in self.snake[1:] or head[0] < 0 or head[0] > 580 or head[1] < 0 or head[1] > 380:
            self.timer.stop()
            self.updateScoreLabel()
            self.restart_button.show()
            self.restart_button.setFocus(QtCore.Qt.OtherFocusReason)

    def checkFood(self):
        if self.snake[0] == self.food:
            self.score += 1
            self.food = (random.randint(0, 29) * 20, random.randint(0, 19) * 20)
            self.snake.append(self.snake[-1])

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Down and not self.direction == "Up":
            self.direction = "Down"
        elif key == QtCore.Qt.Key_Up and not self.direction == "Down":
            self.direction = "Up"
        elif key == QtCore.Qt.Key_Left and not self.direction == "Right":
            self.direction = "Left"
        elif key == QtCore.Qt.Key_Right and not self.direction == "Left":
            self.direction = "Right"

        if self.timer.isActive() and key in [QtCore.Qt.Key_Down, QtCore.Qt.Key_Up, QtCore.Qt.Key_Left, QtCore.Qt.Key_Right]:
            self.restart_button.hide()
            self.restart_button.setFocus(QtCore.Qt.NoFocusReason)

    def startGame(self):
        self.score = 0
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = (200, 200)
        self.direction = "Right"
        self.updateScoreLabel()
        self.restart_button.hide()
        self.restart_button.setFocus(QtCore.Qt.NoFocusReason)
        self.start_button.hide()
        # self.setFocus(QtCore.Qt.StrongFocus)  # Устанавливаем фокус на игровое окно
        if not self.timer.isActive():
            self.timer.start(self.speed, self)
