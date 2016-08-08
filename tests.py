from main import Bowling
import unittest


class TestMain(unittest.TestCase):
    def setUp(self):
        self.jeu = Bowling()

    def test_deux_lances_a_zero_equal_zero(self):
        score = self.jeu.tour(0, 0)
        self.assertEqual(score, 0)


    def test_deux_lancers_a_trois_equal_six(self):
        score = self.jeu.tour(3, 3)
        self.assertEqual(score, 6)

    def test_jouer_deux_tours_additionne_les_scores(self):
        self.jeu.tour(5, 4)
        score = self.jeu.tour(3, 0)
        self.assertEqual(score, 12)

    def test_jouer_un_spare_puis_3_equal_16(self):
        self.jeu.tour(5,5)
        score = self.jeu.tour(3,0)
        self.assertEqual(score, 16)




if __name__ == '__main__':
    unittest.main()
