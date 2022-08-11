def reward_function(params):
    #############################################################################
    '''
    Complete the track in fewer steps
    '''

    # Read input variable
    steps = params['steps']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']

    STEPS_TO_COMPLETION = 300

    # Initialize the reward with typical value
    reward = 0.0

    if not all_wheels_on_track:
        reward = 1e-3
    # Give additional reward if the car pass every 100 steps faster than expected
    elif (steps % 100) == 0 and progress > (steps / STEPS_TO_COMPLETION) * 100 :
        reward += 3.0

    return reward
