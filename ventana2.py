import math
import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel, QVBoxLayout,  QScrollArea, QWidget, QGridLayout, QButtonGroup, QPushButton
from PyQt5 import QtGui

from cliente import Cliente


class Ventana2(QMainWindow):
    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Usuarios Registrados")
        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon("imagenes/flore.png"))


        self.ancho = 900
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedSize(self.ancho, self.alto)

        # para que la ventana no se pueda cambiar de tamaño
        # se fija el ancho y alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap('imagenes/light-pink-background-free-photo.jpg')

        # asignamos la imagen
        self.fondo.setPixmap(self.imagenFondo)

        # establecer el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # el tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # establecemos la ventana fondo como la ventana central
        self.setCentralWidget(self.fondo)

        self.vertical = QVBoxLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Usuarios Registrados")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andalem Mono", 20))

        # Le ponemos el color del texto:
        self.letrero1.setStyleSheet("color: #FE0000;")

        # Agregamos el letrero en la primera fila:
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        # creamos un scroll:
        self.scrollArea = QScrollArea()

        # le ponemos el transparente el fondo del scroll
        self.scrollArea.setStyleSheet("background-color: transparent;")

        # hacemos que el scroll se adapte a  all sizes:
        self.scrollArea.setWidgetResizable(True)

        # Creamos una ventana contenedora para cada celda:
        self.contenedora = QWidget()

        # vamos a crear un layout de grid para poner una cuadricula de elementos:
        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        # metemos en el layout vertical el scroll:
        self.vertical.addWidget(self.scrollArea)

        #Abrimos el archivo en modo de lectura:
        self.file = open('datos/clientes.txt', 'rb')

        # lista vacia para guardar los usuarios:
        self.usuarios = []

        # recorremos el archivo, línea por linea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")
            # Separa si ya no hay mas registros en el archivo
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )
            # metemos el objeto en la lista de usuarios:
            self.usuarios.append(u)

            # cerramos el archivo
        self.file.close()

        # obtenemos el numero de usuaurios registrados:
        # consultamos el tamaño de las listas usuarios:
        self.numeroUsuarios = len(self.usuarios)

        # contador de elementos para controlar a los usuarios en la lista usuarios:
        self.contador = 0

        self.elementosPorColumna = 3

        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        self.botones = QButtonGroup()

        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):

                if self.contador < self.numeroUsuarios:

                    self.ventanaAuxiliar = QWidget()

                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    self.verticalCuadricula = QVBoxLayout()

                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    self.botonAccion.setFixedWidth(150)

                    self.botonAccion.setStyleSheet("Background-color: #A22F88;"
                                                   "color: #000000;"
                                                   "padding: 10px;"
                                                   )

                    self.verticalCuadricula.addWidget(self.botonAccion)

                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    self.verticalCuadricula.addStretch()

                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    self.contador += 1

        self.botones.idClicked.connect(self.metodo_accionBotones)

        # ---------------OJO IMPORTANTE PONER AL FINAL-----------
        # Indicamos que el layout principal del fondo es vertical
        self.fondo.setLayout(self.vertical)

    def metodo_accionBotones(self, cedulaUsuario):
        print(cedulaUsuario)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana2 = Ventana2()
    ventana2.show()
    sys.exit(app.exec_())
