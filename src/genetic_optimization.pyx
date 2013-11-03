# -*- coding: utf-8 -*-

import random


class GeneticOptimization:

    def __init__(self, domain, step=1):
        """
            Keyword arguments:
                domain -- list of tuple (min, max)

        """
        self.domain = domain
        self.step = step

    def __mutate(self, vec):
        """
            element of arg vector updates +step or -step.

            Keyword arguments:
                vec -- list of Number

            Returns: list of next generation
        """
        i = random.randint(0, len(self.domain) - 1)
        if random.random() < 0.5 and vec[i] > self.domain[i][0]:
            return vec[0:i] + [vec[i] - self.step] + vec[i+1:]
        elif vec[i] < self.domain[i][1]:
            return vec[0:i] + [vec[i] + self.step] + vec[i+1:]

