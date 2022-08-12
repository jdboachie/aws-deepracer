def reward_function(params):
    """
    This reward function rewards the model for staying on the track and moving fast on thre track.
    """
    
    # Getting the parameters used from the "params" dictionary
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params["speed"]
    
    # Setting the default value of the reward
    reward = 1
    
    # Setting the speed threshold. I expect that the deepracer keep an averages speed of about 1m/s
    SPEED_THRESHOLD = 1.0
    
    # Penalise the model if it goes off-track.
    if not all_wheels_on_track:
        reward = 1e-3
    elif speed > SPEED_THRESHOLD:
        reward *= 1e3
    # Maximum reward is given to the model if it stays on the track and moves quickly.
    else:
        reward = 1
    
    return float(reward)