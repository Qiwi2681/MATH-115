import numpy as np  
import matplotlib.pyplot as plt  

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y)  
    plt.plot(y, x) 
    plt.show()  

def slope_function(x):
    return np.power(x, 3)

graph(slope_function, range(-100, 101))