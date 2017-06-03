from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

xs = np.array([1,2,3,4,5,6],dtype= np.float64)
ys = np.array([2,5,7,4,5,8],dtype= np.float64)

def best_fit_line_and_intercept(xs,ys):
    m = ((mean(xs)*mean(ys) - mean(xs*ys))/ (mean(xs)**2 - mean(xs**2)))
    b = mean(ys) - m*mean(xs)
    return m,b

def squared_error(ys_orig,ys_line):
    return sum((ys_line-ys_orig)**2)

def coefficient_of_determination(ys_orig,ys_line):
    y_mean_line = mean(ys_orig)
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr/squared_error_y_mean)

m,b = best_fit_line_and_intercept(xs,ys)
regression_line = m*xs + b

# predict_x = 8
# predict_y = (m*predict_x) + b
# print(predict_y)

r_squared = coefficient_of_determination(ys,regression_line)
print(r_squared)

plt.scatter(xs,ys)
plt.plot(xs,regression_line)
plt.show()

