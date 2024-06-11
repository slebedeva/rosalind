from unittest import TestCase
from rosalind.utils import *

class Test(TestCase):
    def test_gc(self):
        self.assertAlmostEqual(gc('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'),
                               0.6091954022988506)
