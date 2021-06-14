from os import name
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication

class gui_principal_corrientazo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Interfaz_Corrientazo.ui", self) #cargamos la plantilla que se crea en editor
        
        self.setFixedSize(800, 600) # no permite que modifiquen el tamaño de la ventana, y estable el tamaño por default.
        self.setWindowTitle("Corrientazo Pedidos pendientes") # agrega titulo a la ventana

        self.Boton_1.clicked.connect(self.funcion_activar)
        self.Boton_2.clicked.connect(self.funcion_activar_2)
        
        self.lista_mesas.addItems(["mesa 1", "mesa 2", "mesa 3"])

    def funcion_activar(self):
        print("hemos oprimido el boton 1")

    def funcion_activar_2(self):
        print("hemos oprimido el boton 2")

if __name__ == '__main__': ### si nuestro archivo principal es ejecutado ejecute nuestro codigo.
    app  = QApplication(sys.argv)
    GUI = gui_principal_corrientazo()
    GUI.show()
    sys.exit(app.exec_()) #el app.exec_() ejecuta la aplicacion, es muy importante.


