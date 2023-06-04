def integrate(f, a, b, n):
    dx = (b - a) / n
    result = 0
    for i in range(n):
        result += f(a + i * dx)
    return result * dx
