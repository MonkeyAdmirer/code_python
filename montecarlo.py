# Problem: Estimating the Probability of Rolling a Sum Greater Than 8 with Two Dice
# We want to use the Monte Carlo method to estimate the probability that the sum of two 6-sided dice is greater than 8.

import random

def estimate_probability(num_trials):
    success_count = 0
    
    for _ in range(num_trials):
        die1 = random.randint(1, 6)  # Roll first die
        die2 = random.randint(1, 6)  # Roll second die
        
        if die1 + die2 > 8:
            success_count += 1
    
    probability = success_count / num_trials
    return probability

# Parameters for estimation
num_trials = 10000  # Number of trials to simulate

# Estimate the probability
estimated_probability = estimate_probability(num_trials)
print(f"Estimated Probability of Rolling a Sum Greater Than 8: {estimated_probability}")
