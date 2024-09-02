#FAR VEDERE AL PROF IL PROBLEMA

import unittest
from film import Film
from movie_genere import Commedia, Drama, Azione
from noleggio import Noleggio

class TestFilm(unittest.TestCase):
    def setUp(self):
        self.film_azione1 = Azione(1, "Azione 1")
        self.film_azione2 = Azione(2, "Azione 2")
        self.film_azione3 = Azione(3, "Azione 3")
        self.film_azione4 = Azione(4, "Azione 4")
        self.film_azione5 = Azione(5, "Azione 5")
        self.film_commedia1 = Commedia(1, "Commedia 1")
        self.film_commedia2 = Commedia(2, "Commedia 2")
        self.film_commedia3 = Commedia(3, "Commedia 3")
        self.film_commedia4 = Commedia(4, "Commedia 4")
        self.film_drama1 = Drama(1, "Drama 1")

        self.film_list = [self.film_drama1, self.film_azione1, self.film_azione2, self.film_azione3, self.film_azione4, self.film_azione5, self.film_commedia1, self.film_commedia2, self.film_commedia3, self.film_commedia4]

        self.noleggio = Noleggio(self.film_list)

    def test_isAvaiable(self):
        self.assertTrue(self.noleggio.isAvaiable(self.film_azione1))
        self.noleggio.rentAMovie(self.film_azione1, 100)
        self.assertTrue(self.noleggio.isAvaiable(self.film_azione1))
'''
    def test_rentAMovie(self):
        self.noleggio.rentAMovie(self.film_azione2, 101)
        self.assertTrue(self.noleggio.isAvaiable(self.film_azione2))
        self.assertIn(self.film_azine2, self.noleggio.rented_film[101])

    def test_rentUnavailableMovie(self):
        self.noleggio.rentAMovie(self.film_azione3, 102)
        self.noleggio.rentAMovie(self.film_azione3, 103)
        self.assertNotIn(self.film_azione3, self.noleggio.rented_film[103])

    def test_giveBack(self):
        self.noleggio.rentAMovie(self.film_azione4, 104)
        self.noleggio.giveBack(self.film_azione4, 104, 3)
        self.assertTrue(self.noleggio.isAvaiable(self.film_azione4))
        self.assertNotIn(self.film_azione4, self.noleggio.rented_film[104])
    
    def test_calcolaPenaleRitardo(self):
        self.assertEqual(self.film_azione5.calcolaPenaleRitardo(2), 6.0)
        self.assertEqual(self.film_commedia1.calcolaPenaleRitardo(2), 5.0)
        self.assertEqual(self.film_drama1.calcolaPenaleRitardo(2), 4.0)

    def test_printMovies(self):
        self.noleggio.printMovies()

    def test_printRentMovies(self):
        self.noleggio.rentAMovie(self.film_commedia2, 105)
        self.noleggio.rentAMovie(self.film_commedia3, 105)
        self.noleggio.printRentMovies(105)
'''
if __name__ == "__main__":
    unittest.main()