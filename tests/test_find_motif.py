from unittest import TestCase
from rosalind.sequence import find_motif


class Test(TestCase):
    def test_find_motif(self):
        self.assertEqual(find_motif('GATATATGCATATACTT', 'ATAT'), [2, 4, 10])
