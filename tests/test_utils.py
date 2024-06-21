from unittest import TestCase
from rosalind.utils import *

class Test(TestCase):
    def test_gc(self):
        self.assertAlmostEqual(gc('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'),
                               0.6091954022988506)

    def test_mw(self):
        self.assertAlmostEqual(calculate_mw("SKADYEK"), 821.392, places = 2)
