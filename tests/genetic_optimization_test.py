# -*- coding: utf-8 -*-

import unittest
from libs.genetic_optimization import *


class GeneticOptimizationTest(unittest.TestCase):

    def setUp(self):
        self.domain = [(1, 255), (1, 255), (1, 255), (100, 150)]
        self.step = 3
        self.go = GeneticOptimization(self.domain,
                                      self.step)

    def test_mutate(self):
        current = len(self.domain) * [1]
        real = self.go._GeneticOptimization__mutate(current)

        self.assertTrue(abs(sum(real) - sum(current)) == self.step)


if __name__ == '__main__':
    unittest.main()
