import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        #CREAMOS VENTANA.
        self.resize(250,150)
        self.setWindowTitle("Reloj digital con PyQt5")

        layout = QVBoxLayout()
        fnt = QFont('Open Sans', 120, QFont.Bold)

        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setFont(fnt)
        layout.addWidget(self.lbl)
        
        self.setLayout(layout)
        
        #CREAMOS EL 'TIMER'
        timer = QTimer(self)
        
        timer.timeout.connect(self.displayTime)
        timer.start(1000)

    #FUNCIÓN PARA MOSTRAR HORA.
    def displayTime(self):
        currentTime = QTime.currentTime()

        displayText = currentTime.toString('hh:mm:ss')

        self.lbl.setText(displayText)
        
#EJECUTAMOS APLICACIÓN.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
sys.exit(app.exec_())
