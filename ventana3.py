import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QToolBar, QAction, QMessageBox
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
        filaActual = self.tabla.currentRow()
        if filaActual < 0:
            return QMessageBox.warning(self, 'Error', 'Para borar, debe selecionar un registro'
        )

        boton = QMessageBox.question(
            self,
            'Confirmación',
            '¿Esta seguro de que quieres borrar este registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if boton == QMessageBox.StandardButton.Yes:
            if(
                self.tabla.item(filaActual, 0).text() != '' and
                self.tabla.item(filaActual, 1).text() != '' and
                self.tabla.item(filaActual, 2).text() != '' and
                self.tabla.item(filaActual, 3).text() != '' and
                self.tabla.item(filaActual, 4).text() != '' and
                self.tabla.item(filaActual, 5).text() != '' and
                self.tabla.item(filaActual, 6).text() != '' and
                self.tabla.item(filaActual, 7).text() != '' and
                self.tabla.item(filaActual, 8).text() != '' and
                self.tabla.item(filaActual, 9).text() != '' and
                self.tabla.item(filaActual, 10).text() != ''
            ):

                self.file = open('datos/clientes.txt', 'rb')

                usuarios = []

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
                    usuarios.append(u)

                    # cerramos el archivo
                self.file.close()

                for u in usuarios:
                    # buscamos el usuario por el docuemento
                    if (
                            u.documento == self.tabla.item(filaActual, 3).text()
                    ):
                        # Indicamos que encontramos el documento:
                        existeRegistro = True

                        usuarios.remove(u)
                        break

                self.file = open('datos/clientes.txt', 'wb')

                for u in usuarios:
                    self.file.write(bytes(u.nombreCompleto + ";"
                                          + u.usuario + ";"
                                          + u.contra + ";"
                                          + u.documento + ";"
                                          + u.correo + ";"
                                          + u.pregunta1 + ";"
                                          + u.respuesta1 + ";"
                                          + u.pregunta2 + ";"
                                          + u.respuesta2 + ";"
                                          + u.pregunta3 + ";"
                                          + u.respuesta3, encoding='UTF-8'))
                    self.file.close()

                    self.tabla.removeRow(filaActual)

                    return QMessageBox.question(
                        self,
                        'Confirmación',
                        'El registro ha sido eliminado exitosamente.',
                        QMessageBox.StandardButton.Yes
                    )
                else:
                    self.tabla.removeRow(filaActual)

    def accion_add(self):

        ultimaFila = self.tabla.rowCount()

        self.tabla.insertRow(ultimaFila)

        self.tabla.setItem(ultimaFila, 0, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 1, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 2, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 3, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 4, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 5, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 6, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 7, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 8, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 9, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 10, QTableWidgetItem(''))


    def accion_insert(self):

        filaActual = self.tabla.currentRow()
        if filaActual < 0:
            return QMessageBox.warning(self, 'Error', 'Para ingresar, debe selecionar un registro')

        boton = QMessageBox.question(
            self,
            'Confirmación',
            '¿Estas seguro de que quieres ingresar este nuevo registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        datosVacios = True

        if boton == QMessageBox.StandardButton.Yes:

            if(
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != '' and
                    self.tabla.item(filaActual, 4).text() != '' and
                    self.tabla.item(filaActual, 5).text() != '' and
                    self.tabla.item(filaActual, 6).text() != '' and
                    self.tabla.item(filaActual, 7).text() != '' and
                    self.tabla.item(filaActual, 8).text() != '' and
                    self.tabla.item(filaActual, 9).text() != '' and
                    self.tabla.item(filaActual, 10).text() != ''

            ):

                datosVacios = False

                self.file = open('datos/clientes.txt', 'rb')

                usuarios = []

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
                    usuarios.append(u)

                    # cerramos el archivo
                self.file.close()

                existeRegistro = False

                existeDocumento = False

                for u in usuarios:
                    if(
                            u.nombreCompleto == self.tabla.item(filaActual, 0).text() and
                            u.usuario == self.tabla.item(filaActual, 1).text() and
                            u.contra == self.tabla.item(filaActual, 2).text() and
                            u.documento == self.tabla.item(filaActual, 3).text() and
                            u.correo == self.tabla.item(filaActual, 4).text() and
                            u.pregunta1 == self.tabla.item(filaActual, 5).text() and
                            u.respuesta1 == self.tabla.item(filaActual, 6).text() and
                            u.pregunta2 == self.tabla.item(filaActual, 7).text() and
                            u.respuesta2 == self.tabla.item(filaActual, 8).text() and
                            u.pregunta3 == self.tabla.item(filaActual, 9).text() and
                            u.respuesta3 == self.tabla.item(filaActual, 10).text()

                    ):
                        existeRegistro = True

                        return QMessageBox.warning(self, 'Error', 'Registro diplicado, no se puede registrar')
                        break

                if not existeRegistro:

                    for u in usuarios:
                        if(
                                u.documento == self.tabla.item(filaActual, 3).text()
                        ):

                            # indicamos que encontramos el documento
                            existeDocumento = True

                            u.nombreCompleto = self.tabla.item(filaActual, 0).text()
                            u.usuario = self.tabla.item(filaActual, 1).text()
                            u.contra = self.tabla.item(filaActual, 2).text()
                            u.documento = self.tabla.item(filaActual, 3).text()
                            u.correo = self.tabla.item(filaActual, 4).text()
                            u.pregunta1 = self.tabla.item(filaActual, 5).text()
                            u.respuesta1 = self.tabla.item(filaActual, 6).text()
                            u.pregunta2 = self.tabla.item(filaActual, 7).text()
                            u.respuesta2 = self.tabla.item(filaActual, 8).text()
                            u.pregunta3 = self.tabla.item(filaActual, 9).text()
                            u.respuesta3 = self.tabla.item(filaActual, 10).text()

                            self.file = open('datos/clientes.txt', 'wb')

                            for u in usuarios:
                                self.file.write(bytes(u.nombreCompleto + ";"
                                                      + u.usuario + ";"
                                                      + u.contra + ";"
                                                      + u.documento + ";"
                                                      + u.correo + ";"
                                                      + u.pregunta1 + ";"
                                                      + u.respuesta1 + ";"
                                                      + u.pregunta2 + ";"
                                                      + u.respuesta2 + ";"
                                                      + u.pregunta3 + ";"
                                                      + u.respuesta3, encoding='UTF-8'))
                            self.file.close()
                            return QMessageBox.question(
                                self,
                                'Confirmación',
                                'Los datos del registro se han editado exitosamente.',
                                QMessageBox.StandardButton.Ok
                            )
                            break

                    if not existeDocumento:
                        self.file = open('datos/clientes.txt', 'ab')

                        self.file.write(bytes(self.tabla.item(filaActual, 0).text() + ";"
                                              + self.tabla.item(filaActual, 1).text() + ";"
                                              + self.tabla.item(filaActual, 2).text() + ";"
                                              + self.tabla.item(filaActual, 3).text() + ";"
                                              + self.tabla.item(filaActual, 4).text() + ";"
                                              + self.tabla.item(filaActual, 5).text() + ";"
                                              + self.tabla.item(filaActual, 6).text() + ";"
                                              + self.tabla.item(filaActual, 7).text() + ";"
                                              + self.tabla.item(filaActual, 8).text() + ";"
                                              + self.tabla.item(filaActual, 9).text() + ";"
                                              + self.tabla.item(filaActual, 10).text() + "\n", encoding='UTF-8'))
                        self.file.seek(0, 2)
                        self.file.close()

                        return QMessageBox.question(
                            self,
                            'Confirmación',
                            'Los datos del registro se han ingresado exitosamente.',
                            QMessageBox.StandardButton.Ok
                        )

                if datosVacios:
                    return QMessageBox.warning(self, 'Error', 'Debe ingresar todos los datos en el registro')

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana3 = Ventana3()
    ventana3.show()
    sys.exit(app.exec_())