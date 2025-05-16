import numpy as np


def newton_method(
        f,
        f_prime,
        x0: float,
        epsilon: float = 1e-8,
        max_iter: int = 50
) -> float:
    x = x0

    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < epsilon:
            return x

        df = f_prime(x)
        if df == 0:
            raise ValueError("Derivative of the function is zero.")

        x = x - fx / df

    raise ValueError("Method did not converge.")


fun = lambda x: np.sin(0.2 * x) + np.exp(x) + 0.5
fun_prime = lambda x: 0.2 * np.cos(0.2 * x) + np.exp(x)

x_0 = 1

x_root = newton_method(fun, fun_prime, x_0)

print("Calculating the root of f(x)")
print(f"Root: {x_root}")
