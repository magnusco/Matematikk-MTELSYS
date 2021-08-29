import numpy as np
import matplotlib.pyplot as plt


def methods_test():
    testproblem = lambda x, t: -x
    exact_solution = lambda t: np.exp(-t)

    t_0, T = 0, 1
    x_0 = 1
    num_points = 4
    partition, h = np.linspace(t_0, T, num_points, retstep=True)

    euler_explicit = np.zeros(num_points)
    euler_implicit = np.zeros(num_points)
    trapezoid = np.zeros(num_points)
    heun = np.zeros(num_points)
    midpoint = np.zeros(num_points)

    euler_explicit[0] = x_0
    euler_implicit[0] = x_0
    trapezoid[0] = x_0
    heun[0] = x_0
    midpoint[0] = x_0

    for i in range(0, num_points - 1):
        euler_explicit[i + 1] = euler_explicit[i] - h * euler_explicit[i]
        euler_implicit[i + 1] = (1 / (1 + h)) * euler_implicit[i]
        trapezoid[i + 1] = ((2 - h) / (2 + h)) * trapezoid[i]
        heun[i + 1] = (1 - h + (h ** 2) / 2) * heun[i]
        midpoint[i + 1] = ((2 - h) / (2 + h)) * midpoint[i]

    fine_partition = np.linspace(t_0, T, 100)
    plt.plot(fine_partition, exact_solution(fine_partition), "r")
    plt.plot(partition, euler_explicit, "o")
    plt.plot(partition, euler_implicit, "o")
    plt.plot(partition, trapezoid, "o")
    plt.plot(partition, heun, "o")
    plt.savefig("TMA4101/11/methods_test.png")
    plt.close()

    print(heun[-1] - exact_solution(T))


if __name__ == "__main__":

    methods_test()
