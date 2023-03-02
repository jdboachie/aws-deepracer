""" 
Baguette
````````
A baguette is a long, thin type of bread of French origin that is commonly
made from basic lean dough. It is distinguishable by its length and crisp
crust.
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
    if reward <= 0:
        reward = 0.000

    return reward