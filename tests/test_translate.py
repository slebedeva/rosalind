from unittest import TestCase
from rosalind.sequence import translate


class Test(TestCase):
    def test_translate(self):
        self.assertEqual(translate('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'),
                         'MAMAPRTEINSTRING')
