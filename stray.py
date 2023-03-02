"""
The deepracer vehicle is guided to stay in the centre.
"""
from math import tanh

def reward_function(params):
    """
    The deepracer vehicle is guided to stay in the centre.
    """

    # Getting the parameters used in this reward function
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params["speed"]
    all_wheels_on_track = params["all_wheels_on_track"]

    # Initialize the reward with typical value
    reward = speed

    if not all_wheels_on_track:
        return 1e-3

    stray = tanh(track_width/2 - distance_from_center)
    reward = tanh((speed * 2) - stray)

    return max(reward, 0.000)