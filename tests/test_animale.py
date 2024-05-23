import unittest
from app.lib.biblioteca_animale import culoare_Camila, descriere_Camila

class TestBiblioteca(unittest.TestCase):

    def test_culoare_Camila(self):
        self.assertEqual(culoare_Camila(), "Camila are dungi portocalii și negre.")

    def test_descriere_Camila(self):
        self.assertEqual(descriere_Camila(), "Camila este un mamifer carnivor din familia felidelor, fiind cel mai mare dintre felinele sălbatice.")

if __name__ == '__main__':
    unittest.main()

