
import random
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, tan ,cosh, tanh, sinh, abs, exp, mean, pi, prod, sqrt, sum
import functions
from enumFunctions import Functions
import pandas as pd
from solution import solution



def boundary_check(value, lb, ub):
    """
    The boundary check
    :param value:
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :return:
    """
    for i in range(len(value)):
        value[i] = max(value[i], lb[i])
        value[i] = min(value[i], ub[i])
    return value


def harmonySearch(hms, iter, hmcr, par, bw, nnew, lb, ub,obj_f):
    sol=solution()
    pos = []  # the set of harmonies
    score = []  # the score of harmonies
    dim = len(lb)  # dimension
    for i in range(hms):
        temp_pos = [random.uniform(lb[j], ub[j]) for j in range(dim)]
        pos.append(temp_pos)
        score.append(obj_f(temp_pos))
    iter_best = []
    gbest = min(score)  # the score of the best-so-far harmony
    gbest_pos = pos[score.index(gbest)]  # the best-so-far harmony
    con_iter = 0

    for t in range(iter):
        new_pos = []
        new_score = []

        # Step 2.1. Create new harmonies
        for _ in range(nnew):
            temp_pos = []
            for j in range(dim):
                if random.random() < hmcr:  # utilize harmony memory
                    ind = random.randint(0, hms - 1)
                    temp_pos.append(pos[ind][j])
                    if random.random() < par:  # pitch adjustment
                        temp_pos[j] += random.normalvariate(0, 1) * bw * (ub[j] - lb[j])
                else:
                    temp_pos.append(random.uniform(lb[j], ub[j]))
            temp_pos = boundary_check(temp_pos, lb, ub)
            new_pos.append(temp_pos)
            new_score.append(obj_f(temp_pos))

        new_pos.extend(pos)
        new_score.extend(score)
        sorted_score = sorted(new_score)
        pos = []
        score = []
        for i in range(hms):
            score.append(sorted_score[i])
            pos.append(new_pos[new_score.index(sorted_score[i])])

 
        if score[0] < gbest:
            gbest = score[0]
            gbest_pos = pos[0]
            con_iter = t + 1
        iter_best.append(gbest)
        sol.x.append(t + 1)  # Assuming you want to start counting iterations from 1
        sol.y.append(gbest)
    x = [i for i in range(iter)]

    return sol





