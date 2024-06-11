from unittest import TestCase
from rosalind.sequence import *
import tempfile


# Create temporary file to test functions which read multifasta:
tp = tempfile.NamedTemporaryFile()
tp.write(b'''>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT''')
tp.flush()


# Tests for rosalind.sequence module

class Test(TestCase):
    def test_reverse_complement(self):
        self.assertEqual(reverse_complement('ATGC'), 'GCAT')

    def test_translate(self):
        self.assertEqual(translate('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'),
                         'MAMAPRTEINSTRING')

    def test_splice_translate(self):
        self.assertEqual(splice_translate(tp.name), 'MVYIADKQHVASREAYGHMFKVCA')

    def test_hamming_distance(self):
        self.assertEqual(hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'), 7)

    def test_find_motif(self):
        self.assertEqual(find_motif('GATATATGCATATACTT', 'ATAT'), [2, 4, 10])

    def test_all_common_substrings(self):
        self.assertEqual(all_common_substrings('ATGCTG', 'GCTTGAC'),
                         {'A', 'AC', 'C', 'CT', 'CTT', 'GA', 'T', 'TG', 'TGA', 'TT'})

    def test_longest_common_substring(self):
        self.assertEqual(longest_common_substring(tp.name), 'TCGGTCGAA')
