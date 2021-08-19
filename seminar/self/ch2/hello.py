import numpy as np

def _change_one_hot_label(X):
    T = np.zeros((X.size, 10))
    for idx, row in enumerate(T):
        print(idx, row)
        row[X[idx]] = 1
        
    return T

x = np.arange(1,9,1)
y = _change_one_hot_label(x)
print(x)
print(y)

