#IMPORTAMOS RECURSOS NECESARIOS.
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit,
QVBoxLayout, QHBoxLayout, QPushButton, QProgressBar)
from PyQt5.QtCore import QUrl

class Buscador(QWidget):
    def __init__(self):
        super().__init__()

        #DIMENSIONES Y TÍTULO DE LA VENTANA
        self.resize(740, 520)
        self.setWindowTitle('My web browser')

        #ENTRADA PARA BUSQUEDA.
        page = "https://www.google.com"
        self.url = QLineEdit(page)
        self.url.setPlaceholderText(page)

        #BOTÓN "Ir".
        self.go = QPushButton("Ir")
        self.go.clicked.connect(self.btnIrClicked)

        #AÑADIMOS ELEMENTOS CREADOS
        self.nav_bar = QHBoxLayout()
        self.nav_bar.addWidget(self.url)
        self.nav_bar.addWidget(self.go)

        #BARRA DE PROGRESO
        self.progress = QProgressBar()
        self.progress.setValue(0)

        html = """
        <!DOCTYPE HTML>
            <html>
                <head>
                    <title>PyChrome</title>
                </head>
                <body>
                <style>
                    *{
                    font-family: Arial;
                    }
                </style>
                    <h1>Bienvenido a QtSearch.</h1>
                    <img src=""/>
                    <p>QtSearch es un navegador creado para "El Programador Chapuzas".</p>
                </body>
            </html>
        """        

        #ESPACIO PARA VISIONAR LAS PÁGINAS
        self.web_view = QWebEngineView()
        self.web_view.loadProgress.connect(self.webLoading)
        self.web_view.setHtml(html)
        
        
        #INCLUIMOS "WIDGETS" CREADOS.
        root = QVBoxLayout()
        root.addLayout(self.nav_bar)
        root.addWidget(self.web_view)
        root.addWidget(self.progress)
        self.setLayout(root)

    #FUNCIÓN PARA REALIZAR BÚSQUEDA
    def btnIrClicked(self, event):
        url = QUrl(self.url.text())
        self.web_view.page().load(url)

    #FUNCIÓN PARA ACTUALIZAR BARRA DE PROGRESO
    def webLoading(self, event):
        self.progress.setValue(event)    

#EJECUTAMOS PROGRAMA.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Buscador()
    win.show()
    sys.exit(app.exec_())
