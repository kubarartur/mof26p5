import numpy as np
import scipy.linalg as sl


class Solver:

    def __init__(self,
                 n_cell: int = 201,
                 dr: float = 0.1):

        self.dr = dr
        self.diag = np.empty(n_cell)
        self.off_diag = -0.5/self.dr**2*np.ones(n_cell - 1)

        # helper
        self.rs = dr*np.arange(1, n_cell+1, step=1, dtype=np.float32)

    def solve(self, n_range: tuple(int, int), ql: int, eigvals_only=True):

        self.diag = 1/self.dr**2
        self.diag += 0.5*ql*(ql + 1)/self.rs**2
        self.diag -= 1./self.rs

        if eigvals_only:
            vals = sl.eigh_tridiagonal(self.diag, self.off_diag,
                                       eigvals_only=eigvals_only,
                                       select='i',
                                       select_range=n_range)
            return vals
        else:
            vals, phis = sl.eigh_tridiagonal(self.diag, self.off_diag,
                                             eigvals_only=eigvals_only,
                                             select='i',
                                             select_range=n_range)
            return vals, phis

    def get_psis(self, phis):

        psis = np.empty_like(phis)
        try:
            for i in range(phis.shape[1]):
                psis[:, i] = phis[:, i]/self.rs
        except IndexError:
            psis = phis/self.rs

        return psis
