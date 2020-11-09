#IMPORTAMOS RECUROS NECESARIOS.
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        #INICIAR FUNCIÓN.
        self.muestra_foto()
        
        
    def muestra_foto(self):      

        #CREAMOS LAYOUT
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("Honda_Goldwing.jpg")

        #CREAMOS ETIQUETA
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        #AÑADIMOS ETIQUETA AL LAYOUT.
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        #UBICACIÓN Y TÍTULO DE LA VENTANA.
        self.move(400,100)
        self.setWindowTitle('My photo')
        self.show()        
        

#EJECUTAMOS CLASE "Example".
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
