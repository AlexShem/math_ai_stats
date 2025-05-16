import math
from collections.abc import Callable
from typing import Optional, List, Tuple
from heron_method import heron_sqrt
from scipy import optimize


def numeric_derivative(
        f: Callable[[float], float],
        x: float,
        h: float = 1e-5,
        method: str = 'central'
) -> float:
    """
    Calculate the numeric derivative of a function at a point using various methods.

    Args:
    :param f: (Callable[[float], float]): The function to differentiate.
    :param x: (float): The point at which to calculate the derivative.
    :param h: (float): The small step size for calculation (default: 1e-5).
    :param method: (str): The method to use for derivative calculation.
                  Options: 'central' (default), 'forward', 'backward', 'central_higher_order'.

    Returns:
    :returns: float: The estimated derivative value.
    """

    if method not in ['central', 'forward', 'backward', 'central_higher_order']:
        raise ValueError(
            "Invalid derivative method. Choose 'central', 'forward', 'backward', or 'central_higher_order'.")

    if method == 'central':
        return (f(x + h) - f(x - h)) / (2 * h)
    elif method == 'forward':
        return (f(x + h) - f(x)) / h
    elif method == 'backward':
        return (f(x) - f(x - h)) / h
    elif method == 'central_higher_order':
        # Fourth-order central difference
        return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)
    else:
        raise ValueError("Invalid method. Choose 'central', 'forward', 'backward', or 'central_higher_order'.")


def newton_method(
        f: Callable[[float], float],
        f_prime: Optional[Callable[[float], float]] = None,
        x0: float = 0.1,
        epsilon: float = 1e-7,
        max_iterations: int = 100,
        derivative_method: str = 'central'
) -> Tuple[float, List[float]]:
    """
    Find the root of a function using the Newton-Raphson method.
    
    Args:
    :param f: (Callable[[float], float]): The function to find the root of.
    :param f_prime: (Optional[Callable[[float], float]]): The derivative of the function. If not provided, it will be estimated numerically.
    :param x0: (float): Initial guess for the root.
    :param epsilon: (float): The desired precision (default: 1e-7).
    :param max_iterations: (int): Maximum number of iterations (default: 100).
    :param derivative_method: (str): The method to use for numeric derivative calculation if f_prime is not provided.

    :returns: Tuple[float, List[float]]: The calculated root and the list of x values at each iteration.
    """

    if derivative_method not in ['central', 'forward', 'backward', 'central_higher_order']:
        raise ValueError(
            "Invalid derivative method. Choose 'central', 'forward', 'backward', or 'central_higher_order'.")

    x = x0
    x_values = [x0]

    for _ in range(max_iterations):
        fx = f(x)
        if abs(fx) < epsilon:
            return x, x_values

        # Use provided derivative function or estimate numerically
        f_prime_x = f_prime(x) if f_prime else numeric_derivative(f, x, method=derivative_method)

        if f_prime_x == 0:
            raise ValueError("Derivative is zero. No solution found.")

        x = x - fx / f_prime_x
        x_values.append(x)

    raise ValueError(f"Newton method did not converge within {max_iterations} iterations.")


def newton_sqrt(number: float, epsilon: float = 1e-7, max_iterations: int = 100) -> Tuple[float, List[float]]:
    """
    Calculate the square root of a number using the Newton method.
    
    Args:
    :param number: (float): The number to calculate the square root of.
    :param epsilon: (float): The desired precision (default: 1e-7).
    :param max_iterations: (int): Maximum number of iterations (default: 100).
    
    Returns:
    :returns: Tuple[float, List[float]]: The calculated square root and the list of x values at each iteration.
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")

    if number == 0:
        return 0, [0]

    f = lambda x: x ** 2 - number
    f_prime = lambda x: 2 * x

    return newton_method(f, f_prime, number / 2, epsilon, max_iterations)


def compare_methods(number: float) -> None:
    """
    Compare the Newton method and Heron method for calculating square roots.
    
    Args:
    :param number: (float): The number to calculate the square root of.

    Returns:
    :returns: None
    """
    newton_result, newton_iterations = newton_sqrt(number)
    heron_result = heron_sqrt(number)
    actual_result = math.sqrt(number)

    print(f"Square root of {number}:")
    print(f"Newton method result:  {newton_result}")
    print(f"Heron method result:   {heron_result}")
    print(f"Built-in sqrt result:  {actual_result}")
    print(f"Newton method error:   {abs(newton_result - actual_result)}")
    print(f"Heron method error:    {abs(heron_result - actual_result)}")
    print(f"Newton method iterations: {len(newton_iterations)}")
    print()


def complex_function(x: float) -> float:
    """
    A more complex function: f(x) = x^3 - 2x^2 + 4x - 8
    """
    return x ** 3 - 2 * x ** 2 + 4 * x - 8


def compare_complex_root_finding() -> dict[str, dict]:
    """
    Compare our Newton method with SciPy's root finding for a complex function.
    
    Returns:
    :returns: dict[str, dict]: A dictionary containing the results and iteration data for each method.
    """
    print("Finding root of f(x) = x^3 - 2x^2 + 4x - 8")

    results = {}

    # Calculate the true root using SciPy (we'll consider this the "true" value)
    true_root = optimize.root_scalar(complex_function, method='brentq', bracket=[0, 5]).root

    # Our Newton method with different derivative methods
    derivative_methods = ['central', 'forward', 'backward', 'central_higher_order']
    for method in derivative_methods:
        try:
            our_result, iterations = newton_method(complex_function, derivative_method=method)
            print(f"Our Newton method result ({method}): {our_result}")
            print(f"Function value at our result: {complex_function(our_result)}")
            results[f'newton_{method}'] = {
                'root': our_result,
                'iterations': iterations,
                'true_root': true_root
            }
        except ValueError as e:
            print(f"Our Newton method failed ({method}): {e}")
        print()

    print(f"True root (SciPy's result): {true_root}")
    print(f"Function value at true root: {complex_function(true_root)}")

    return results


if __name__ == "__main__":
    print("Comparing Newton and Heron methods for square root calculation:\n")
    compare_methods(16)
    compare_methods(2)
    compare_methods(1000000)

    print("\nComparing root-finding methods for a complex function:\n")
    compare_results = compare_complex_root_finding()
