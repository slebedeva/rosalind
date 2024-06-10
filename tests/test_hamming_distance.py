from rosalind.sequence import hamming_distance
from unittest import TestCase


class Test(TestCase):
    def test_hamming_distance(self):
        self.assertEqual(hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'), 7)
