import sys
import PyQt5.QtGui

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel, QDialog, QDesktopWidget


class GameOverWindow(QDialog):
    WIDTH = 300
    HEIGHT = 300

    def __init__(self, parent=None):
        super(GameOverWindow, self).__init__(parent)
        self.initialize_component()

    def initialize_component(self):
        self.setWindowTitle('Tetris')
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.initialize_field()
        self.center_on_screen(self)

    def initialize_field(self):
        self.label = QLabel('GAME OVER !', self)
        self.label.setGeometry(60, 0, 300, 300)
        self.label.setFont(QFont('SansSerif', 15))

    def center_on_screen(self, element):
        resolution = QDesktopWidget().screenGeometry()
        element.move(int((resolution.width() / 2) - (self.frameSize().width() / 2)),
                     int((resolution.height() / 2) - (self.frameSize().height() / 2)))
