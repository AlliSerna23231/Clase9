import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QToolBar, QAction
from PyQt5 import QtGui

from cliente import Cliente


class Ventana3(QMainWindow):
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

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

        # Abrimos el archivo en modo de lectura:
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

        self.contador = 0

        self.vertical = QVBoxLayout()

         # ---Construir el menu TOOLBAR:

        self.toolbar = QToolBar('Main toolbar')
        self.toolbar.setIconSize(QSize(30,30))
        self.addToolBar(self.toolbar)

        # delete
        self.delete = QAction(QIcon("imagenes/delete.png"), '&Delete', self)
        self.delete.triggered.connect(self.accion_delete)
        self.toolbar.addAction(self.delete)

        # add
        self.add = QAction(QIcon("imagenes/add.png"), '&Add', self)
        self.add.triggered.connect(self.accion_add)
        self.toolbar.addAction(self.add)

        # insert
        self.insert = QAction(QIcon("imagenes/editar.png"), '&Insert', self)
        self.insert.triggered.connect(self.accion_insert)
        self.toolbar.addAction(self.insert)
        # Fin del tool bar




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

        # hacemos que el scroll se adapte a  all sizes:
        self.scrollArea.setWidgetResizable(True)

        # creamos una tabla:
        self.tabla = QTableWidget()

        self.tabla.setColumnCount(11)

        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Usuario',
                                              'Password',
                                              'Documento',
                                              'Correo',
                                              'Pregunta 1',
                                              'Respuesta 1',
                                              'Pregunta 2',
                                              'Respuesta 2',
                                              'Pregunta 3',
                                              'Respuesta 3'])

        self.tabla.setRowCount(self.numeroUsuarios)

        for u in self.usuarios:
            self.tabla.setItem(self.contador,0, QTableWidgetItem(u.nombreCompleto))
            # hacemos que el nombre no se pueda editar
            self.tabla.item(self.contador,0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.contra))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            # hacemos que el nombre no se pueda editar
            self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        self.scrollArea.setWidget(self.tabla)
        self.vertical.addWidget(self.scrollArea)
        self.vertical.addStretch()

        # ---Boton Volver---
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet("Background-color: #A22F88;"
                                       "color: #000000;"
                                       "padding: 10px;"
                                       "margin-top: 10px;"
                                       )
        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.vertical.addWidget(self.botonVolver)

        # ---------------OJO IMPORTANTE PONER AL FINAL-----------
        # Indicamos que el layout principal del fondo es vertical
        self.fondo.setLayout(self.vertical)

    def accion_delete(self):
        print("delete")

    def accion_add(self):
        print("add")

    def accion_insert(self):
        print("insertar")

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana3 = Ventana3()
    ventana3.show()
    sys.exit(app.exec_())