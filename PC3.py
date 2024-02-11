'''
Problema 1
Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque.
'''
def pregunta_1(fraccion):
    try:
        x,y = map(int, fraccion.split('/'))

        if not (0 < x <= y and y != 0):
            raise ValueError("X debe ser menor o igual a Y. Y debe ser diferente de 0.")

        porcentaje = (x / y) * 100
        if porcentaje < 1:
            return 'E'
        elif porcentaje > 99:
            return 'F'
        else:
            return f'{round(porcentaje)}%'

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None

while True:
    entrada = input("Ingrese una fracción en formato X/Y: ")
    resultado = pregunta_1(entrada)
    
    if resultado is not None:
        print(f"La cantidad de combustible en el tanque es: {resultado}")
        break

'''
Problema 2
Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)
'''
def obtener_calificaciones():
    while True:
        alumno = input("Coloque el nombre del alumno: ").upper()
        entrada = input(f"Ingrese las notas de {alumno} separadas por comas: ")

        try:
            calificaciones_str = entrada.split(',')
            calificaciones = [int(calificacion) for calificacion in calificaciones_str]

            if all(0 <= calificacion <= 20 for calificacion in calificaciones): #Las notas deben estar entre 0 y 20
                print("Calificaciones ingresadas correctamente:", calificaciones)
                return calificaciones
            else:
                print("Error: Las calificaciones deben estar en el rango de 0 a 20.")

        except ValueError:
            print("Error de inscripción. Coloque solo números.")

# Llamar a la función para obtener las calificaciones
calificaciones_obtenidas = obtener_calificaciones()

'''
Problema 3:
Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.
'''
import math #Nos permitir usar pi

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area
try:

    radio_usuario = float(input("Ingrese el radio del círculo: "))
    mi_circulo = CIRCULO(radio_usuario)
    area_circulo = mi_circulo.calcular_area()
    print(f"El área del círculo con radio {radio_usuario} es: {area_circulo:.2f}")

except ValueError:
    print("Error: Ingrese un valor numérico para el radio del círculo.")

'''
Problema 4:
Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase.
'''
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

# Ejemplo de uso de la clase RECTANGULO
try:
    # Solicitar al usuario los valores para largo y ancho del rectángulo
    largo_re = float(input("Ingrese el largo del rectángulo: "))
    ancho_re= float(input("Ingrese el ancho del rectángulo: "))

    # Crear una instancia de la clase RECTANGULO
    mi_rectangulo = RECTANGULO(largo_re, ancho_re)

    # Calcular y mostrar el área del rectángulo
    area_rectangulo = mi_rectangulo.calcular_area()
    print(f"El área del rectángulo es: {area_rectangulo}")

except ValueError:
    print("Error: Ingrese valores numéricos para el largo y el ancho del rectángulo.")

