def reward_function(params):
    """
    This reward function rewards the model for staying on the track and moving fast on thre track. It penalises for moving too far from the centre.
    """
    
    # Getting the parameters used from the "params" dictionary
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params["speed"]
    
    # Setting the default value of the reward
    reward = 1
    
    # Setting the speed threshold. I expect that the deepracer keep an averages speed of about 1m/s
    SPEED_THRESHOLD = 1.0
    
    # Penalise the model if it goes off-track.
    if not all_wheels_on_track:
        reward = 1e-3
    elif (track_width*0.5 - distance_from_center) <= 0.01:
        reward *= 0.5
    # If the model is on the track, penalise it for moving slowly
    elif speed < SPEED_THRESHOLD:
        reward *= 0.5
    # Maximum reward is given to the model if it stays on the track and moves quickly.
    else:
        reward = 1
    
    return float(reward)