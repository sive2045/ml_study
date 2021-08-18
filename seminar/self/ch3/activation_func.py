import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    y = x > 0
    return y.astype(np.int) # bool을 int형으로 변환.

# plot step func
#x = np.arange(-5.0, 6.0, 0.1)
#y = step_function(x)
#plt.plot(x, y); plt.ylim(-0.1, 1.1)
#plt.title('Heavisid step function'); plt.show()

sigmoid_function = lambda x: 1 / (1 + np.exp(-x))

#plot sigmoid function
#x = np.arange(-5.0, 6.0, 0.1)
#y = sigmoid_function(x)
#plt.plot(x, y); plt.ylim(-0.1, 1.1)
#plt.title('Sigmoid function'); plt.show()

#plot sigmoid and step
step = lambda x: np.array(x>0, dtype=np.int32)
sigmoid = lambda x: 1 /(1 + np.exp(-x))

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(-6,6)
y_step = step(x)
y_sig = sigmoid(x)

ax.plot(x,y_step, '--', label=r'$H(x)$', c='g')
ax.plot(x,y_sig, label=r'$S(x)$', c='g')
ax.set_xlim(-6,6); ax.set_ylim(-0.1, 1.1)
ax.set_xlabel(r'$x$'); ax.set_ylabel(r'$y$')
ax.legend()

plt.show()