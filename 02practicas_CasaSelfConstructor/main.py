
class Juguete():
    def __init__(self,nombre,precio = 0.0):
        self.nombre = nombre
        self.precio = precio
        self.color = ""

videojuego = Juguete("Super Juego")

videojuego.precio = 13.49
print("nombre : " + videojuego.nombre + " " + " precio : " + 
      str(videojuego.precio))
  
