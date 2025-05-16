import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from coinflip import flip_coin  # Import the flip_coin function provided


def run_experiments(n_flips: int, n_experiments: int, p: float | None = None):
    """Simulate multiple coin flip experiments to estimate the probability of heads.

    This function runs multiple experiments, each consisting of `n_flips` coin flips,
    and returns the estimated probabilities of heads from each experiment.

    :param n_flips: (int): Number of coin flips per experiment.
    :param n_experiments: (int): Number of experiments to run.
    :param p: (float, optional): Probability of the coin landing on heads. If None,
              the default probability from the coinflip module will be used (0.54).

    :return: list[float]: List of estimated probabilities from each experiment.
    """
    estimated_probabilities = []  # List to store the estimated probabilities
    
    for _ in range(n_experiments):
        flips = []  # List to store results of coin flips in this experiment
        # Flip the coin n_flips times
        for _ in range(n_flips):
            flip_result = flip_coin(p)  # Flip the coin with probability p (uses default from coinflip.py if None)
            flips.append(flip_result)  # Store the result (1 for heads, 0 for tails)
        # Calculate the estimated probability for this experiment
        probability_estimate = sum(flips) / n_flips
        estimated_probabilities.append(probability_estimate)

    return estimated_probabilities


if __name__ == '__main__':
    # Number of coin flips for the initial estimation
    N_FLIPS = 10

    # Initial example: Flip a coin N_FLIPS times and estimate the probability of heads
    # This uses the default PROBABILITY_HEAD value from coinflip.py (0.54)
    coin_flips = [flip_coin() for _ in range(N_FLIPS)]  # Flip the coin N_FLIPS times
    head_probability = sum(coin_flips) / N_FLIPS  # Calculate the estimated probability
    print(f'Estimated P(head) after {N_FLIPS} flips: {head_probability:.4f}')    # Perform multiple experiments with increasing numbers of coin flips
    # to demonstrate the Law of Large Numbers
    N_EXPERIMENTS = 20  # Number of experiments to repeat for each number of flips

    # List of different numbers of coin flips to try (exponentially increasing)
    n_flips_list = [10, 100, 1000, 10000, 100000]  # Powers of 10 for logarithmic scale plotting

    # Lists to store the statistical results across experiments
    avg_probabilities = []  # Average estimated probabilities across experiments
    max_probabilities = []  # Maximum estimated probabilities observed
    min_probabilities = []  # Minimum estimated probabilities observed    # Loop over each number of flips to see how estimation improves with sample size
    for n_flips in n_flips_list:
        # Run the experiments and get the estimated probabilities
        # Each experiment flips the coin n_flips times and calculates P(head)
        probabilities = run_experiments(n_flips, N_EXPERIMENTS)

        # Calculate summary statistics across all experiments with this sample size
        average_p = sum(probabilities) / N_EXPERIMENTS  # Mean estimated probability
        max_p = max(probabilities)  # Maximum observed probability (highest estimate)
        min_p = min(probabilities)  # Minimum observed probability (lowest estimate)

        # Append the statistics to the lists
        avg_probabilities.append(average_p)
        max_probabilities.append(max_p)
        min_probabilities.append(min_p)

        # Print the results
        print(f'\nEstimated P(head) for {n_flips} flips:')
        print(f'Average: {average_p:.4f}')
        print(f'Maximum: {max_p:.4f}')
        print(f'Minimum: {min_p:.4f}')    # Plot the results using a logarithmic scale for x-axis (number of flips)
    plt.figure(figsize=(10, 6))
    # Using semilogx for logarithmic x-scale to better visualize the range of flip counts
    plt.semilogx(n_flips_list, avg_probabilities, label='Average', marker='o')
    plt.semilogx(n_flips_list, max_probabilities, label='Maximum', linestyle='--', color='red', marker='x')
    plt.semilogx(n_flips_list, min_probabilities, label='Minimum', linestyle='--', color='green', marker='x')
    
    # Add a horizontal line at the true probability (0.54) for reference
    plt.axhline(y=0.54, color='black', linestyle='-', alpha=0.5, label='True P(head)=0.54')
    
    plt.xlabel('Number of Coin Flips (log scale)')
    plt.ylabel('Estimated Probability of Heads')
    plt.title('Estimating P(head) with Increasing Sample Sizes')
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)  # Grid lines for both major and minor ticks
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()
