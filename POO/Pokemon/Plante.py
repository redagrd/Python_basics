from Pokemon import Pokemon

class PokemonPlante(Pokemon):
    def __init__(self, nom, hp, atk):
        super().__init__(nom, hp, atk, "plante") 