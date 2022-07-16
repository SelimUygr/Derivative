import numpy as np
from sympy import Poly, sympify
from matplotlib import pyplot as plt


x = np.linspace(1,20,50)

def draw(function):
    poly_string = function
    coeffs = Poly(sympify(poly_string)).all_coeffs()
    p_callable = np.poly1d(np.array(coeffs).astype(np.float))

    xs = np.linspace(-10,10,100)
    ys = p_callable(xs)

    plt.title(f"Polynomial: {function}")
    plt.plot(xs, ys)
    plt.show()