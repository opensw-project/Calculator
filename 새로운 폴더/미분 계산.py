def differentiate(f, x):
    h = 1e-10
    return (f(x+h) - f(x)) / h
