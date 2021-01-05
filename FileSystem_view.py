import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PyQt5.QtCore import QModelIndex

class FileSystemView(QWidget):
   def __init__(self, dir_path):
      super().__init__()

      #TITULO Y DIMENSIONES DE LA VENTANA.
      self.setWindowTitle('File System Viewer')
      self.setGeometry(300, 300, 800, 300)

      #DEFINIR DIRECTORIO.
      self.model = QFileSystemModel()
      self.model.setRootPath(dir_path)

      #GENERAR VISTA DE ARCHIVOS Y CARPETAS.
      self.tree = QTreeView()
      self.tree.setModel(self.model)
      self.tree.setRootIndex(self.model.index(dirPath))
      self.tree.setColumnWidth(200,250)
      self.tree.setAlternatingRowColors(True)

      #MOSTRAR VENTANA CON LAS VISTA.
      layout = QVBoxLayout()
      layout.addWidget(self.tree)

      self.setLayout(layout)


if __name__ == '__main__':
   app = QApplication(sys.argv)

   #DIRECTORIO BASE.
   dirPath = os.getcwd()

   demo = FileSystemView(dirPath)
   demo.show()
   sys.exit(app.exec_())
