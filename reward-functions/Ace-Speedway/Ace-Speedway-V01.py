import math
# import random
# import numpy
# import scipy
# import shapely

def reward_function(params):
    
    # Getting the parameters used in this reward function
    waypoints = params["waypoints"]
    closest_waypoints = params["closest_waypoints"]
    heading = params["heading"]
    speed = params["speed"]

    # Initializing the reward with its default value of 
    reward = 1.0
    
    # Initializing the threshold values for certain variables
    DIRECTION_THRESHOLD = 7.0
    SPEED_THRESHOLD = 2.5

    # Calculate the direction of the next waypoint
    next_waypoint = waypoints[closest_waypoints[1]]
    previous_waypoint = waypoints[closest_waypoints[0]] # These waypoints are lists with (x, y) format.

    route_dxn = math.atan2(next_waypoint[1]-previous_waypoint[1], next_waypoint[0]-previous_waypoint[0])
    route_dxn = math.degrees(route_dxn)

    # Calculating the difference between the route direction and the direction of the deepracer vehicle
    direction_difference = abs(heading-route_dxn)
    if direction_difference > 180:
      direction_difference = 360 - direction_difference

    
    if direction_difference > DIRECTION_THRESHOLD:
      reward *= 0.5
    elif speed < SPEED_THRESHOLD:
      reward *= 0.8

    return reward