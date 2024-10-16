from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QDesktopWidget, QMessageBox, QLabel, QPushButton, QDialogButtonBox, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from os.path import dirname, abspath
from .animator import QAnimator
from .connector import QConnector
from .collapsible_box import QCollapsibleBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Serial Animator")
        self.icon = QIcon(dirname(abspath(__file__)) + "/images/icon.png")
        self.setWindowIcon(self.icon)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)
        
        self.collapse = QCollapsibleBox(parent=self, title="Serial Connection", collapsed=False)
        vbox = QVBoxLayout()
        self.connector = QConnector()
        vbox.addWidget(self.connector)
        self.collapse.setContentLayout(vbox)
        

        self.animator = QAnimator()

        self.layout.addWidget(self.collapse)
        self.layout.addWidget(self.animator)

        # Press on the collapse widget to expand it


        # Add Menu Bar
        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu("&File")
        self.helpMenu = self.menuBar.addMenu("&Help")

        self.fileMenu.addAction("Settings...", self.showSettingsDialog)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction("E&xit", self.close)
        self.helpMenu.addAction("About...", self.about)

        self.centerOnScreen()
        self.show()

    def showSettingsDialog(self):
        pass

    def about(self):
        # Show a message dialog
        dialog = QMessageBox()
        dialog.setWindowTitle("About")
        dialog.setWindowIcon(self.icon)
        dialog.setIcon(QMessageBox.Information)
        dialog.findChildren(QLabel)[1].setAlignment(Qt.AlignJustify)
        # Create an html text to show in the dialog
        text = "<html><head/><body>\
        <p><span style=\" font-size:9pt; font-weight:normal; text-align=justify;\">This desktop app was created to visualize the \
        numerical data coming from serial port. Select the port and the baudrate of the connected \
        device (e.g an Arduino) to start visualizing. The program parses the string lines and displays the numerical data on a moving plot. \
        <p><span style=\" font-size:9pt; font-weight:normal;\">Version Number: 1.0.0</span></p>\
        <p><span style=\" font-size:9pt; font-weight:normal;\">Author: <em>Berke Ataseven</em> (bataseven15@ku.edu.tr)</span></p>\
        <p><span style=\" font-size:9pt; font-weight:normal;\"><em><a href=\"https://github.com/bataseven\">See on GitHub...</a></em></span></p>\
        </body></html>"
        dialog.setText(text)
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.exec_()

    def centerOnScreen(self):
        frameGm = self.frameGeometry()
        screen = QDesktopWidget().screenGeometry()
        frameGm.moveCenter(screen.center())
        self.move(frameGm.topLeft())
