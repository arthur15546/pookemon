from pokemon import Pokemon

class Batalha():
    def __init__(self, pkm1, pkm2):
        self._pkm1 = pkm1
        self._pkm2 = pkm2
        self.primeiro = None

    @property
    def pkm1(self):
        return self._pkm1
    
    @property
    def pkm2(self):
        return self._pkm2
    
    @pkm1.setter
    def pkm1(self, pokemon):
        if isinstance(pokemon, Pokemon):
            self._pkm1 = pokemon
        else:
            raise TypeError("não é um pokemon valido")
    
    @pkm2.setter
    def pkm1(self, pokemon):
        if isinstance(pokemon, Pokemon):
            self._pkm2 = pokemon
        else:
            raise TypeError("não é um pokemon valido")
    