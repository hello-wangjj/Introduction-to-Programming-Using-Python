from lmfit import minimize, Minimizer, Parameters, Parameter, report_fit
import numpy as np

__author__ = 'wangj'
__date__ = '2017/12/24 16:31'


def residual(p, x, data):
    model = p['a'] * np.sin(p['b'] * x) + p['c'] * (
            1 - 1 / np.sqrt(1 - p['d'] * p['d']) * np.e ** (-p['e']) * np.sin(
        np.sqrt(1 - p['d'] * p['d']) * x + np.arccos(p['d'])))
    return model - data


if __name__ == '__main__':
    p = Parameters()
    p.add('a', value=0.01)
    p.add('b', value=0.01)
    p.add('c', value=0.1)
    p.add('d', value=0.01, min=-0.9999, max=0.9999)
    p.add('e', value=0.01)
    # p.add('f', value=0.010)
    x = np.linspace(0, 200, 20)
    data = np.sin(x)
    # do fit, here with leastsq model
    minner = Minimizer(residual, p, fcn_args=(x, data))
    result = minner.minimize(method='least_squares')

    # calculate final result
    final = data + result.residual

    # write error report
    report_fit(result)

    # try to plot results
    try:
        import pylab

        pylab.plot(x, data, 'k+')
        pylab.plot(x, final, 'r')
        pylab.show()
    except:
        pass
