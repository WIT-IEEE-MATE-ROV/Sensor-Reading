from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication([])
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.black)
app.setPalette(palette)
button = QPushButton("Acceleration X: \nAccleration Y: \nAcceleration Z: \n\nMag X: \nMag Y: \nMag Z: \n\nGyro X: "
                     "\nGyro Y: \nGyro Z: ")
button.show()
app.exec_()
