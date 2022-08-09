def reward_function(params):
    #############################################################################
    '''
    Complete the track in fewer steps
    '''

    # Read input variable
    steps = params['steps']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']

    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 300

    # Initialize the reward with typical value
    reward = 1.0

    if not all_wheels_on_track :
        reward = 1e-3
    # Give additional reward if the car pass every 100 steps faster than expected
    elif (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 10.0

    return float(reward)
