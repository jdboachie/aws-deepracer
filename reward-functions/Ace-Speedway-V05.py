import math

global previous_reward, reward

previous_reward = 0

def reward_function(params):
    global previous_reward, reward
    if not params["all_wheels_on_track"]:
        reward = 1e-3
        return reward
    

    # Getting the parameters used in this reward function
    waypoints = params["waypoints"]
    closest_waypoints = params["closest_waypoints"]
    heading = params["heading"]
    speed = params["speed"]

    # Initializing the reward with its default value of 1.0
    reward = 1.0
    kp = 0.01
    
    # Initializing the threshold values for speed and direction
    DIRECTION_THRESHOLD = 7.0
    SPEED_THRESHOLD = 1.0

    # Calculating the speed difference
    speed_difference = SPEED_THRESHOLD - speed
    # Calculate the direction of the next waypoint
    next_waypoint = waypoints[closest_waypoints[1]]
    previous_waypoint = waypoints[closest_waypoints[0]] # These waypoints are lists with (x, y) format.

    route_dxn = math.atan2(next_waypoint[1]-previous_waypoint[1], next_waypoint[0]-previous_waypoint[0])
    route_dxn = math.degrees(route_dxn)

    # Calculating the difference between the route direction and the direction of the deepracer vehicle
    direction_difference = abs(heading-route_dxn)
    if direction_difference > 180:
      direction_difference = 360 - direction_difference

    reward = 1- (kp * direction_difference) - speed_difference 
    derivative = previous_reward - reward
    reward += derivative

    previous_reward = reward
    return reward