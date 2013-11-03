# -*- coding: utf-8 -*-

import random


class GeneticOptimization:

    def __init__(self, costf, domain, psize=50, step=1, mutprob=0.2, elite=0.2):
        """
            Keyword arguments:
                domain -- list of tuple (min, max)

        """
        self.costf = costf
        self.domain = domain
        self.step = step
        self.psize = psize
        self.mutprob = mutprob
        self.elite = elite
        self.population = self.__make_population()

    def __iter__(self):
        return self

    def next(self):
        """
            generate next generaion. using mutate and crossover method.
        """
        scores = [(self.costf(v), v) for v in self.population]
        scores.sort()
        ranked = [v for (s, v) in scores]

        topelite = int(self.elite * self.psize)
        population = ranked[:topelite]

        while len(population) < self.psize:
            if random.random() < self.mutprob:
                c = random.randint(0, topelite)
                population.append(self.__mutate(ranked[c]))
            else:
                c1 = random.randint(0, topelite)
                c2 = random.randint(0, topelite)
                population.append(self.__crossover(ranked[c1], ranked[c2]))

        self.population = population
        self.score = scores[0]

    def __make_population(self):
        """
            make new vectors in domain.

            Returns: list of list. initial population.
        """
        population = list()
        for i in range(self.psize):
            vec = [random.randint(self.domain[j][0], self.domain[j][1])
                    for j in range(len(self.domain))]
            population.append(vec)
        return population

    def __mutate(self, vec):
        """
            element of arg vector updates +step or -step.

            Keyword arguments:
                vec -- list of Number

            Returns: list of next generation
        """
        i = random.randint(0, len(self.domain) - 1)
        if random.random() < 0.5 and vec[i] > self.domain[i][0]:
            return vec[:i] + [vec[i] - self.step] + vec[i+1:]
        elif vec[i] < self.domain[i][1]:
            return vec[:i] + [vec[i] + self.step] + vec[i+1:]
        else:
            return vec

    def __crossover(self, vec1, vec2):
        """
            element of arg vectors merged

            Keyword arguments:
                vec1, vec2 -- list of Number

            Returns: list of next generation
        """
        i = random.randint(1, len(self.domain) - 2)
        return vec1[:i] + vec2[i:]
