import matplotlib.pyplot as plt
from solver import Solver

dr = 0.1
n_cell = 201
sol = Solver(n_cell=n_cell, dr=dr)

_, phis = sol.solve((0, 2), 0, eigvals_only=False)

fig, ax = plt.subplots()
ax.plot(sol.rs,  phis[:, 0], label="n = 1")
ax.plot(sol.rs,  phis[:, 1], label="n = 2")
ax.plot(sol.rs,  phis[:, 2], label="n = 3")
ax.set_xlabel("r [j.at]")
ax.set_ylabel(r"$\phi$")
ax.set_title(r"Funkcja pomocnicza $\phi$")
plt.legend()
plt.show()

