import random
from tkinter.tix import INTEGER
import numpy as np
from typing import Callable
from gx_utils import *
import logging
import itertools
import time

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]
def InitialState(list_):
    all_lists = sorted(problem(N, seed=42), key=lambda l: len(l))
    return all_lists[0]




class State:
    def _init_(self, data: np.ndarray):
        self._data = data.copy()
        self._data.flags.writeable = False

    def _hash_(self):
        return hash(bytes(self._data))

    def _eq_(self, other):
        return bytes(self._data) == bytes(other._data)

    def _lt_(self, other):
        return bytes(self._data) < bytes(other._data)

    def _str_(self):
        return str(self._data)

    def _repr_(self):
        return repr(self._data)

    '''
    def data.tolist(self):
        list_tot = list()
        list_tot.append(self._data.all())
        return list_tot
    '''

    @property
    def data(self):
        return self._data

    def copy_data(self):
        return self._data.copy()

def priority_function(state: State):
     list_ = state.data.tolist()
     return sum(len(s) for s in list_)

def possible_actions(all_list: list, actualState):
    all_list1 = all_list.copy()
    for i in actualState:
        while i in all_list1:
            all_list1.remove(i)
    return all_list1 
    
def goal_test(state,N):
    set_ = set()
    for el in state:
        for a in el: 
            set_.add(a)
    set_2 = set(range(N))
    return set_ == set_2


def result(state, a):
    state.append(a)
    return State(np.array(state, dtype=object))

def search(
    all_list,
    initial_state: State,
    goal_test: Callable,
    parent_state: dict,
    state_cost: dict,
    priority_function: Callable,
    unit_cost: Callable,
    number : INTEGER
):
    frontier = PriorityQueue()
    parent_state.clear()
    state_cost.clear()
    state = initial_state
    parent_state[state] = None
    state_cost[state] = 0
    solution = []
    all_list.sort()
    all_list = sorted(list(k for k,_ in itertools.groupby(all_list)), key = lambda l : len(l))

    while state is not None and not goal_test(state.data.tolist(),N):
        for a in possible_actions(all_list,state.data.tolist()):
            new_state = result(state.data.tolist(), a)
            cost = unit_cost(a)
            if new_state not in state_cost and new_state not in frontier:
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                frontier.push(new_state, p=priority_function(new_state))
                logging.debug(f"Added new node to frontier (cost={state_cost[new_state]})")
            elif new_state in frontier and state_cost[new_state] > state_cost[state] + cost:
                old_cost = state_cost[new_state]
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                logging.debug(f"Updated node cost in frontier: {old_cost} -> {state_cost[new_state]}")
        if frontier:
            state = frontier.pop()
        else:
            state = None

    path = list()
    s = state
    while s:
        path.append(s.copy_data())
        s = parent_state[s]

    print(f"Found a solution in {len(path):,} steps; visited {len(state_cost):,} states")
    print(f"Initial blocks : {all_list}")
    print(f"Solution: {state}")
    #print(f"Parent State Dict: {parent_state}")
    #print(f"Path: {list(reversed(path))}")
    return list(reversed(path))            

parent_state = dict()
state_cost = dict()

for N in [5]:
    start = time.time()
    GOAL = set(range(N))
    all_lists = problem(N, seed=42)
    search(
        all_lists,
        initial_state = State(np.array([],dtype = object)),
        goal_test=goal_test,
        parent_state=parent_state,
        state_cost=state_cost,
        priority_function= priority_function,
        unit_cost= lambda a: len(a),
        number= N
        )
    end = time.time()

    print(f"Done in {end-start} seconds")