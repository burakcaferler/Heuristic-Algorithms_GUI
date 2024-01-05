import numpy as np

def DO(objf, bounds, dim, PopSize, iters):
    lb, ub = bounds
    # Initialize the dragonfly population
    population = np.random.uniform(lb, ub, (PopSize, dim))
    fitness = np.array([objf(ind) for ind in population])
    g_best = population[np.argmin(fitness)]

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

    return g_best, objf(g_best)