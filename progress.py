"""_summary_: This is a reward function that rewards the agent
    for staying in the center of the track
    and for completing the track in fewer steps.
"""

from math import tanh, sin

def reward_function(params):
    '''
    Reward function that encourages the car to stay close to the center line
    and complete the track in fewer steps.
    '''

    # Read input variables
    steps = params.get('steps', 0)
    progress = params.get('progress', 0)
    all_wheels_on_track = params.get('all_wheels_on_track', False)
    track_width = params.get('track_width', 0)
    distance_from_center = params.get('distance_from_center', 0)

    # Define constants
    inner_lane_boundary = 0.1 * track_width
    mid_lane_boundary = 0.25 * track_width
    outer_lane_boundary = 0.5 * track_width
    steps_to_completion = 300

    # Calculate reward based on distance from center line
    if distance_from_center <= inner_lane_boundary:
        reward = 1.0
    elif distance_from_center <= mid_lane_boundary:
        reward = 0.5
    elif distance_from_center <= outer_lane_boundary:
        reward = 0.1
    else:
        reward = 0.01  # Penalize if too far from center line
    reward *= (1.0 - (distance_from_center / inner_lane_boundary))
    # Penalize if car is off track
    if not all_wheels_on_track:
        reward *= 1e-3

    # Give additional reward if car completes track faster than expected
    elif (steps % 50) == 0 and progress > (steps / steps_to_completion) * 100:
        reward *= progress

    return tanh(reward)
