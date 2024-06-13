from producto import Producto
class Electronico(Producto):
    def __init__(self,nombre,precio,cantidad,marca,modelo): #LLamo al constructor y defino los atributos
        super().__init__(nombre,precio,cantidad) #se heredan los atributos de la clase Producto
        
        self.marca = marca #inicializacion de atributos
        self.modelo = modelo
        

    def getMarca(self):  #con este metodo obtengo la marca   
            return self.marca

    def getModelo(self): #con este metodo obtengo el modelo
            return self.modelo  
    
    def mostrar_informacion_electronico(self): #metodo que muestra el print
       print ("\nLos datos de su producto son: " + "\n" +"\nNombre: "+ str(self.getNombre()) + "\n" +"\nPrecio: "+ str(self.getPrecio()) + "\n" +"\nCantidad: "+ str(self.getCantidad()) + "\n" + "\nMarca:"+ str(self.getMarca())+ "\n" +"\nModelo:" + str(self.getModelo()))