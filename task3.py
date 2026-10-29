import matplotlib.pyplot as plt
from solver import Solver

dr = 0.1
n_cell = 201
sol = Solver(n_cell=n_cell, dr=dr)

_, phis = sol.solve((0, 2), 0, eigvals_only=False)
psis = sol.get_psis(phis)

fig, ax = plt.subplots()
ax.plot(sol.rs,  psis[:, 0], label="n = 1")
ax.plot(sol.rs,  psis[:, 1], label="n = 2")
ax.plot(sol.rs,  psis[:, 2], label="n = 3")
ax.set_xlabel("r [j.at]")
ax.set_ylabel(r"$\psi$")
ax.set_title(r"Funkcja falowa $\psi$")
plt.legend()
plt.show()
