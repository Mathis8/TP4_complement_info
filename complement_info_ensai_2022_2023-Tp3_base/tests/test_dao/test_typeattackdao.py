from dao.db_connection import DBConnection
from unittest import TestCase
from dao.typeattackdao import TypeAttackDao
from dao.attaquedao import AttaqueDao

class TestDao(TestCase) :
    def test_find_by_id(self) :
        type_attack = "physical attack"
        test = TypeAttackDao()
        res = test.find_id_by_label(type_attack)
        self.assertEqual(2, res)

    def test_find_all(self) :
        test = TypeAttackDao()
        res = test.find_all() 
        self.assertEqual([[1, 'fixed damage'], [2, 'physical attack'], [3, 'special attack']], res)

    def test_find_all_attack(self) :
        test = AttaqueDao()
        res = test.find_all_attack(10, 3)
        self.assertEqual(len(res), 10)
        self.assertEqual(res[0]["id_attack"], 4)