Genetic Algorithm
===

Genetic optimaization using mutation and crossover.


# Build
```
$ python setup.py build_ext --inplace
```

# How to Use
```
# DOMAIN -- list of tuple (min, max)
go = GeneticOptimization(COST_FUNCTION, DOMAIN)

for i in range(ITER_CNT):
    go.next()

# printout (cost value, vector)
print go.score
```

# Example
this example is distribution of the book.

```
$ python src/example.py
(8, [7, 5, 0, 0, 0, 1, 2, 1, 1, 0])
(8, [7, 5, 0, 0, 0, 1, 2, 1, 1, 0])
(8, [7, 5, 0, 0, 0, 1, 2, 1, 1, 0])
(8, [7, 1, 0, 2, 0, 4, 3, 0, 1, 0])
(8, [6, 5, 0, 0, 0, 1, 3, 2, 1, 0])
(7, [7, 1, 0, 0, 0, 1, 2, 1, 1, 0])
(7, [6, 1, 0, 0, 0, 1, 2, 1, 1, 0])
(6, [7, 1, 0, 0, 0, 4, 3, 1, 1, 0])
(6, [6, 1, 0, 0, 0, 4, 3, 1, 1, 0])
(2, [7, 1, 1, 0, 0, 4, 3, 1, 1, 0])
(2, [6, 1, 1, 0, 0, 4, 3, 1, 1, 0])
…
Alicia	Something Wicked This Way Comes
Caesar	Do Androids Dream of Electric Sheep?
June	Pride and Prejudice and Zombies
Gaston	Do Androids Dream of Electric Sheep?
Edgar	Pride and Prejudice and Zombies
Claire	I Was Told There'd Be Cake
Lana	I Was Told There'd Be Cake
Kevin	The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy).
Aaron	The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy).
Nina	Something Wicked This Way Comes
```

# Test
```
$  nosetests tests
```
