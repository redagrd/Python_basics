from Pokemon import Pokemon

class PokemonFeu(Pokemon):
    def __init__(self, nom, hp, atk):
        super().__init__(nom, hp, atk, "feu")