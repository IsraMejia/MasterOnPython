class Persona():
    def __init__(self, nombre : str, edad :int):
        self.nombre = nombre
        self.__edad = edad
    
    def get_datos(self): 
    #def __get_datos(self): #__ <- hace el metodo privado, impidiendo hacer la sobre carga
        return "Nombre : " + self.nombre + "Edad : " + str(self.__edad)

    def getEdad(self):
        return self.__edad

class Empleado(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.calificacion = "*"
    
    def get_datos(self):
        return "Nombre : " + self.nombre + "Edad : " + str(self.getEdad()) + " Tiene la calificacion: " + self.calificacion
        #Hemos realizado la sobre carga de metodo, al sobre modificar el metodo que hereda, para poder 
        #hacer esa misma tarea, pero de la forma en especifico que se necesita hacer en la clase hija

def main():
    Pepe = Persona("Pepe", 55)
    print(Pepe.get_datos())
    Juan = Empleado("Juan", 34)
    print(Juan.get_datos())

    print(Pepe.__str__)
    print(Juan.__str__)

    print(f"Comparando: \n\t {Pepe.nombre.__eq__(Juan.nombre)}")

    print(Pepe.__sizeof__)
    print(Juan.__sizeof__)

    print(f"Comparando: \n\t {Pepe.getEdad().__le__(Juan.getEdad())}")
    #Comparamos atributos privados
main()