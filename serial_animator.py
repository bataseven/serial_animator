from cmath import inf
import os
import sys
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotx
import logging
import argparse
import sys
import ctypes
import os
from os.path import dirname, abspath
from UI.main_window import MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui
from UI import PyQt5_stylesheets as p5s

# Following 3 line displays the icon of the app on the taskbar.
# https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
myappid = 'bataseven.SerialAnimator.GUI.v1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

logging.getLogger('matplotlib').setLevel(level=logging.CRITICAL)

rcParams.update({'figure.autolayout': True})
plt.style.use(matplotx.styles.github["dimmed"])


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


parser = argparse.ArgumentParser(description='Serial Animator')
parser.add_argument("--port", type=str, help="Serial port to use")
parser.add_argument("--baud", type=int, help="Baud rate to use")

args = parser.parse_args()

args_port = args.port
args_baud = args.baud


def main():
    app = QApplication(sys.argv)

    style = "style_DarkOrange"
    styleSheet = p5s.load_stylesheet_pyqt5(style=style)
    app.setStyleSheet(styleSheet)

    # Change the font across the app
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    app.setFont(font)

    app.setWindowIcon(QtGui.QIcon(
        dirname(abspath(__file__)) + "/UI/images/icon.png"))

    splashImagePath = dirname(abspath(__file__)) + "/UI/images/splash_nobg.png"
    pixmap = QPixmap(splashImagePath)
    splash = QSplashScreen(pixmap)
    splash.show()

    ui = MainWindow()
    ui.centerOnScreen()
    QTimer.singleShot(500, lambda: ui.show())
    splash.finish(ui)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
