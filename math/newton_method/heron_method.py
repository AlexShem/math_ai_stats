import warnings

def heron_sqrt(number, epsilon=1e-7, max_iterations=100):
    """
    Calculate the square root of a number using the Heron method.
    
    Args:
    number (float): The number to calculate the square root of.
    epsilon (float): The desired precision (default: 1e-7).
    max_iterations (int): Maximum number of iterations (default: 100).
    
    Returns:
    float: The calculated square root.
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    
    if number == 0:
        return 0
    
    guess = number / 2  # Initial guess
    
    for _ in range(max_iterations):
        new_guess = (guess + number / guess) / 2
        if abs(new_guess - guess) < epsilon:
            return new_guess
        guess = new_guess
    
    warnings.warn(f"Maximum number of iterations ({max_iterations}) reached. The result may not be accurate.", RuntimeWarning)
    return guess

# Example usage
if __name__ == "__main__":
    number = 16
    result = heron_sqrt(number)
    print(f"The square root of {number} is approximately {result}")
    print(f"Built-in sqrt function result: {number**0.5}")
    
    number = 2
    result = heron_sqrt(number)
    print(f"\nThe square root of {number} is approximately {result}")
    print(f"Built-in sqrt function result: {number**0.5}")

