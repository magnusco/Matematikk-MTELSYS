import numpy as np
import matplotlib.pyplot as plt


def phase_plane_1():
    X, Y = np.meshgrid(np.linspace(-1.0, 1.0, 30), np.linspace(-1.0, 1.0, 30))
    U, V = Y, -5 * X - 2 * Y

    plt.streamplot(X, Y, U, V, color="r", linewidth=1, density=1, minlength=0.25)
    plt.axis("square")
    plt.xticks([], [])
    plt.yticks([], [])
    plt.axhline(color="black", lw=0.8)
    plt.axvline(color="black", lw=0.8)
    plt.savefig("TMA4111/1/phase_plane_1.png")
    plt.close()
    return 0


def phase_plane_2():
    X, Y = np.meshgrid(np.linspace(-1.0, 1.0, 30), np.linspace(-1.0, 1.0, 30))
    U, V = X - 5 * Y, X - Y

    plt.streamplot(X, Y, U, V, color="r", linewidth=1, density=1, minlength=0.25)
    plt.axis("square")
    plt.xticks([], [])
    plt.yticks([], [])
    plt.axhline(color="black", lw=0.8)
    plt.axvline(color="black", lw=0.8)
    plt.savefig("TMA4111/1/phase_plane_2.png")
    plt.close()
    return 0


def phase_plane_3():
    X, Y = np.meshgrid(np.linspace(-1.0, 1.0, 30), np.linspace(-1.0, 1.0, 30))
    U, V = X + Y, X - 2 * Y

    plt.streamplot(X, Y, U, V, color="r", linewidth=1, density=1, minlength=0.25)
    plt.axis("square")
    plt.xticks([], [])
    plt.yticks([], [])
    plt.axhline(color="black", lw=0.8)
    plt.axvline(color="black", lw=0.8)
    plt.savefig("TMA4111/1/phase_plane_3.png")
    plt.close()
    return 0


def phase_plane_4():
    X, Y = np.meshgrid(np.linspace(-1.0, 1.0, 30), np.linspace(-1.0, 1.0, 30))
    U, V = 4 * X - 2 * Y, 3 * X + Y

    plt.streamplot(X, Y, U, V, color="r", linewidth=1, density=1, minlength=0.25)
    plt.axis("square")
    plt.xticks([], [])
    plt.yticks([], [])
    plt.axhline(color="black", lw=0.8)
    plt.axvline(color="black", lw=0.8)
    plt.savefig("TMA4111/1/phase_plane_4.png")
    plt.close()
    return 0


def phase_plane_radial():
    X, Y = np.meshgrid(np.linspace(-2.0, 2.0, 30), np.linspace(-2.0, 2.0, 30))
    R, Theta = (X ** 2 + Y ** 2) ** 0.5, np.arctan2(Y, X)

    dR, dTheta = R * (1 - R * R), 1
    C, S = np.cos(Theta), np.sin(Theta)
    U, V = dR * C - R * S * dTheta, dR * S + R * C * dTheta

    plt.streamplot(X, Y, U, V, color="r", linewidth=1, density=1, minlength=0.25)
    plt.axis("square")
    plt.xticks([], [])
    plt.yticks([], [])
    plt.axhline(color="black", lw=0.8)
    plt.axvline(color="black", lw=0.8)
    plt.savefig("TMA4111/1/phase_plane_radial.png")
    plt.close()
    return 0


def van_der_pol():
    mu = 1
    X, Y = np.meshgrid(np.linspace(-3.0, 3.0, 30), np.linspace(-3.0, 3.0, 30))
    U = Y
    V = -mu * (X ** 2 - 1) * Y - X

    plt.streamplot(X, Y, U, V, color="r", linewidth=1, density=1, minlength=0.25)
    plt.axis("square")
    plt.xticks([], [])
    plt.yticks([], [])
    plt.axhline(color="black", lw=0.8)
    plt.axvline(color="black", lw=0.8)
    plt.savefig("TMA4111/1/van_der_pol.png")
    plt.close()
    return 0


def van_der_pol_impl_euler():
    mu = 1
    T = 20
    N = 2000
    h = T / N
    time = np.linspace(0, T, N)

    x_dot = lambda x, y, mu : y
    y_dot = lambda x, y, mu : mu * (1-x**2) * y - x
    
    x = np.zeros(N)
    y = np.zeros(N)
    x[0], y[0] = 0, 4

    for i in range(0, N - 1):
        x[i + 1] = x[i] + h * x_dot(x[i], y[i], mu)
        y[i + 1] = y[i] + h * y_dot(x[i+1], y[i], mu)

    plt.plot(x, y, 'k')
    plt.axis("square")
    plt.xlim([-4, 4])
    plt.grid(True)
    plt.savefig("TMA4111/1/van_der_pol_impl_euler.png")
    plt.close()
    return 0


if __name__ == "__main__":
    # phase_plane_1()
    # phase_plane_2()
    # phase_plane_3()
    # phase_plane_4()
    # phase_plane_radial()
    # van_der_pol()

    van_der_pol_impl_euler()