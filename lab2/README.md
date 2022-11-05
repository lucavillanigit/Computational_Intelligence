# Set covering with GA

In this repository is present a possible solution for the set covering problem solved with a genetic algorithm.
I wrote this code with my colleague Luca Marcellino.

## Input parameters

In this code we implemented both **crossover and mutation**. For the mutation we used two different probability: 0.3, 0.45.

The set covering is generated for N = [5,10,20,100,1000] and we can find solution, not optimal, for each of this set. 
Moreover we used different kind of **stopping condition** related to the steps, that are a crossover and a possible mutation, that are [10_000,20_000,50_000,100_000]

## Genetic parameters

The problem encoding is a np.array with 0 if we don't take the list and 1 viceversa.

For this code we used both **mutation** and crossover, for mutation we used flip mutation, so if the gene was 1 it will be 0 and viceversa.

Regarding the **crossover** we used the multi-points crossover and specifically 2. So we copy the first part from the first parent until the first cut point, between the two cut points we copy the gens from the second parent, and from the second cut point to the end, again, the first parent.


## Results

The results are also present inside the lab2 folder in two different csv.

|N |Time|Solution Found <br> with mutation = 0.3| Solution Found <br> with mutation = 0.45
|:----:|:----:|:----:|:----:|
5|10000|    5| 5 
5|20000|    5| 5
5|50000|    5| 5
5|100000|   5| 5
10|10000|   10| 10
10|20000|   10| 10
10|50000|   10| 10
10|100000|  10| 10
20|10000|   28| 28
20|20000|   28| 28
20|50000|   28| 28
20|10000|   28| 28
100|10000|  262| 202
100|20000|  262| 202
100|50000|  262| 198
100|100000| 262| 198
500|10000|  1852| 1578
500|20000|  1852| 1578
500|50000|  1852| 1578
500|100000| 1852| 1578
1000|10000| 4579| 4030
1000|20000| 4579| 3933
1000|50000| 4579| 3933
1000|100000|4579| 3933

We can notice that the value found not change if the steps increase and in extension we will talk about that.

## Possible extension

Like said before solutions don't change if we change the stopping condition, we can immagine that we are stacked in a local minima and that we found this in a 10_000 steps. A good think to implement could be change the population after 10_000 step and use that to find another minima and compere to our minima.

Another idea could be look the last 1000 steps after find and optima and if it is not increased in these step we change our populations.


