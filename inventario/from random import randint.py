from random import randint

class Pokemon:
    def __init__(self, nombre:str, tipo:str):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = randint(1,100)
        self.ataque = randint(1,100)
        self.defensa = randint(1,100)

class Entrenador:
    def __init__(self, nombre, pokemon):
        self.nombre = nombre
        self.pokemon = pokemon

class Batalla:
    def __init__(self):
        p1 = Pokemon("Pikachu", "Electrico")
        p2 = Pokemon("Capibara", "Charco")
        self.entrenador1 = Entrenador("Ash", p1)
        self.entrenador2 = Entrenador("Jaimito",p2)
        self.ganador = None
        self.perdedor = None

    def luchar(self):
        while self.entrenador1.pokemon.vida > 0 and self.entrenador2.pokemon.vida > 0:
            #Entrenador 2 Ataque primero
            
            golpe = self.entrenador2.pokemon.ataque - self.entrenador1.pokemon.defensa
            if golpe <= 0: golpe = 1
            self.entrenador1.pokemon.vida -= golpe

            if self.entrenador1.pokemon.vida <= 0:
                self.ganador = self.entrenador2
                self.perdedor = self.entrenador1

            #Entranador1 Ataque
            golpe = self.entrenador1.pokemon.ataque - self.entrenador2.pokemon.defensa
            if golpe <= 0: golpe = 1
            self.entrenador2.pokemon.vida -= golpe

            if self.entrenador2.pokemon.vida <= 0:
                self.ganador = self.entrenador1
                self.perdedor = self.entrenador2

    def mostrar_ganador(self):
        print("El ganador es: ", self.ganador.nombre)
        print(f"Gano con el pokemon: {self.ganador.pokemon.nombre}, estadisticas:\n Ataque: {self.ganador.pokemon.ataque} \n Vida: {self.ganador.pokemon.vida}\n Defensa: {self.ganador.pokemon.defensa}" )
        print(f"{self.perdedor.nombre} le tiene que pagar una arepa a {self.ganador.nombre}")

def main():
    batalla = Batalla()
    batalla.luchar()
    batalla.mostrar_ganador()

main()