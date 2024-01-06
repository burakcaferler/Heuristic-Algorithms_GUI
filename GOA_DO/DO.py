import numpy as np
from solution import solution

def DO(objf, lb, ub, dim, PopSize, iters):
    # Initialize the dragonfly population
    population = np.random.uniform(lb, ub, (PopSize, dim))
    fitness = np.array([objf(ind) for ind in population])
    g_best = population[np.argmin(fitness)]

    s = solution()
    s.objfname = objf.__name__  

    for epoch in range(iters):
        w = 0.9 - epoch * ((0.9 - 0.4) / iters)
        for i in range(PopSize):
            new_position = population[i] + w * (g_best - population[i])
            new_position = np.clip(new_position, lb, ub)
            population[i] = new_position
            fitness[i] = objf(new_position)

        # Update the global best
        idx_best = np.argmin(fitness)
        if fitness[idx_best] < objf(g_best):
            g_best = population[idx_best]

        # Her iterasyonda s.y ve s.x listelerine değer ekleme
        s.y.append(objf(g_best))
        s.x.append(epoch)

    s.best = objf(g_best) 
    s.bestIndividual = g_best.tolist()  

    return s
