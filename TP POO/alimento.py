from producto import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):   #llamo al constructor y defino los atributos
        super().__init__(nombre, precio, cantidad) #se heredan los atributos de la clase Producto
        self.fecha_expiracion = fecha_expiracion # inicializacion del atributo 

    def get_fecha_expiracion(self):   #Con este metodo se obtiene la fecha de caducidad    
        return self.fecha_expiracion
    
    def mostrar_informacion_alimento(self): #Con este metodo se muestra el print
       print ("\nLos datos de su producto son: " + "\n" +"\nNombre: "+ str(self.getNombre()) + "\n" +"\nPrecio: "+ str(self.getPrecio()) + "\n" +"\nCantidad: "+ str(self.getCantidad()) + "\n" + "\nFecha de expiración: " + str(self.get_fecha_expiracion())) 