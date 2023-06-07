"""_summary_: this  visualises the reward function by generating random
    "params" dictionaries and evaluating the reward function for each one.
"""
import random
from src.waypoints import reward_function

def generate_random_params():
    '''
    Generates a random "params" dictionary for the DeepRacer simulator.
    '''
    random_params = {
        'steps': random.randint(1, 1000),
        'speed': random.uniform(0, 1.5),
        'progress': random.uniform(0, 100),
        'all_wheels_on_track': random.choice([True, False]),
        'track_width': random.uniform(1, 10),
        'distance_from_center': random.uniform(0, 0.5),
    }
    return random_params

# Evaluate the reward for a random "params" dictionary
for i in range(50):
    params = generate_random_params()
    REWARD = reward_function(params)
    print(f"Reward: {REWARD}")
