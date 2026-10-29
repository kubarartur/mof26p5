import numpy as np
import matplotlib.pyplot as plt
from solver import Solver

En3 = {
    "l0": [],
    "l1": [],
    "l2": []
}

En2 = {
    "l0": [],
    "l1": []
}

En1 = {
    "l0": []
}

drs = np.linspace(0.01, 1, 1001)
for dr in drs:
    sol = Solver(dr=dr)

    El0 = sol.solve((0, 2), 0)
    El1 = sol.solve((0, 1), 1)
    El2 = sol.solve((0, 0), 2)

    En3["l0"].append(El0[2])
    En3["l1"].append(El1[1])
    En3["l2"].append(El2[0])

    En2["l0"].append(El0[1])
    En2["l1"].append(El1[0])

    En1["l0"].append(El0[0])

fig, ax = plt.subplots()
plt.title("n = 1")
ax.plot(drs, En1["l0"], label="stan podstawowy")
ax.plot((drs[0], drs[-1]), [-0.5, -0.5], 'k--', label="energia analityczna")

ax.set_xlabel(r"$\Delta r$")
ax.set_ylabel("E")
plt.legend()
plt.show()

fig, ax = plt.subplots()
plt.title("n = 2")
ax.plot(drs, En2["l0"], label="l = 0")
ax.plot(drs, En2["l1"], label="l = 1")
ax.plot((drs[0], drs[-1]), [-0.125,  -0.125],
        'k--', label="energia analityczna")

ax.set_xlabel(r"$\Delta r$")
ax.set_ylabel("E")
plt.legend()
plt.show()

fig, ax = plt.subplots()
plt.title("n = 3")
ax.plot(drs, En3["l0"], label="l = 0")
ax.plot(drs, En3["l1"], label="l = 1")
ax.plot(drs, En3["l2"], label="l = 2")
ax.plot((drs[0], drs[-1]), [-1./18,  -1./18],
        'k--', label="energia analityczna")

ax.set_xlabel(r"$\Delta r$")
ax.set_ylabel("E")
plt.legend()
plt.show()
