import math

def reward_function(params):
    """
    I call this model the second waypoint algorithm.
    It uses the second closest waypoint for the deepracer's navigation.
    I expect it to be faster than the closest waypoint version since there'll be more straight lines
    """
    
    # Getting the parameters used in this reward function
    waypoints = params["waypoints"]
    closest_waypoints = params["closest_waypoints"]
    heading = params["heading"]
    speed = params["speed"]

    # Initializing the reward with its default value of 1.0
    reward = 1.0
    
    # Initializing the threshold values for direction and speed
    DIRECTION_THRESHOLD = 7
    SPEED_THRESHOLD = 1.0

    # Calculate the direction of the next waypoint
    try:
        next_waypoint = waypoints[closest_waypoints[1] +3]
    except:
        next_waypoint = waypoints[closest_waypoints[1]]
    finally:
        previous_waypoint = waypoints[closest_waypoints[0]-3] # These waypoints are lists with (x, y) format.

    # In the above two lines of code, I've edited to point the next and previous waypoints one step forwards and backwards

    route_dxn = math.atan2(next_waypoint[1]-previous_waypoint[1], next_waypoint[0]-previous_waypoint[0])
    route_dxn = math.degrees(route_dxn)

    # Calculating the difference between the route direction and the direction of the deepracer vehicle
    direction_difference = abs(heading-route_dxn)
    if direction_difference > 180:
      direction_difference = 360 - direction_difference

    # The reward is cut in half the deepracer veers too much (its turn angle is excessive).
    if direction_difference > DIRECTION_THRESHOLD:
      reward *= 0.5


    return reward