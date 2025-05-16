# Newton Method

Newton's method is an iterative method for finding the roots of a differentiable function. It is also known as
Newton-Raphson method. The method is based on the idea that a continuous and differentiable function can be approximated
by a straight line tangent to it. The tangent line is then extended to the x-axis to find a better approximation of the
root.

## Algorithm

Given a function $f(x)$, the Newton method is defined as follows:

1. Choose an initial guess $x_0$ for the root.
2. Compute the tangent line to the function at $x_0$.
3. Find the x-intercept of the tangent line to get the next approximation $x_1$.
4. Repeat steps 2 and 3 until the desired accuracy is achieved.

The formula for the Newton method is given by:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

where $f'(x)$ is the derivative of the function $f(x)$.

## Example

Let's find the root of the function $f(x) = x^2 - 4$ using Newton's method. The derivative of $f(x)$ is $f'(x) = 2x$.

1. Choose an initial guess $x_0 = 1$.
2. Compute $f(x_0) = 1^2 - 4 = -3$ and $f'(x_0) = 2 \times 1 = 2$.
3. Compute the next approximation:

   $$x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} = 1 - \frac{-3}{2} = 2.5$$

4. Repeat the process until the desired accuracy is achieved.

## Python Implementation

```python
def newton_method(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        x = x - fx / f_prime(x)
    return x
```

> **Note:** The function `newton_method` takes the function $f(x)$, its derivative $f'(x)$, the initial guess $x_0$, the
> tolerance `tol`, and the maximum number of iterations `max_iter`. It returns the root of the function $f(x)$.

> **Warning:** Newton's method may not converge for all functions or initial guesses. It is important to check the
> convergence of the method for a given problem.

Therefore, it is important to add validations that check

- if the derivative is zero at the current point (as this would cause an undefined division by zero),
- if the maximum number of iterations is reached.

```python
def newton_method(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x

        dfx = f_prime(x)
        if dfx == 0:
            raise ValueError("Derivative of f(x) is zero.")
        x = x - fx / f_prime(x)
    raise ValueError("Newton method did not converge.")
```

## Appendix: Tangent Line

The tangent line to a function $f(x)$ at a point $x_0$ is given by:

$$y = f'(x_0)(x - x_0) + f(x_0)$$

where $f'(x_0)$ is the derivative of the function at $x_0$.

This construction is based on three transformations of the $y = x$ line:

1. Scale the linear function by the derivative $f'(x_0)$.
2. Shift the line horizontally by $x_0$.
3. Shift the line vertically by $f(x_0)$.
