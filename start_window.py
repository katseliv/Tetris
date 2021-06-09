import sys
import PyQt5.QtGui

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import QMainWindow, QLabel, QDialog, QDesktopWidget, QSlider, QApplication

import logic
from field import Field
from game_over_window import GameOverWindow


class StartWindow(QMainWindow):
    WIDTH = 650
    HEIGHT = 750

    def __init__(self):
        super(StartWindow, self).__init__()
        self.initialize_component()
        self.show()

    def initialize_component(self):
        self.setWindowTitle('Tetris')
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.initialize_background_music()
        self.initialize_wall()
        self.center_on_screen(self)
        self.initialize_start_button()
        self.initialize_settings_button()
        self.initialize_quit_button()

    def initialize_background_music(self):
        playlist = QMediaPlaylist(self)
        playlist.addMedia(
            QMediaContent(QUrl.fromLocalFile('C:\\Users\\katse\\PycharmProjects\\Task_6\\music\\background_music.mp3')))
        playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.player = QMediaPlayer(self)
        self.player.setPlaylist(playlist)
        self.player.setVolume(50)
        self.player.play()

    def initialize_wall(self):
        label = QLabel(self)
        label.setStyleSheet("QLabel { border-image: url(images/tetris.jpeg) }")
        label.setFixedWidth(1536)
        label.setFixedHeight(864)

    def initialize_start_button(self):
        self.btn = QtWidgets.QPushButton('Start Game', self)
        self.btn.setMinimumSize(QSize(20, 40))
        self.btn.setStyleSheet("QPushButton { background-color: white }"
                               "QPushButton:hover  { background-color: #abdb58 }")
        self.btn.move(int(self.WIDTH / 2) - 50, int(self.HEIGHT / 2) - 100)
        self.btn.clicked.connect(self.btn_start_game_clicked)

    def initialize_settings_button(self):
        self.btn = QtWidgets.QPushButton('Settings', self)
        self.btn.setMinimumSize(QSize(20, 40))
        self.btn.setStyleSheet("QPushButton { background-color: white }"
                               "QPushButton:hover  { background-color: #52a1eb }")
        self.btn.move(int(self.WIDTH / 2) - 50, int(self.HEIGHT / 2) - 50)
        self.btn.clicked.connect(self.btn_settings_clicked)

    def initialize_quit_button(self):
        self.btn = QtWidgets.QPushButton('Quit', self)
        self.btn.setMinimumSize(QSize(20, 40))
        self.btn.setStyleSheet("QPushButton { background-color: white }"
                               "QPushButton:hover  { background-color: #e856cb }")
        self.btn.move(int(self.WIDTH / 2) - 50, int(self.HEIGHT / 2))
        self.btn.clicked.connect(self.close)

    def center_on_screen(self, element):
        resolution = QDesktopWidget().screenGeometry()
        element.move(int((resolution.width() / 2) - (self.frameSize().width() / 2)),
                     int((resolution.height() / 2) - (self.frameSize().height() / 2)))

    def btn_start_game_clicked(self):
        self.hide()
        dialog = GameWindow(parent=self)
        if dialog.exec():
            pass
        self.show()

    def btn_settings_clicked(self):
        self.hide()
        dialog = SettingsWindow(self.player, parent=self)
        if dialog.exec():
            pass
        self.show()


class GameWindow(QDialog):
    WIDTH = 650
    HEIGHT = 750

    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)
        self.initialize_component()

    def initialize_component(self):
        self.setWindowTitle('Tetris')
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.initialize_field()
        self.center_on_screen(self)

    def initialize_field(self):
        self.up_layout = QtWidgets.QVBoxLayout(self)
        self.up_layout.addWidget(Field(parent=self))

    def center_on_screen(self, element):
        resolution = QDesktopWidget().screenGeometry()
        element.move(int((resolution.width() / 2) - (self.frameSize().width() / 2)),
                     int((resolution.height() / 2) - (self.frameSize().height() / 2)))


class SettingsWindow(QDialog):
    WIDTH = 650
    HEIGHT = 750

    def __init__(self, player, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.initialize_component()
        self.player = player

    def initialize_component(self):
        self.setWindowTitle('Tetris')
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.initialize_wall()
        self.initialize_labels()
        self.initialize_sliders()
        self.centerOnScreen(self)

    def initialize_wall(self):
        label = QLabel(self)
        label.setStyleSheet("QLabel { border-image: url(images/tetris.jpeg) }")
        label.setFixedWidth(1536)
        label.setFixedHeight(864)

    def initialize_labels(self):
        style = "QLabel { color: white }"
        self.title = QLabel('Settings', self)
        self.title.setGeometry(250, 10, 300, 300)
        self.title.setFont(QFont('SansSerif', 20))
        self.title.setStyleSheet(style)

        self.volume_label = QLabel('Volume: ', self)
        self.volume_label.setGeometry(225, 110, 300, 300)
        self.volume_label.setFont(QFont('SansSerif', 12))
        self.volume_label.setStyleSheet(style)

        self.unuseful_label = QLabel('Adjust something: ', self)
        self.unuseful_label.setGeometry(225, 250, 300, 300)
        self.unuseful_label.setFont(QFont('SansSerif', 12))
        self.unuseful_label.setStyleSheet(style)

    def initialize_sliders(self):
        style = """
                QSlider::groove:horizontal {
                    border-radius: 1px;
                    height: 7px;
                    margin: 0px;
                    background-color: #ffffff;
                }
                QSlider::handle:horizontal {
                    background-color: #abdb58;
                    border: none;
                    height: 40px;
                    width: 20px;
                    margin: -20px 0;
                    border-radius: 10px;
                    padding: -20px 0px;
                }
                QSlider::handle:horizontal:hover {
                    background-color: #e856cb;
                }
                QSlider::handle:horizontal:pressed {
                    background-color: #b340b3;
                }
                """

        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setGeometry(225, 285, 200, 30)
        self.volume_slider.setMinimumSize(QSize(30, 50))
        self.volume_slider.setStyleSheet(style)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged[int].connect(self.change_value)

        self.unuseful_slider = QSlider(Qt.Horizontal, self)
        self.unuseful_slider.setGeometry(225, 425, 200, 30)
        self.unuseful_slider.setMinimumSize(QSize(30, 50))
        self.unuseful_slider.setStyleSheet(style)
        self.unuseful_slider.setValue(50)

    def change_value(self, value):
        self.player.setVolume(value)

    def centerOnScreen(self, element):
        resolution = QDesktopWidget().screenGeometry()
        element.move(int((resolution.width() / 2) - (self.frameSize().width() / 2)),
                     int((resolution.height() / 2) - (self.frameSize().height() / 2)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StartWindow()
    sys.exit(app.exec_())
