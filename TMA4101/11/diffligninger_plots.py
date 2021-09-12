import numpy as np
import matplotlib.pyplot as plt


def methods_test_plot():
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
    plt.plot(
        fine_partition, exact_solution(fine_partition), "k", label="Eksakt løsning"
    )
    plt.plot(partition, euler_explicit, "o--", label="Eksplisitt Euler")
    plt.plot(partition, euler_implicit, "o--", label="Implisitt Euler")
    plt.plot(partition, trapezoid, "o--", label="Trapesmetoden")
    plt.plot(partition, heun, "o--", label="Heuns metode")
    plt.legend()
    plt.savefig("TMA4101/11/methods_test.png")
    plt.close()


def error_test():
    testproblem = lambda x, t: -x
    exact_solution = lambda t: np.exp(-t)
    
    t_0, T = 0, 1
    x_0 = 1

    f = open("TMA4101/11/errors.txt", "w")

    for num_points in [10, 100, 1000, 10000]:
        partition, h = np.linspace(t_0, T, num_points, retstep=True)

        euler_explicit = np.zeros(num_points)
        euler_implicit = np.zeros(num_points)
        trapezoid = np.zeros(num_points)
        heun = np.zeros(num_points)

        euler_explicit[0] = x_0
        euler_implicit[0] = x_0
        trapezoid[0] = x_0
        heun[0] = x_0

        for i in range(0, num_points - 1):
            euler_explicit[i + 1] = euler_explicit[i] - h * euler_explicit[i]
            euler_implicit[i + 1] = (1 / (1 + h)) * euler_implicit[i]
            trapezoid[i + 1] = ((2 - h) / (2 + h)) * trapezoid[i]
            heun[i + 1] = (1 - h + (h ** 2) / 2) * heun[i]
        
        exact = exact_solution(partition)

        f.write("Local errors for partition " + str(num_points) + "\n \n")

        f.write("Eksplisitt Euler: " + str("{:.3e}".format(np.abs(euler_explicit[1] - exact[1]))) + "\n")
        f.write("Implisitt Euler: " + str("{:.3e}".format(np.abs(euler_implicit[1] - exact[1]))) + "\n")
        f.write("Trapesmetoden: " + str("{:.3e}".format(np.abs(trapezoid[1] - exact[1]))) + "\n")
        f.write("Heuns metode: " + str("{:.3e}".format(np.abs(heun[1] - exact[1]))) + "\n")
        f.write("\n \n")

        f.write("Global errors for partition " + str(num_points) + "\n \n")

        f.write("Eksplisitt Euler: " + str("{:.3e}".format(np.abs(euler_explicit[-1] - exact[-1]))) + "\n")
        f.write("Implisitt Euler: " + str("{:.3e}".format(np.abs(euler_implicit[-1] - exact[-1]))) + "\n")
        f.write("Trapesmetoden: " + str("{:.3e}".format(np.abs(trapezoid[-1] - exact[-1]))) + "\n")
        f.write("Heuns metode: " + str("{:.3e}".format(np.abs(heun[-1] - exact[-1]))) + "\n")
        f.write("\n \n")
    f.close()


def stability_plot():
    testproblem = lambda x, t: -x
    exact_solution = lambda t: np.exp(-t)

    t_0, T = 0, 15
    x_0 = 1
    num_points = 5
    partition, h = np.linspace(t_0, T, num_points, retstep=True)

    euler_explicit = np.zeros(num_points)
    euler_implicit = np.zeros(num_points)
    
    euler_explicit[0] = x_0
    euler_implicit[0] = x_0
    
    for i in range(0, num_points - 1):
        euler_explicit[i + 1] = euler_explicit[i] - h * euler_explicit[i]
        euler_implicit[i + 1] = (1 / (1 + h)) * euler_implicit[i]
    
    fine_partition = np.linspace(t_0, T, 100)
    plt.plot(
        fine_partition, exact_solution(fine_partition), "k", label="Eksakt løsning"
    )
    plt.plot(partition, euler_explicit, "o--r", label="Eksplisitt Euler")
    plt.legend()
    plt.savefig("TMA4101/11/stability_test_explicit.png")
    plt.close()

    plt.plot(
        fine_partition, exact_solution(fine_partition), "k", label="Eksakt løsning"
    )
    plt.plot(partition, euler_implicit, "o--r", label="Implisitt Euler")
    plt.legend()
    plt.savefig("TMA4101/11/stability_test_implicit.png")
    plt.close()

    


if __name__ == "__main__":

    # methods_test_plot()
    # error_test()
    stability_plot()