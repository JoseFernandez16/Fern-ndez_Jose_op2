import pyttsx3
import speech_recognition 
import time

listaEstudiantes = []

class Estudiantes(object):
    def __init__(self, codigo, nombre, apellido, edad, nota1, nota2, nota3):
        self.Codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.notaFinal = (nota1 + nota2 + nota3) / 3
        self.notaFinal = round(self.notaFinal,3)
        
    def entregarDatos(self):
        print(f"El estudiante {self.nombre} con código {self.Codigo} tiene:\n nota1={self.nota1}\n nota2={self.nota2}\n nota3={self.nota3}\n promedio={self.notaFinal}")
    
    def editarNotas(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.notaFinal = (nota1 + nota2 + nota3) / 3
        print("Las notas fueron modificadas exitosamente!")

def procesamientoVoz():
    reco = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        cod= reco.listen(source)
    time.sleep(1)
    val=(reco.recognize_google(cod,language="es"))
    return val

def registrarEstudiante():#Creación de un Objeto Estudiante
    print("Registro de Estudiantes\n")
    print("Ingrese el código: ")
    codigo = int(procesamientoVoz());print(codigo)
    print("Ingrese el nombre: ")
    nombre = str(procesamientoVoz());print(nombre)
    print("Ingrese el apellido: ")
    apellido = str(procesamientoVoz());print(apellido)
    print("Ingrese su edad: ")
    edad = int(procesamientoVoz());print(edad)
    print("Ingrese la nota N°1: ")
    nota1 = float(procesamientoVoz());print(nota1)
    print("Ingrese la nota N°2: ")
    nota2 = float(procesamientoVoz());print(nota2)
    print("Ingrese la nota N°3: ")
    nota3 = float(procesamientoVoz());print(nota3)
    alumno = Estudiantes(codigo, nombre, apellido, edad, nota1, nota2, nota3)
    listaEstudiantes.append(alumno)
    engine=pyttsx3.init()
    engine.say(f"El estudiante {nombre} ha sido creado")
    print(f"El estudiante {nombre} ha sido creado")
    engine.runAndWait()
    time.sleep(1)

def buscarEstudiante():
    print("Buscador de Estudiantes\n")
    print("Ingrese el código del estudiante que desea buscar: ")
    codigo=int(procesamientoVoz())
    print("El estudiante buscado es el siguiente:")
    for objAlumno in listaEstudiantes:
        if codigo == objAlumno.Codigo:
            objAlumno.entregarDatos()
    time.sleep(1)
            
def mostrarEstudiantes():
    print("Lista de Estudiantes\n")
    for objAlumno in listaEstudiantes:
        objAlumno.entregarDatos()
        print("-----------------------------------------")
    time.sleep(1)

def modificarNotas():
    print("Modificación de Notas de Estudiantes\n")
    print("Ingrese el código del estudiante")
    cod = int(procesamientoVoz())
    for objAlumno in listaEstudiantes:
        if cod == objAlumno.Codigo:
            print("Ingrese los valores de las nuevas notas")
            nota1 = float(procesamientoVoz());print(nota1)
            nota2 = float(procesamientoVoz());print(nota2)
            nota3 = float(procesamientoVoz());print(nota3) 
            objAlumno.editarNotas(nota1, nota2, nota3)
            objAlumno.entregarDatos()
            print(f"Las notas nuevas notas son:\n nota1={nota1}\n nota2={nota2}\n nota3={nota3}\n")
            print("Los cambios fueron guardados exitosamente!!")
            engine=pyttsx3.init()
            engine.say("Los cambios fueron guardados exitosamente!!")
            engine.runAndWait()
    time.sleep(1)
           
def salir():
    print("Se ha finalizado el sistema.!")
    engine=pyttsx3.init()
    engine.say("Se ha finalizado el sistema.!")
    engine.runAndWait()
    exit()

def Principal():
    engine=pyttsx3.init()
    engine.say("Bienvenido al Menú de Inicio, Por favor seleccione una opción")
    engine.runAndWait()
    print("Bienvenido al Menú de Inicio, Por favor seleccione una opción")
    print("\n")
    print("Seleccione una de las siguientes opciones:");
    print("1.- Registrar Estudiante")
    print("2.- Listado de Estudiantes")
    print("3.- Buscar Estudiante")
    print("4.- Modificar notas")
    print("5.- Cerrar Programa\n")

    while True:
        print("Ingrese la opción deseada")
        opcion=str(procesamientoVoz())
        opcion.lower()
        if opcion == "opción 1":
            registrarEstudiante()
        elif opcion == "opción 2":
            mostrarEstudiantes()
        elif opcion == "opción 3":
            buscarEstudiante()
        elif opcion == "opción 4":
            modificarNotas()
        elif opcion == "opción 5":
            salir()  
        else:
           print("La opcion es incorrecta, Intente nuevamente.")
           engine=pyttsx3.init()
           engine.say("La opcion es incorrecta, Intente nuevamente.")
           engine.runAndWait()
            
if __name__ == "__main__":
    Principal();