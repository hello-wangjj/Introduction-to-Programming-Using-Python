import numpy as np
from sklearn import datasets
from scipy.special import comb
import math
import matplotlib.pyplot as plt

__author__ = 'wangj'
__date__ = '2018/01/16 20:03'


def main():
    pass


def ensemble_error(n_classifier, error):
    k_start = math.ceil(n_classifier / 2)
    probs = [comb(n_classifier, k) * error ** k * (1 - error) ** (n_classifier - k) for k in
             range(k_start, n_classifier + 1)]
    return sum(probs)


if __name__ == '__main__':
    main()
    print(ensemble_error(11, 0.25))
    error_range = np.arange(0.0, 1.01, 0.01)
    ens_errors = [ensemble_error(n_classifier=11, error=error) for error in error_range]
    plt.figure(1)
    plt.plot(error_range, ens_errors, label='Ensemble error', linewidth=2)
    plt.plot(error_range, error_range, linestyle='--', label='base error', linewidth=2)
    plt.xlabel('base error')
    plt.ylabel('Base/Ensemble error')
    plt.legend(loc='best')
    plt.grid()
    plt.show()
