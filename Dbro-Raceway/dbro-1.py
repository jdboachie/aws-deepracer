def reward_function(params):
    #############################################################################
    '''
    Complete the track in fewer steps
    '''

    # Read input variable
    steps = params['steps']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    STEPS_TO_COMPLETION = 300
    reward = 1.0

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1

    if not all_wheels_on_track:
        reward = 1e-3
    # Give additional reward if the car pass every 100 steps faster than expected
    elif (steps % 50) == 0 and progress > (steps / STEPS_TO_COMPLETION) * 100 :
        reward += 10.0

    return reward
