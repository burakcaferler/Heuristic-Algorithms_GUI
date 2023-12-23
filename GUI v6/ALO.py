#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 15:18
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : ALO.py
# @Statement : Ant Lion Optimizer
# @Reference : Mirjalili S. The ant lion optimizer[J]. Advances in Engineering Software, 2015, 83: 80-98.
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from solution import solution



s = solution()

def boundary_check(value, lb, ub):
    """
    The boundary check
    :param value:
    :param lb: the lower bound
    :param ub: the upper bound
    :return:
    """
    

    for i in range(len(value)):
        value[i] = max(value[i], lb[i])
        value[i] = min(value[i], ub[i])
    return value


def roulette(pro):
    """
    The roulette selection
    :param pro: probability
    :return:
    """
    r = random.random()
    probability = 0
    sum_pro = sum(pro)
    for i in range(len(pro)):
        probability += pro[i] / sum_pro
        if probability >= r:
            return i





def ALO(obj_func,pop, iter, lb, ub,dim):
    if not isinstance(lb, (list, np.ndarray)):
        lb = [lb] * dim
    if not isinstance(ub, (list, np.ndarray)):
        ub = [ub] * dim

    def random_walk(t, iter, dim, lb, ub, pos):
    # The random walk around pos
        if t < 0.1 * iter:
            w = 1
        elif t < 0.5 * iter:
            w = 2
        elif t < 0.75 * iter:
            w = 3
        elif t < 0.9 * iter:
            w = 4
        elif t < 0.95 * iter:
            w = 5
        else:
            w = 6
        if w == 1:
            I = 1  # the ratio of random walk
        else:
            I = 1 + 10 ** w * (t + 1) / iter
        temp_lb = [lb[i] / I for i in range(dim)]
        temp_ub = [ub[i] / I for i in range(dim)]
        if random.random() < 0.5:
            temp_lb = [temp_lb[i] + pos[i] for i in range(dim)]
        else:
            temp_lb = [-temp_lb[i] + pos[i] for i in range(dim)]
        if random.random() >= 0.5:
            temp_ub = [temp_ub[i] + pos[i] for i in range(dim)]
        else:
            temp_ub = [-temp_ub[i] + pos[i] for i in range(dim)]
        new_pos = []
        for i in range(dim):
            X = np.cumsum(2 * (np.random.rand(iter, 1) > 0.5) - 1)
            X[0] = 0
            a = np.min(X)
            b = np.max(X)
            c = temp_lb[i]
            d = temp_ub[i]
            temp_value = (X - a) * (d - c) / (b - a) + c
            new_pos.append(temp_value[t])
        return new_pos



    """
    The main function of the ALO
    :param pop: the population size
    :param iter: the number of iterations
    :param lb: the lower bound
    :param ub: the upper bound
    :return:
    """
    # Step 1. Initialization
      # dimension
    a_pos = []  # the position of ants
    a_score = []  # the score of ants
    al_pos = []  # the position of ant lions
    al_score = []  # the score of ant lions
    for _ in range(pop):
        temp_a_pos = [random.uniform(lb[i], ub[i]) for i in range(dim)]
        temp_al_pos = [random.uniform(lb[i], ub[i]) for i in range(dim)]
        a_pos.append(temp_a_pos)
        a_score.append(obj_func(temp_a_pos))
        al_pos.append(temp_al_pos)
        al_score.append(obj_func(temp_al_pos))
    elite_score = min(al_score)  # the score of the elite ant lion
    elite_pos = al_pos[al_score.index(elite_score)]  # the position of the elite ant lion
    iter_best = []  # the global best of each iteration
    con_iter = 0  # the convergence iteration

    # Step 2. The main loop
    for t in range(iter):
        for i in range(pop):
            pro = [1 / al_score[i] for i in range(pop)]
            ind = roulette(pro)  # roulette selection
            RA = random_walk(t, iter, dim, lb, ub, al_pos[ind])  # the random walk around the selected ant lion
            RE = random_walk(t, iter, dim, lb, ub, elite_pos)  # the random walk around the elite
            a_pos[i] = [(RA[j] + RE[j]) / 2 for j in range(dim)]
            a_pos[i] = boundary_check(a_pos[i], lb, ub)
            a_score[i] = obj_func(a_pos[i])

        # Catching prey and re-building the pit
        temp_pos = al_pos.copy()
        temp_score = al_score.copy()
        temp_pos.extend(a_pos)
        temp_score.extend(a_score)
        al_pos = []
        al_score = []
        sorted_index = np.argsort(temp_score)
        for i in range(pop):
            al_pos.append(temp_pos[sorted_index[i]])
            al_score.append(temp_score[sorted_index[i]])
        if min(al_score) < elite_score:
            elite_score = min(al_score)
            elite_pos = al_pos[al_score.index(elite_score)]
            con_iter = t + 1
        else:
            al_pos[0] = elite_pos
            al_score[0] = elite_score
        iter_best.append(elite_score)
        s.x.append(t)
        s.y.append(elite_score)

    print(elite_score)
    print(elite_pos)
    print(con_iter)

    # Step 3. Sort the results
    #x = [i for i in range(iter)]
    #plt.figure()
    #plt.plot(x, iter_best, linewidth=2, color='blue')
    #plt.xlabel('Iteration number')
    #plt.ylabel('Global optimal value')
    #plt.title('Convergence curve')
    #plt.show()
    #return {'best score': elite_score, 'best solution': elite_pos, 'convergence iteration': con_iter}
    return s


