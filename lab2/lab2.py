from itertools import combinations
import random 
import numpy as np
from tqdm import tqdm
import pandas as pd

"""
TODO list of step to create this code:
    initial variable 
    creation of initial population -> len( ) = (len(initial_formulation)//2) +1
    mutation with p = pi
    check feasiable
    crossover
    check feasiable
    save the best 
"""

# Function for the problem 
def problem(N, seed=42):
    """Creates an instance of the problem"""

    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

#Check if in the individual are present each number in range(N)
def checkFeasible(individual, N):
    goal = set(list(range(N)))
    flag = False
    coverage = set()
    for list_ in individual:
        for num in list_:
            coverage.add(num)
        if coverage == goal:
            return True
    return False

#Encoding the individual in a binary way, 0 if we don't take the list, 1 if we take
def createIndividual(indexes,len_):
    individual01 = np.zeros(len_)
    individual01[indexes] = 1
    return individual01

#Fitness = sum of number of elements inside the list that we take
def createFitness(induvual):
    fitness = 0
    for list_ in induvual:
        fitness += len(list_)
    return fitness
#Crossover with two side so the offspring is created with the parentA's first part, parentB's between the two cut point and the last part parentA
def crossOver(parentA,parentB,initial_formualtion, N):
    parentA, parentB = parentA[1], parentB[1]
    gap1 = list(range(1,len(parentA)-1))
    cutIndex = sorted(np.random.choice(gap1,2))
    offSpring = np.concatenate((parentA[:cutIndex[0]],parentB[cutIndex[0]:cutIndex[1]],parentA[cutIndex[1]:]), axis=0)
    indexOff = np.where(offSpring > 0)
    offSpringList =  np.array(initial_formulation, dtype=object)[indexOff]
    if checkFeasible(offSpringList,N) == True:
        flag = True
        return ((createFitness(offSpringList),offSpring), True)
    else:
        return (offSpring,False)
#Here is present the mutation function in which we change a gene chosen randomly
def mutation(parent,initial_formulation,N):
    parentA = parent[1]
    mutIndex = np.random.choice(list(range(len(list(parentA)))))
    mut = np.concatenate((parentA[:mutIndex],np.array([1-parentA[mutIndex]]),parentA[mutIndex+1:]), axis=0)
    indexMut = np.where(mut > 0)
    MutList =  np.array(initial_formulation, dtype=object)[indexMut]
    if checkFeasible(MutList,N) == True:
        flag = True
        return ((createFitness(MutList),mut), True)
    else:
        return (mut,False)

#fuction to remove the duplicates from the population
def removeDuplicates(population):
    population1 = [(",".join(map(str,map(int,x[1].tolist()))),x[0]) for x in population]
    dict_ = dict(population1)
    list_ = list()
    for k,v in dict_.items():
        list_.append((v,np.fromstring(k,sep=",")))
    return list_


#Inital list of lists
N = [5,10,20,100,500,1000]
dictPrint = dict()
dictPrint["N"] = []
dictPrint["Time"] = []
dictPrint["Solution Found"] = []
for N in tqdm(N):
    #Initail variable 
    for tmax in tqdm([10_000,20_000,50_000,100_000]):
        t = 0 
        initial_formulation = problem(N)
        random.seed(42)
        np.random.seed(42)
        gap = list(range(0,len(initial_formulation)))
        population = list()
        #Creation of the popualtion and check if the creation is feasible or not 
        while len(population) != ((len(initial_formulation)//2)+1):
            indexes = np.random.choice(gap, (len(initial_formulation)//2)+1)
            individual = np.array(initial_formulation, dtype=object)[indexes]
            if checkFeasible(individual,N) == True:
                individual01 = createIndividual(indexes, len(initial_formulation))
                population.append((createFitness(individual),individual01))

        #Sort the population based on fitness, less fitness better solution 
        population.sort(key = lambda l : l[0])

        while t <=  tmax:
            repoducer = [population[i] for i in range(7)]  #choose the best six to reproduce
            offSprings = list()
            for i in combinations(repoducer, 2): #I used each of best 6 to reproduce and generate the new offsprings
                parentA = i[0]
                parentB = i[1]
                if random.random() < .45: #Random mutation and randomly which parent will be mutate
                    choose = random.choice([0,1])
                    if choose == 0:
                        (offSpring,flag) = mutation(parentA,initial_formulation,N)
                        if flag == True:
                            offSprings.append(offSpring)
                    else:
                        (offSpring,flag) = mutation(parentB,initial_formulation,N)
                        if flag == True:
                            offSprings.append(offSpring)
                (offSpring,flag)  = crossOver(parentA,parentB,initial_formulation, N)
                if flag == True:
                    offSprings.append(offSpring)
            offSprings.sort(key = lambda l: l[0])
            population += offSprings[:3] #I append to the population only the best three solutions between the offsprings
            population.sort(key = lambda l : l[0])
            population = removeDuplicates(population)
            if len(population) > 10:
                del population[len(population)-3:] #I delete the final three to not compute heavy sorting, pay attentio that is not obvious that we have such items
            t+=1 
        dictPrint["N"].append(N)
        dictPrint["Time"].append(tmax)
        dictPrint["Solution Found"].append(population[0][0])

pd.DataFrame(dictPrint).to_csv("result_lab2_mutatation=0,45.csv")
 




