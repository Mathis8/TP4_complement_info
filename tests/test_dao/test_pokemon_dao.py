from unittest import TestCase
from business_object.pokemon.abstract_pokemon import AbstractPokemon

from dao.pokemon_dao import PokemonDao


pokemon_dao = PokemonDao()
class TestPokemonDao(TestCase):

    def test_find_all_pokemon(self):
        # GIVEN
        
        # WHEN
        pokemons = pokemon_dao.find_all()

        # THEN
        self.assertEqual(100, len(pokemons))
        self.assertIsInstance(pokemons[1], AbstractPokemon)

    def test_find_pokemon_by_name(self):
        # GIVEN
        pokemon_name="Pikachu"
        # WHEN
        pokemon = pokemon_dao.find_pokemon_by_name(pokemon_name)

        # THEN
        self.assertEqual(pokemon_name, pokemon.name)
        self.assertIsNotNone(pokemon.common_attacks)