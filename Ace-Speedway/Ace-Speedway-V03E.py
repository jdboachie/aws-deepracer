import math

def reward_function(params):
    """
    In this version of the Ace Speedway reward function:
    
    1. The model is punished for:
    * Not steering too much
    * speeding up

    The model is initially given a reward of 1. Its "wrong deeds" reduce the reward.

    In version three, the model is built with SAC(Soft Actor Critic) Algorithm.
    """
    
    # Getting the parameters used in this reward function
    waypoints = params["waypoints"]
    closest_waypoints = params["closest_waypoints"]
    heading = params["heading"]
    speed = params["speed"]

    # Initializing the reward with its default value of 1.0
    reward = 1.0
    
    # Initializing the threshold values for direction and speed
    DIRECTION_THRESHOLD = 14 # My current research is into the direction threshold effect on model performance (specifically speed)
    SPEED_THRESHOLD = 1.0

    # Calculate the direction of the next waypoint
    next_waypoint = waypoints[closest_waypoints[1]]
    previous_waypoint = waypoints[closest_waypoints[0]] # These waypoints are lists with (x, y) format.

    route_dxn = math.atan2(next_waypoint[1]-previous_waypoint[1], next_waypoint[0]-previous_waypoint[0])
    route_dxn = math.degrees(route_dxn)

    # Calculating the difference between the route direction and the direction of the deepracer vehicle
    direction_difference = abs(heading-route_dxn)
    if direction_difference > 180:
      direction_difference = 360 - direction_difference

    # The reward is cut in half the deepracer veers too much (its turn angle is excessive).
    if direction_difference > DIRECTION_THRESHOLD:
      reward *= 0.5
    elif speed < SPEED_THRESHOLD:
      reward *= 0.5

    return reward