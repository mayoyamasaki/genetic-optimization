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

        self.assertEqual(abs(sum(real) - sum(current)), self.step)

    def test_crossover(self):
        cur1 = range(1, 6)  # 1 to 5
        cur2 = range(6, 11)  # 6 to 10
        real = self.go._GeneticOptimization__crossover(cur1, cur2)

        isContain = all(filter(lambda x: x in set(cur1) | set(cur2), real))
        self.assertTrue(isContain)


if __name__ == '__main__':
    unittest.main()
