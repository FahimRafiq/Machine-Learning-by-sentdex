from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

xs = np.array([1,2,3,4,5,6],dtype= np.float64)
ys = np.array([6,4,5,3,2,1],dtype= np.float64)

def best_fit_line_and_intercept(xs,ys):
    m = ((mean(xs)*mean(ys) - mean(xs*ys))/ (mean(xs)**2 - mean(xs**2)))
    b = mean(ys) - m*mean(xs)
    return m,b

m,b = best_fit_line_and_intercept(xs,ys)
regression_line = m*xs + b
plt.scatter(xs,ys)
plt.plot(xs,regression_line)
plt.show()

