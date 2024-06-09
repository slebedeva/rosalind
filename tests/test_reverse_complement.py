from unittest import TestCase

from rosalind.sequence import reverse_complement


class Test(TestCase):
    def test_reverse_complement(self):
        self.assertEqual(reverse_complement('ATGC'), 'GCAT')
