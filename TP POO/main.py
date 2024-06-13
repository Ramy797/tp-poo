from alimento import Alimento #importo la clase Alimento del archivo alimento.py
from producto import Producto #importo la clase Producto del arcihvo Producto.py
from electronico import Electronico #importo la clase Electronico del archivo electronico.py


a= Electronico("iphone 15",1200000,7,"Apple","pro max") #doy los valores a los atributos
a.mostrar_informacion_electronico()#se muestra la info


b= Producto("Cargador generico", 20000, 100) #doy valores a los atributos
b.mostrar_informacion_producto()#se muestra la información


c= Alimento("Brownie",1800,8,"15/8/2024") #doy valores a los atributos
c.mostrar_informacion_alimento()#se muestra la información 