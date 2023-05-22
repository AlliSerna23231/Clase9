import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QVBoxLayout, QDialog, QDialogButtonBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from cliente import Cliente
from ventana2 import Ventana2


class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        self.setWindowTitle("Formulario de Registro")

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

        # ventana en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # para que la ventana no se pueda cambiar de tamaño
        # se fija el ancho y alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap('imagenes/paisaje.jpg')

        # asignamos la imagen
        self.fondo.setPixmap(self.imagenFondo)

        # establecer el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # el tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # establecemos la ventana fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribuccion de los elementos en Layout horizontal
        self.horizontal = QHBoxLayout()
        # Le ponemos las margenes:
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # *****************Layout IZQUIERDO******************

        # creamos el layout del lado izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Información del Cliente")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andalem Mono", 20))

        # Le ponemos el color del texto:
        self.letrero1.setStyleSheet("color: #FE0000;")

        # Agregamos el letrero en la primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        # Agregamos el layout ladoIzquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # Hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(340)

        # Les escribimos el e¿texto
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero2.setFont(QFont("Andalem Mono", 10))

        # Le ponemos el color del texto y margenes:
        self.letrero2.setStyleSheet("color: #FE0000; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #FE0000;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        # Hacemoc el campo para ingresar el usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar la contraseña:
        self.contra = QLineEdit()
        self.contra.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Contraseña*", self.contra)

        # Hacemos el campo para ingresar la contraseña2:
        self.contra2 = QLineEdit()
        self.contra2.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Contraseña*", self.contra2)

        # Hacemos el campo para agregar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # Hacemos el botón para registrar los datos:
        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(90)
        self.botonRegistrar.setStyleSheet("background-color: #A22F88;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Hacemos el botón para limpiar los datos:
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setStyleSheet("background-color: #A22F88;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los botones al Layout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # Agregamos el layout ladoIzquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # *****************Layout DERECHO******************

        # creamos el layout del lado izquierdo:
        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # Hacemos el letrero
        self.letrero3 = QLabel()

        # Le escribimos el texto:
        self.letrero3.setText("Recuperar Contraseña")

        # Le asignamos el tipo de letra
        self.letrero3.setFont(QFont("Andalem Mono", 20))

        # Le ponemos el color del texto:
        self.letrero3.setStyleSheet("color: #FE0000;")

        # Agregamos el letrero en la primera fila:
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero:
        self.letrero4 = QLabel()

        # Establecemos el ancho del label:
        self.letrero4.setFixedWidth(400)

        # Les escribimos el e¿texto
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero4.setFont(QFont("Andalem Mono", 10))

        # Le ponemos el color del texto y margenes:
        self.letrero4.setStyleSheet("color: #FE0000; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #FE0000;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.letrero4)

        # --- 1

        # Hacemos el letrero de la pregunta 1
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta1)

        # Hacemos el campo para ingresar la pregunta1:
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.pregunta1)

        # Hacemos el letrero de la respuesta 1
        self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # Hacemos el campo para ingresar la respuesta1:
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.respuesta1)

        # --- 2

        # Hacemos el letrero de la pregunta 2
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta2)

        # Hacemos el campo para ingresar la pregunta2:
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.pregunta2)

        # Hacemos el letrero de la respuesta 2
        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # Hacemos el campo para ingresar la respuesta2:
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.respuesta2)

        # --- 3

        # Hacemos el letrero de la pregunta 3
        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta3)

        # Hacemos el campo para ingresar la pregunta1:
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.pregunta3)

        # Hacemos el letrero de la respuesta 1
        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # Hacemos el campo para ingresar la respuesta3:
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow(self.respuesta3)

        # Hacemos el botón para buscar las preguntas:
        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(90)
        self.botonBuscar.setStyleSheet("background-color: #A22F88;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)

        # Hacemos el botón para recuperar la contraseña:
        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(90)
        self.botonRecuperar.setStyleSheet("background-color: #A22F88;"
                                            "color: #FFFFFF;"
                                            "padding: 10px;"
                                            "margin-top: 40px;")
        self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)

        # Hacemos el botón para continuar en la ventana sigueinte:
        self.botonContinuar = QPushButton("Continuar")
        self.botonContinuar.setFixedWidth(90)
        self.botonContinuar.setStyleSheet("background-color: #A22F88;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonContinuar.clicked.connect(self.accion_botonContinuar)

        # Agregamos los botones al Layout ladoIzquierdo:
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)
        self.ladoDerecho.addRow(self.botonContinuar)

        # Agregamos el layout ladoDerecho al layout horizontal:
        self.horizontal.addLayout(self.ladoDerecho)

        # ---------------OJO IMPORTANTE PONER AL FINAL-----------
        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)

        # -----------Construccion de la ventana emergente----------------

        # Creamos la ventana de diálogo:
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Poner el icono:
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("imagenes/flore.png"))

        # Definimos el tamaño de la ventana:
        self.ventanaDialogo.resize(300, 150)

        # Creamos el boton de aceptar:
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # Configuramos la ventana para que sea modal:
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos un layout vertical:
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes:
        self.mensaje = QLabel("")

        # Le ponemos estilo al label mensaje:
        self.mensaje.setStyleSheet("background-color: #A22F88; color: #FFFFFF; padding: 10px;")

        # agregamos el label de mensajes
        self.vertical.addWidget(self.mensaje)

        # Agregamos las opciones de los botones.
        self.vertical.addWidget(self.opciones)

        # Establecemos el layout para la ventana de dialogo:
        self.ventanaDialogo.setLayout(self.vertical)


    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.contra.setText('')
        self.contra2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def accion_botonContinuar(self):
        self.hide()
        self.ventana2 = Ventana2(self)
        self.ventana2.show()

    def accion_botonBuscar(self):

        # Creamos una variable para validar si los datos estan correctos
        self.datosCorrectos = True

        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Buscar preguntas de validación")

        # Validar que se haya ingresado el documento.
        if (
                self.documento.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("Si va a buscar las preguntas"
                                 " para recuperar la contraseña."
                                 "\nDebe primero, ingresar el documento.")

            # hacemos que la ventanaDIalogo se vea:
            self.ventanaDialogo.exec_()

        # validar si el documento si es numerico
        if (
                not self.documento.text().isnumeric()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("El documento debe ser númerico."
                                 "\nNo debe ingresar letras "
                                 "ni caracterés especiales.")

            # hacemos que la ventanaDIalogo se vea:
            self.ventanaDialogo.exec_()

            # limpiamos el campo del documento:
            self.documento.setText('')

        # Si los datos están correctos:
        if (
                self.datosCorrectos
        ):
            # Abrimos el archivo en modo de lectura:
            self.file = open('datos/clientes.txt', 'rb')

            # Lista vacia para guardar los usuarios
            usuarios = []

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

            # en este punto ya tenemos la lista users con todos los usuarios

            # variable para controlar si exite el docuemento
            existeDocumento = False

            # Buscamos en la lista users por users para ver si existe la cedula:
            for u in usuarios:
                if u.documento == self.documento.text():
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)

                    # indicamos que encontramos el dodumento:
                    existeDocumento = True

                    # paramos el for
                    break

            # Si no exite un usuario con este documento:
            if (
                    not existeDocumento
            ):
                # escribimos el texto explicativo:
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     +self.documento.text())

                # hacemos que la ventanaDIalogo se vea:
                self.ventanaDialogo.exec_()





    def accion_botonRecuperar(self):

        # Creamos una variable para validar si los datos estan correctos
        self.datosCorrectos = True

        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Recuperar contraseña")

        # Validar que se haya ingresado las preguntas:
        if (
                self.pregunta1.text() == '' or
                self.pregunta2.text() == '' or
                self.pregunta3.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("Para recuperar la contraseña debe"
                                 "\nbuscar las preguntas de verificación."
                                 "\n\nPrimero ingrese su documento y luego"
                                 "\npresione el botón 'Buscar'")

            # hacemos que la ventanaDIalogo se vea:
            self.ventanaDialogo.exec_()

        # Validamos si se buscaron las preguntas pero no se ingresaron las respuestas:
        if (
                self.pregunta1.text() != '' and
                self.respuesta1.text() == '' and
                self.pregunta2.text() != '' and
                self.respuesta2.text() == '' and
                self.pregunta3.text() != '' and
                self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("Para recuperar la contraseña debe"
                                 "\ningresar las respuestas a cada pregunta.")

            # hacemos que la ventanaDIalogo se vea:
            self.ventanaDialogo.exec_()

        # Si los datos son correctos:
        if(
            self.datosCorrectos
        ):
            # Abrimos el archivo en modo de lectura:
            self.file = open('datos/clientes.txt', 'rb')

            # Lista vacia para guardar los usuarios
            usuarios = []

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

            # En este punto tenemos la lista de usuarios con todos los usuarios:

            # variable para controlar si existe el documento:
            existeDocumento = False

            # Definimos las variables para guardar las preguntas:
            resp1 = ''
            resp2 = ''
            resp3 = ''
            contraa = ''

            # Buscamos en la lista usuarios por usuario si existe la cédula:
            for u in usuarios:
                if u.documento == self.documento.text():
                    # Indicamos que encontramos el documeto:
                    existeDocumento = True
                    # Guardamos las respuestas
                    resp1 = u.respuesta1
                    resp2 = u.respuesta2
                    resp3 = u.respuesta3
                    contraa = u.contra
                    # Paramos el for
                    break

            # Verificamos si las respuestas son las correctas:
            # Hacemos que las respuestas sean en letra misnuscula
            if (
                # usamos strip() para borrar espacios y saltos de lineas:
                self.respuesta1.text().lower().strip() == resp1.lower().strip() and
                self.respuesta2.text().lower().strip() == resp2.lower().strip() and
                self.respuesta3.text().lower().strip() == resp3.lower().strip()
            ):
                # Limpiamos los campos
                self.accion_botonLimpiar()

                # Escribimos el texto explicativo:
                self.mensaje.setText("Contraseña: " + contraa)

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()
            else:
                # Escribimos el texto explicativo:
                self.mensaje.setText("Las respuestas son incorrectas "
                                     "\npara estas preguntas de recuperación."
                                     "\n\nVuelva a intentarlo...suerte.")

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()

    def accion_botonRegistrar(self):

        # Creamos una variable para validar si los datos estan correctos
        self.datosCorrectos = True

        # validamos que las contra sean iguales
        if (
            self.contra.text() != self.contra2.text()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Las contraseñas no son iguales")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # Validamos que se ingresen todos los campos
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.contra.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe llenar todos los campos")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # Si los datos están correctos:
        if self.datosCorrectos:

            # Abrimos el archivo en modo agregar escribiendo datos en binario.
            self.file = open('datos/clientes.txt', 'ab')

            # traer el texto de los QLineEdit() y los agrega concatenandolos.
            # para escribirlos en el archivo en formato binario utf-8
            self.file.write(bytes(
                self.nombreCompleto.text() + ";"
                + self.usuario.text() + ";"
                + self.contra.text() + ";"
                + self.documento.text() + ";"
                + self.correo.text() + ";"
                + self.pregunta1.text() + ";"
                + self.respuesta1.text() + ";"
                + self.pregunta2.text() + ";"
                + self.respuesta2.text() + ";"
                + self.pregunta3.text() + ";"
                + self.respuesta3.text() + "\n"
                ,encoding='UTF-8'))
            self.file.close()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un onjeto de tipo Ventana1 con el nombre de ventana1
    ventana1 = Ventana1()
    # hacer que objeto ventana 1 se vea
    ventana1.show()

    sys.exit(app.exec_())