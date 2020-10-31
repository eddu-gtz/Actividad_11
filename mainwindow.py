from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
#Decorador que se llama cuando se ejecute la aplicacion
from PySide2.QtCore import Slot
#clase Vista
from ui_mainwindow import Ui_MainWindow
#Clases Administradora y Particula
from administradora import Administradora
from particula import Particula

#Controlador de vista
class MainWindow(QMainWindow):
    def __init__(self):
        #inicializar el objeto QMainWindow
        super(MainWindow, self).__init__()
        #Creacion del objeto Administrador de particulas
        self.administrador = Administradora()

        #Objeto de la clase Ui_MainWindow
        self.ui = Ui_MainWindow()
        #Se incrustan las configuraciones de la clase
        self.ui.setupUi(self)
        #Configurar el evento click del boton
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        #Configuracion del menu
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        #configuracion de la tabla
        self.ui.show_table_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.search_pushButton.clicked.connect(self.buscar_particula)

    @Slot()
    def click_mostrar(self):
        #Limpia el PlainText y despues inserta los datos
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.administrador))
    
    @Slot()
    def click_agregar_final(self):
        #Variables para obtener la informacion
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)

        self.administrador.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        #Variables para obtener la informacion
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)

        self.administrador.agregar_inicio(particula)
    
    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)'
        )[0]
        #[0] retorna la ubicacion del archivo

        if self.administrador.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo " + ubicacion
            )

        
    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        #[0] retorna la ubicacion del archivo

        if self.administrador.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se guardó el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se guardó el archivo" + ubicacion
            )
    
    @Slot()
    def mostrar_tabla(self):
        self.ui.table.setColumnCount(10)
        #Definir el titulo de las columnas
        headers = ["Id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Blue", "Green", "Distancia"]
        #Agregar los headers a la tabla
        self.ui.table.setHorizontalHeaderLabels(headers)
        #Agregar las filas en base a los registros almacenados
        self.ui.table.setRowCount(len(self.administrador))
        #contador para las filas
        row = 0
        for particula in self.administrador:
            #Crear los widgets para insertar los elementos en la tabla
            id_widget = QTableWidgetItem(str(particula.id))
            origenx_widget = QTableWidgetItem(str(particula.origen_x))
            origeny_widget = QTableWidgetItem(str(particula.origen_y))
            destinox_widget = QTableWidgetItem(str(particula.destino_x))
            destinoy_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            #insertar el elemento en la fila y columna indicadas
            self.ui.table.setItem(row, 0, id_widget)
            self.ui.table.setItem(row, 1, origenx_widget)
            self.ui.table.setItem(row, 2, origeny_widget)
            self.ui.table.setItem(row, 3, destinox_widget)
            self.ui.table.setItem(row, 4, destinoy_widget)
            self.ui.table.setItem(row, 5, velocidad_widget)
            self.ui.table.setItem(row, 6, red_widget)
            self.ui.table.setItem(row, 7, green_widget)
            self.ui.table.setItem(row, 8, blue_widget)
            self.ui.table.setItem(row, 9, distancia_widget)

            #Aumentar el contador de la fila
            row += 1
            


    @Slot()
    def buscar_particula(self):
        #obtener el id a buscar
        id_buscar = self.ui.search_id_lineEdit.text()
        encontrado = False
        for particula in self.administrador:
            if id_buscar == str(particula.id):
                #limpiar la tabla
                self.ui.table.clear()
                headers = ["Id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Blue", "Green", "Distancia"]
                #Agregar los headers a la tabla
                self.ui.table.setHorizontalHeaderLabels(headers)
                self.ui.table.setRowCount(1)
                #Crear los widgets para insertar los elementos en la tabla
                id_widget = QTableWidgetItem(str(particula.id))
                origenx_widget = QTableWidgetItem(str(particula.origen_x))
                origeny_widget = QTableWidgetItem(str(particula.origen_y))
                destinox_widget = QTableWidgetItem(str(particula.destino_x))
                destinoy_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                #insertar el elemento en la fila y columna indicadas
                self.ui.table.setItem(0, 0, id_widget)
                self.ui.table.setItem(0, 1, origenx_widget)
                self.ui.table.setItem(0, 2, origeny_widget)
                self.ui.table.setItem(0, 3, destinox_widget)
                self.ui.table.setItem(0, 4, destinoy_widget)
                self.ui.table.setItem(0, 5, velocidad_widget)
                self.ui.table.setItem(0, 6, red_widget)
                self.ui.table.setItem(0, 7, green_widget)
                self.ui.table.setItem(0, 8, blue_widget)
                self.ui.table.setItem(0, 9, distancia_widget)

                encontrado = True
                return
        
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La particula: "{id_buscar}" no fue encontrada'
            )
