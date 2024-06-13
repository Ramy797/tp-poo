class Producto:
    def __init__(self,nombre,precio,cantidad): #LLamo al constructor y defino los atributos 
        #inicializacion de los atributos
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def getNombre (self):   #Con este metodo obtengo el nombre 
        return self.nombre
    
    def getPrecio(self):   #Con este metodo obtengo el precio
        return self.precio
    
    def getCantidad(self):   #Con este metodo obtengo la cantidad 
        return self.cantidad
    
    def mostrar_informacion_producto(self): #Este metodo muestr el print que va a ver el usuario
       print ("\nLos datos de su producto son: " + "\n" +"\nNombre: "+ str(self.getNombre()) + "\n" +"\nPrecio: "+ str(self.getPrecio()) + "\n" +"\nCantidad: "+ str(self.getCantidad())) #estructura para el print