import serial
from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QComboBox
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont


class QConnector(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Connector")
        self.layout = QHBoxLayout()

        layout = QFormLayout()
        self.portsCombo = QComboBox()
        self.baudrateEdit = QLineEdit("")

        label = QLabel("Port: ")
        label.setBuddy(self.portsCombo)
        layout.addRow(label, self.portsCombo)

        label = QLabel("Baudrate: ")
        label.setBuddy(self.baudrateEdit)
        layout.addRow(label, self.baudrateEdit)

        self.connectButton = QPushButton("Connect")
        self.connectButton.clicked.connect(self.connect)
        self.connectButton.setMinimumWidth(140)
        self.connectButton.setMaximumWidth(200)
        self.connectButton.setMinimumHeight(50)
        self.connectButton.setSizePolicy(self.connectButton.sizePolicy().MinimumExpanding, self.connectButton.sizePolicy().MinimumExpanding)

        # Change the font size from stylesheet
        self.connectButton.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.layout.addLayout(layout)
        self.layout.addWidget(self.connectButton)

        self.setLayout(self.layout)
        self.show()

        # Create a timer to periodically update the serial ports when no port is connected.
        self.refreshPortsTimer = QTimer(self)
        self.refreshPortsTimer.timeout.connect(self.refreshSerialPorts)
        self.refreshPortsInterval = 100  # ms
        self.refreshPortsTimer.start(self.refreshPortsInterval)

    def connect(self):
        print("Connect")


    def refreshSerialPorts(self) -> None:
        availablePorts = [port.portName()
                        for port in QSerialPortInfo.availablePorts()]
        for port in availablePorts:
            self.connectButton.setEnabled(True)
            # Add the port to the combo box if it is not already there.
            if self.portsCombo.findText(port) == -1:
                self.portsCombo.addItem(port)
                self.portsCombo.setEnabled(True)

        for i in range(self.portsCombo.count()):
            # Remove the port from the combo box if it no longer exists.
            if self.portsCombo.itemText(i) not in availablePorts:
                self.portsCombo.removeItem(i)

        # If no ports are available, disable the connect button.
        if availablePorts == []:
            self.connectButton.setEnabled(False)
            self.portsCombo.addItem("No ports detected")
            self.portsCombo.setEnabled(False)