'''
Problema 5
Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante.
'''
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = None

    def display(self):
        print("Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        print(f"Edad: {self.edad}" if self.edad is not None else "Edad: No asignada")
        print(f"Notas: {self.notas}" if self.notas is not None else "Notas: No asignadas")

    def set_age(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        # Verificar que todas las notas estén en el rango de 0 a 20
        if all(0 <= nota <= 20 for nota in notas):
            self.notas = notas
        else:
            print("Error: Las notas deben estar en el rango de 0 a 20.")


nombre_alumno = input("Ingrese el nombre del estudiante: ").upper()
numero_registro_alumno = input("Ingrese el número de registro del estudiante: ")

mi_alumno = Alumno(nombre_alumno, numero_registro_alumno)

# Asignar edad al estudiante
edad_alumno = int(input("Ingrese la edad del estudiante: "))
mi_alumno.set_age(edad_alumno)

# Asignar notas al estudiante
notas_alumno = input("Ingrese las notas del estudiante (separadas por comas): ").split(',')
notas_alumno = [float(nota) for nota in notas_alumno]  # Convertir a números decimales
mi_alumno.set_notas(notas_alumno)

'''
Problema 6
Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase
Catálogo y Producto, realizar un objeto dentro de un catálogo productos el cual debe tener un
método para agregar productos y otra para mostrar toda la lista de productos.
Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede
agregar más atributos a los productos para que se puedan hacer otras funcionalidades
'''

class Producto:
    def __init__(self, nombre, categoria, precio, año):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - Año: {self.año}, Precio: {self.precio}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            print("Lista de productos en el catálogo:")
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if not productos_filtrados:
            print(f"No hay productos del año {año} en el catálogo.")
        else:
            print(f"Productos del año {año}:")
            for producto in productos_filtrados:
                print(producto)

    def filtrar_por_categoria(self, categoria):
        productos_filtrados = [producto for producto in self.productos if producto.categoria == categoria]
        if not productos_filtrados:
            print(f"No hay productos en la categoría {categoria} en el catálogo.")
        else:
            print(f"Productos en la categoría {categoria}:")
            for producto in productos_filtrados:
                print(producto)

# Ejemplo de uso de las clases
catalogo_autopartes = Catalogo()

# Agregar productos al catálogo
producto1 = Producto("Batería de coche", "Accesorios", 120, 2021)
producto2 = Producto("Filtro de aceite", "Repuestos", 15, 2020)
producto3 = Producto("Llantas deportivas", "Accesorios", 300, 2022)

catalogo_autopartes.agregar_producto(producto1)
catalogo_autopartes.agregar_producto(producto2)
catalogo_autopartes.agregar_producto(producto3)

# Mostrar todos los productos en el catálogo
catalogo_autopartes.mostrar_productos()

# Filtrar por año
catalogo_autopartes.filtrar_por_año(2021)

# Filtrar por categoría
catalogo_autopartes.filtrar_por_categoria("Accesorios")

'''
Desarrollar un módulo que contenga las siguientes funciones:
● Que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista.
● Mostrar la lista obtenida por pantalla.
● Ordenar los valores de la lista y mostrarla por pantalla.
Luego crea un script main.py en el mismo directorio en el que deberás importar el módulo y
ejecutar las funciones.
Nota: utilizar el módulo “random” para generar un número aleatorio.
'''
# Se crea un script con nombre mimodulo.py

import random

def generar_numeros_aleatorios(cantidad=20, rango=(0, 100)):
    return [random.randint(rango[0], rango[1]) for _ in range(cantidad)]

def mostrar_lista(lista):
    print("Lista generada:", lista)

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)

#Creamos otro script en el mismo escritorio de nombre main.py

# main.py

#Hacemos un llamado a mimodulo, previamente creado
from mimodulo import generar_numeros_aleatorios, mostrar_lista, ordenar_y_mostrar

lista_aleatoria = generar_numeros_aleatorios()
mostrar_lista(lista_aleatoria)
ordenar_y_mostrar(lista_aleatoria)

'''
Problema 9
'''
#Al igual que el ejercicio anterior creamos un script de nombre operaciones.py
# operaciones.py

def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido en la suma."

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido en la resta."

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido en el producto."

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("No es posible dividir entre cero.")
        resultado = a / b
        return resultado
    except (TypeError, ZeroDivisionError) as e:
        return f"Error: {str(e)}"

#Luego creamos un script de nombre calculos.py

from operaciones import suma, resta, producto, division #Llamamos al módulo operaciones

a = float(input("Insterte el primer valor: "))
b = float(input("Insterte el segundo valor: "))

# Suma
resultado_suma = suma(a, b)
print(f"Suma: {resultado_suma}")

# Resta
resultado_resta = resta(a, b)
print(f"Resta: {resultado_resta}")

# Producto
resultado_producto = producto(a, b)
print(f"Producto: {resultado_producto}")

# División
resultado_division = division(a, b)
print(f"División: {resultado_division}")

'''
Problema 10
'''
#Extraemos solo la clase CIRCULO y creamos un module circulo_module.py
import math 

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area

#Extraemos solo la clase RECTANGULO y creamos un module rectangulo_module.py
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area
#Editamos nuestar carpeta main.py del ejercicio anterior
#main.py
# main.py

from circulo_module import CIRCULO
from rectangulo_module import RECTANGULO

def calcular_area_circulo():
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        mi_circulo = CIRCULO(radio)
        area_circulo = mi_circulo.calcular_area()
        print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")
    except ValueError:
        print("Error: Ingrese un valor numérico para el radio del círculo.")

def calcular_area_rectangulo():
    try:
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        mi_rectangulo = RECTANGULO(largo, ancho)
        area_rectangulo = mi_rectangulo.calcular_area()
        print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area_rectangulo:.2f}")
    except ValueError:
        print("Error: Ingrese valores numéricos para el largo y el ancho del rectángulo.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            calcular_area_circulo()
        elif opcion == "2":
            calcular_area_rectangulo()
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()