import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
from main import difficulty_select, intro, lob_grenades,call_airstrike,counter_attack

log_file_name = "game-test.txt"
class testApp(unittest.TestCase):
    def testDifficultySelect(self):
        global test_game_one 
        test_game_one = difficulty_select(log_file_name,"initiate")
        self.assertEqual(test_game_one.marine_count, 25, "Incorrect count")

        global test_game_two 
        test_game_two = difficulty_select(log_file_name,"astartes")
        self.assertEqual(test_game_two.marine_count, 20, "Incorrect count")

        global test_game_three
        test_game_three = difficulty_select(log_file_name,"custodes")
        self.assertEqual(test_game_three.marine_count, 15, "Incorrect count")

    # def testIntro(self):
    #     # intro(test_game_one, log_file_name, "grenades")
    #     # self.assertEqual(test_game_one.marine_count, 15, "Incorrect count")

    #     # intro(test_game_two, log_file_name, "grenades")
    #     # self.assertEqual(test_game_two.marine_count, 10, "Incorrect count")

    #     # intro(test_game_three, log_file_name, "airstrike")
    #     # self.assertEqual(test_game_three.marine_count, 12, "Incorrect count")

    # def testSecondDecision(self):
    #     lob_grenades(test_game_one, log_file_name, "defend")
    #     self.assertEqual(test_game_one.marine_count, 8, "Incorrect count")

    #     # lob_grenades(test_game_two, log_file_name, "attack")
    #     # self.assertEqual(test_game_two.marine_count, 7, "Incorrect count")

    #     # call_airstrike(test_game_three, log_file_name, "attack")
    #     # self.assertEqual(test_game_three.marine_count, 9, "Incorrect count")

    # def testThirdDecision(self):
    #     counter_attack(test_game_one,log_file_name, "carnifex")
    #     self.assertEqual(test_game_one.marine_count, 2, "Incorrect count")

    #     # counter_attack(test_game_two,log_file_name, "tyrant")
    #     # self.assertEqual(test_game_two.marine_count, 4, "Incorrect count")

    #     # counter_attack(test_game_three,log_file_name, "tyrant")
    #     # self.assertEqual(test_game_three.marine_count, 6, "Incorrect count")

unittest.main()