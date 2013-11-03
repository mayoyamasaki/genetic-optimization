# -*- coding: utf-8 -*-

import unittest
from libs.genetic_optimization import *


class GeneticOptimizationTest(unittest.TestCase):

    def setUp(self):
        self.domain = [(1, 255), (1, 255), (1, 255), (100, 150)]
        self.psize = 30
        self.step = 3
        self.go = GeneticOptimization(self.domain,
                                      psize=self.psize,
                                      step=self.step)

    def test_make_population(self):
        population = self.go._GeneticOptimization__make_population()

        isContainAll = []
        for i in range(self.psize):
            isContain = all(filter(lambda ((l, u), x): x in range(l, u + 1),
                                   zip(self.domain, population[i])))
            isContainAll.append(isContain)

        self.assertTrue(all(isContainAll))
        self.assertEqual(len(population), self.psize)


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
