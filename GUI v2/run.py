import functions
from enumFunctions import Functions
from SA import SA_geometric, SA_linear
import pandas as pd
import numpy as np

def select_functions():
    funcs_obj=[functions.selectFunction(Functions.ackley),functions.selectFunction(Functions.griewank),functions.selectFunction(Functions.schwefel),functions.selectFunction(Functions.rastrigin),functions.selectFunction(Functions.sphere),functions.selectFunction(Functions.perm),functions.selectFunction(Functions.zakharov),functions.selectFunction(Functions.rosenbrock),functions.selectFunction(Functions.dixonprice)]

    return funcs_obj

def bounds(function_num,dimension):
    lower_bounds=[None]*dimension
    upper_bounds=[None]*dimension
    bounds=[[-32.768,32768],[-600,600],[-500,500],[-5.12,5.12],[-5.12,5.12],[-30,30],[-5,10],[-2048,2048],[-10,10]]
    
    for idx in range(dimension):
        lower_bounds[idx]=bounds[function_num][0]
        upper_bounds[idx]=bounds[function_num][1]
    return lower_bounds, upper_bounds

def SimulatedAnnealing():
    dim=30
    obj_funcs = select_functions()
    temperatures = [1000,5000,10000]
    results = []
    dfs = [pd.DataFrame()] * len(obj_funcs)

    for idx,_ in enumerate(obj_funcs):
        obj_func=obj_funcs[idx]
        lower,upper=bounds(idx,30)
        for temp in temperatures:
            modes=[0,1]
            for mode in modes:
                for i in range(5):
                    if(mode==0):
                        best = SA_geometric(dim=dim ,min_values = lower, max_values = upper, mu = 0, sigma = 1, initial_temperature = temp, temperature_iterations = 5000,
                        final_temperature = 0.0001, alpha = 0.9, target_function = obj_func, verbose = True)
                        results.append([obj_func.__name__,lower[0],upper[0],temp,round(best[0, -1], 4),'geometric'])

                    else:
                        best = SA_linear( dim=dim,min_values = lower, max_values = upper, mu = 0, sigma = 1, initial_temperature = temp, temperature_iterations = 5000,
                        final_temperature = 0.0001, alpha = 0.9, target_function = obj_func, verbose = True)
                        results.append([obj_func.__name__,lower[0],upper[0],temp,round(best[0, -1], 4),'linear'])
                        
                
        df=pd.DataFrame(results,columns = ['obj_f','lower_bound','upper_bound','temp','best','type'])
        df['std_dev'] = df['best'].rolling(5).std()
        df['avg_fitness']=df['best'].rolling(5).mean()
        df['bestfitness']=df['best'].rolling(5).min()
        df.drop('best', axis=1, inplace=True)
        dfs[idx]=df.iloc[4::5]
        results=[]

    with pd.ExcelWriter('SA_output.xlsx') as writer:
        for idx,df in enumerate(dfs):  
            dfs[idx].to_excel(writer, sheet_name=obj_funcs[idx].__name__)
def main():
    SimulatedAnnealing()

if __name__ == "__main__":
    main()