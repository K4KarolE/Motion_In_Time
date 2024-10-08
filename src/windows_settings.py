from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


def window_settings_set_style(self, button_color, button_color_clicked):
    self.setStyleSheet(
                    "QMainWindow"
                        "{"
                        f"background-color : {button_color};"
                        "border-radius: 5px;"
                        "border: 2px solid black;"
                        "}"

                    "QPushButton"
                        "{"
                        f"background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 0.3 {button_color}, stop: 0.6 {button_color}, stop: 1 {button_color_clicked} );"
                        "border-radius: 5px;"
                        "border: 1px solid black;"
                        "}"

                    "QPushButton::pressed"
                        "{"
                        f"background-color : {button_color_clicked};"
                        "}"

                    "QSlider::handle"
                        "{"
                        "width: 10;"
                        "border-radius: 3px;"
                        "background-color : 'black';"
                        "margin: -5 px;  /* expand outside the groove */"
                        "}"
                    
                    "QSlider::groove"
                        "{"
                        "height: 5px;"
                        "border-radius: 2px;"
                        f"background-color : {button_color_clicked};"
                        "}"
                    )



def window_skin_set_style(self, button_color, button_color_clicked):
    self.setStyleSheet(
                    "QPushButton"
                        "{"
                        f"background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 0.3 {button_color}, stop: 0.6 {button_color}, stop: 1 {button_color_clicked} );"
                        "border-radius: 5px;"
                        "border: 1px solid black;"
                        "}"

                    "QPushButton::pressed"
                        "{"
                        f"background-color : {button_color_clicked};"
                        "}"

                    "QTabWidget"
                        "{"
                        f"background: {button_color_clicked};"
                        "}"
                    )



def button_set_style(self, button_color, button_color_clicked):
    self.setStyleSheet(
                    "QPushButton"
                        "{"
                        f"background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 0.3 {button_color}, stop: 0.6 {button_color}, stop: 1 {button_color_clicked} );"
                        "border-radius: 6px;"
                        "border: 2px solid black;"
                        "}"

                    "QPushButton::pressed"
                        "{"
                        f"background-color : {button_color_clicked};"
                        "}"
                    )



'''
Qt.WindowType:

Sheet: closing the main window --> closing settings window as well
WindowStaysOnTopHint: settings window stays on top
    - even when clicked elsewhere
    - even when the main window get minimized
'''
class MySettingsWindow(QMainWindow):
    def __init__(self, window_title, button_color, button_color_clicked, width, height, pos_x, pos_y):
        super().__init__()

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Sheet)
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setWindowTitle(window_title)
        self.setWindowIcon(QIcon(f'skins/_images/settings.png'))
        self.move(pos_x, pos_y)
        window_settings_set_style(self, button_color, button_color_clicked)


