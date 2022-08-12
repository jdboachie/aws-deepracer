global reward
reward = 0

def reward_function(params):
    #############################################################################
    '''
    Complete the track in fewer steps
    '''
    global reward

    # Read input variable
    steps = params['steps']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']

    STEPS_TO_COMPLETION = 300

    if not all_wheels_on_track:
        reward = 1e-3
    # Give additional reward if the car pass every 100 steps faster than expected
    elif (steps % 100) == 0 and progress > (steps / STEPS_TO_COMPLETION) * 100 :
        reward += 1.0

    return reward
