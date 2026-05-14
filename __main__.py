from models.golpes_repository import Golpe_repository
from models.pokemon_repository import PokemonRepository

golpe_repo = Golpe_repository()
pokemon_repo = PokemonRepository(golpe_repo)

pokemon = pokemon_repo.get_by_id(1)
print(pokemon)