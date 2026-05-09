from models.pokemon import Pokemon
import csv

class PokemonRepository():
    def __init__(self, golpe_repositorio):
        self.golpe_repo = golpe_repositorio
        self._pokemons = self._carregar()

    def _carregar(self):
        with open("./data/pokemons.csv", mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            linha_pokemons = list(leitor)
        
        with open("./data/pokemon_golpes.csv", mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            linha_golpes = list(leitor)
        lista_pokemon = []
        for pokemon in linha_pokemons:
            pkm_id = int(pokemon["#"])
            pkm_nome = pokemon["nome"]
            pkm_hp = int(pokemon["hp"])
            pkm_tipo1 = pokemon["tipo1"]
            pkm_tipo2 = pokemon["tipo2"]
            pkm_velocidade = int(pokemon["velocidade"])
            golpes = []

            golpes_id = []
            for golpe in linha_golpes:
                if int(golpe["pokemon_id"]) == pkm_id:
                    golpes_id.append(golpe["golpe_id"])
            
            for id in golpes_id:
                golpes.append(self.golpe_repo.get_by_id(id))
            
            objeto = Pokemon(pkm_id, pkm_nome, pkm_hp, pkm_tipo1, pkm_tipo2, pkm_velocidade, golpes)
            lista_pokemon.append(objeto)
            
        return lista_pokemon

    def get_by_id(self, id):
        for pokemon in self._pokemons:
            if pokemon.id == id:
                return pokemon
            
        raise ValueError("id não valido")
