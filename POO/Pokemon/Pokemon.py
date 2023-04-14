"""
Contexte : 
Vous connaissez certainement tous ces petites bêtes toute mignonnes (ou pas pour certaines)
Ces petites créatures sont dressées par des "dresseurs de pokemons" et sont amenées à combattre entre elles.
Et bien, nous allons aussi les faire combattre !
Les Pokémon sont certes de très mignonnes créatures, mais ils sont également un bon exemple pour illustrer l’héritage. 

Je vous propose de commencer par créer une classe "Pokemon" qui contient les champs suivants : 
    ▪ un attribut nom qui représente le nom du Pokémon.
    ▪ un attribut hp (pour Health Points) qui représente les points de vie du Pokémon.
    ▪ un attribut qui s’appelle atk qui représente la force de base de l’attaque du Pokémon.
    ▪ un constructeur pour instancier des Pokémon adéquatement.
    ▪ une méthode isDead() qui retourne un boolean pour indiquer si un Pokémon est mort (hp == 0) ou non.

Créez une méthode "attaquer(Pokemon p)" qui permet au Pokémon appelant d’attaquer le Pokémon passé en paramètre. 
L’attaque déduit atk points de la vie hp du Pokémon attaqué p.
Redéfinissez la méthode toString() qui va nous permettre d'afficher  les informations du Pokémon.

En plus des Pokémon dit "normaux" (décrits à travers la classe Pokemon), on ressence trois types de Pokémon :
    ▪ Les Pokémon de type Feu
    ▪ Les Pokémon de type Eau
    ▪ Les Pokémon de type Plante 
(en réalité il existe 17 types en tout mais on ne va pas s’amuser à tous les coder)

les Pokémon de type Feu sont super efficaces contre les Pokémon de type Plante et leur infligent deux fois plus de dégâts (2*atk). 
Par contre, ils sont très peu efficaces contre les Pokémon de type Eau ou de type Feu et ne leur infligent que la moitié des dégâts (0.5*atk). 
Ils infligent des dégâts normaux aux Pokémon de type Normal.

les Pokémon de type Eau sont super efficaces contre les Pokémon de type Feu et leur infligent deux fois plus de dégâts (2*atk). 
Par contre, ils sont très peu efficaces contre les Pokémon de type Eau ou de type Plante et ne leur infligent que la moitié des dégâts (0.5*atk). 
Ils infligent des dégâts normaux aux Pokémon de type Normal.

les Pokémon de type Plante sont super efficaces contre les Pokémon de type Eau et leur infligent deux fois plus de dégâts (2*atk). 
Par contre, ils sont très peu efficaces contre les Pokémon de type Plante ou de type Feu et ne leur infligent que la moitié des dégâts (0.5*atk). 
Ils infligent des dégâts normaux aux Pokémon de type Normal.

Créez trois classes : 
    ▪ PokemonFeu
    ▪ PokemonEau
    ▪ PokemonPlante
Ces classes héritent de la classe Pokemon et qui représentent les trois types de Pokémon 
susmentionnés. 
Ensuite, amusez-vous à faire des combats de Pokémon.

"""
class Pokemon: #classe mère
    def __init__(self, nom, hp, atk, type = "normal"): #constructeur de la classe mère Pokemon qui prend en paramètre le nom, les points de vie, l'attaque et le type du pokemon
        self.nom = nom
        self.hp = hp
        self.atk = atk
        self.type = type

    def isDead(self): #méthode qui retourne un boolean pour indiquer si un Pokémon est mort (hp == 0) ou non.
        if self.hp == 0:
            return True
        else:
            return False
        
    def attaquer(self, poke): #méthode qui permet au Pokémon appelant d’attaquer le Pokémon passé en paramètre. L’attaque déduit atk points de la vie hp du Pokémon attaqué poke.
        if (self.type == "eau" and poke.type == "feu") or (self.type == "feu" and poke.type == "plante") or (self.type == "plante" and poke.type == "eau") : #si le type du pokemon est eau et que le type du pokemon attaqué est feu ou si le type du pokemon est feu et que le type du pokemon attaqué est plante ou si le type du pokemon est plante et que le type du pokemon attaqué est eau
            mult = 2 #alors le pokemon attaquant fait des dégats super efficace
            print("c'est super efficace !")
        elif (self.type == "normal" or poke.type == "normal"): #sinon si le type du pokemon est normal ou si le type du pokemon attaqué est normal
            multi = 1 #alors le pokemon attaquant fait des dégats normaux
        else:
            mult = .5 #sinon le pokemon attaquant fait des dégats très peu efficace
            print("ce n'est pas très efficace")
        poke.hp -= self.atk * mult #on retire les dégats au pokemon attaqué en multipliant l'attaque du pokemon attaquant par le multiplicateur
        return poke.hp #on retourne les points de vie du pokemon attaqué
    
    def combat(self, poke): #méthode qui permet de faire combattre deux pokemons
        while self.hp > 0 and poke.hp > 0: #tant que les points de vie des deux pokemons sont supérieurs à 0
            self.attaquer(poke) #le pokemon attaquant attaque le pokemon attaqué
            poke.attaquer(self) #le pokemon attaqué attaque le pokemon attaquant
            print(f"{self.nom} a {self.hp} HP") #on affiche les points de vie des deux pokemons
            print(f"{poke.nom} a {poke.hp} HP") #on affiche les points de vie des deux pokemons
        if self.hp <= 0: #si les points de vie du pokemon attaquant sont inférieurs ou égaux à 0
            print(f"{self.nom} est mort") #alors le pokemon attaquant est mort
        else:
            print(f"{poke.nom} est mort") #sinon le pokemon attaqué est mort
            
    def __str__(self):
        return f"Nom: {self.nom} HP: {self.hp} ATK: {self.atk}"
    