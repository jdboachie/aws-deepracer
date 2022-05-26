def reward_function(params):
    """
    This reward function rewards the model for staying left of the track.
    I'm attempting this because I realise that the left side of the track presents a faster opportunity 
    for the deepracer to complete the track.
    This is only theoretical.
    """
    
    # Getting the parameters used from the "params" dictionary
    all_wheels_on_track = params['all_wheels_on_track']
    is_left_of_center = params["is_left_of_center"]
    
    # Setting the default value of the reward
    reward = 1
    
    # Setting the speed threshold. I expect that the deepracer keep an averages speed of about 1m/s
    SPEED_THRESHOLD = 1.0
    
    # Penalise the model if it goes off-track.
    if not all_wheels_on_track:
        reward = 1e-3
    elif is_left_of_center:
        reward *= 2 #EV42 uses 2 and E4 uses 5
    else:
        reward = 0
    
    return float(reward)