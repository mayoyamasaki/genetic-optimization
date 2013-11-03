# -*- coding:utf-8 -*-

import random
import math
from libs.genetic_optimization import *


class DistributeBook(object):

    def __init__(self, books, prefs):
        self.books = books
        self.prefs = prefs
        self.domain = [(0, (len(self.books) * 2) -i -1)
                        for i in range(len(self.books) * 2)]

    def dormcost(self, vec):
        cost = 0
        slots = []
        for i in range(len(self.books)): slots += [i, i]

        for i in range(len(vec)):
            x = int(vec[i])
            book = self.books[slots[x]]
            pref = self.prefs[i][1]

            if pref[0] == book: cost += 0
            elif pref[1] == book: cost += 1
            else: cost += 3
            del slots[x]
        return cost

    def printsolution(self, vec):
        slots = []
        for i in range(len(self.books)): slots += [i, i]

        for i in range(len(vec)):
            x = int(vec[i])

            book=self.books[slots[x]]
            print "{}\t{}".format(self.prefs[i][0], book)
            del slots[x]

    def optimize(self, iter_cnt):
        go = GeneticOptimization(self.dormcost, self.domain)

        for i in range(iter_cnt):
            go.next()
            print go.score

        self.printsolution(go.score[1])

if __name__ == "__main__":

    books = ['Do Androids Dream of Electric Sheep?',
             'Pride and Prejudice and Zombies',
             'Something Wicked This Way Comes',
             "The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy).",
             "I Was Told There'd Be Cake"]

    prefs = [('Alicia',
              ("The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy).",
               'Something Wicked This Way Comes')),
             ('Caesar',
              ('Do Androids Dream of Electric Sheep?',
               "I Was Told There'd Be Cake")),
             ('June',
              ('Pride and Prejudice and Zombies',
               'Do Androids Dream of Electric Sheep?')),
             ('Gaston',
              ('Do Androids Dream of Electric Sheep?',
               "I Was Told There'd Be Cake")),
             ('Edgar',
              ('Pride and Prejudice and Zombies',
               "The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy).")),
             ('Claire',
              ('Something Wicked This Way Comes',
               "I Was Told There'd Be Cake")),
             ('Lana',
              ("I Was Told There'd Be Cake",
               'Pride and Prejudice and Zombies')),
             ('Kevin',
              ("The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy).",
               'Something Wicked This Way Comes')),
             ('Aaron',
              ("The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy).",
               'Something Wicked This Way Comes')),
             ('Nina',
              ('Something Wicked This Way Comes',
               'Pride and Prejudice and Zombies'))]

    eg = DistributeBook(books, prefs)
    eg.optimize(50)



