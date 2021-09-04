import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def c_n(f, L, n_max):
    # Warning: Casts away imaginary parts, only use even f
    c_n = {}
    for i in range(-n_max, n_max + 1):
        (c_n[i], _err) = quad(lambda t : f(t) * np.exp(-1j*i*np.pi*t/L), -L, L)
        c_n[i] = c_n[i]/(2 * L)
    return c_n

def f_1(t):
    f = np.cos(t)
    #f = t**2
    return f

def f_2(t):
    f = 0.5*np.cos(2*t)
    return f

def f_3(t):
    f = f_1(t) + f_2(t)
    return f

L = np.pi
n_max = 3

n_f_1 = []
c_n_f_1 = []
c_n_dict_f_1 = c_n(f_1, L, n_max)
for key in c_n_dict_f_1:
    n_f_1.append(key)
    c_n_f_1.append(c_n_dict_f_1[key])

n_f_2 = []
c_n_f_2 = []
c_n_dict_f_2 = c_n(f_2, L, n_max)
for key in c_n_dict_f_2:
    n_f_2.append(key)
    c_n_f_2.append(c_n_dict_f_2[key])

n_f_3 = []
c_n_f_3 = []
c_n_dict_f_3 = c_n(f_3, L, n_max)
for key in c_n_dict_f_3:
    n_f_3.append(key)
    c_n_f_3.append(c_n_dict_f_3[key])

# Kan gjøres bedre; mer generelt
fig, axs = plt.subplots(2, 3)
t = np.linspace(-np.pi, np.pi, 300)

# Functions
axs[0, 0].plot(t, f_1(t), "tab:red")
axs[0, 0].set_title("f_1(t) = cos(t)")
axs[0, 0].grid(True)

axs[0, 1].plot(t, f_2(t), "tab:blue")
axs[0, 1].set_title("f_2(t) = 0.5cos(2t)")
axs[0, 1].grid(True)
axs[0, 1].sharey(axs[0, 0])

axs[0, 2].plot(t, f_3(t), "tab:purple")
axs[0, 2].set_title("f_3(t) = f_1(t) + f_2(t)")
axs[0, 2].grid(True)
axs[0, 2].sharey(axs[0, 0])

# Fourier coefficients
axs[1, 0].scatter(n_f_1, c_n_f_1)
#axs[1, 0].set_title("f_1")
axs[1, 0].grid(True)

axs[1, 1].scatter(n_f_2, c_n_f_2)
#axs[1, 1].set_title("f_2")
axs[1, 1].grid(True)
axs[1, 1].sharey(axs[1, 0])

axs[1, 2].scatter(n_f_3, c_n_f_3)
#axs[1, 2].set_title("f_3")
axs[1, 2].grid(True)
axs[1, 2].sharey(axs[1, 0])


for i in range(3):  # Magic number
    axs[0, i].set(xlabel='t')
    axs[1, i].set(xlabel='n', ylabel='c_n')

fig.tight_layout()
plt.show()