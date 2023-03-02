# AWS DeepRacer

This repository contains a collection of reward function code that can be used with AWS DeepRacer. The reward function is a critical component of a DeepRacer model as it determines how the car should be rewarded based on its actions in the simulation environment.

## Getting Started

To use the reward function code in this repository, follow these steps:

1. Clone the repository to your local machine.
2. In the AWS DeepRacer console, create a new model or select an existing one.
3. In the model settings, select the reward function option and choose "Custom reward function".
4. Copy and paste the contents of the reward function code into the editor.
5. Save the reward function and start a new training job.

## Reward Functions

The reward functions in this repository are designed to achieve specific objectives in the AWS DeepRacer simulation environment. Here is a list of the reward functions currently included in the repository:

1. progress.py : This reward function is designed to encourage the car to complete the track in as few steps as possible. The reward increases as the car progresses through the track, and additional rewards are given for reaching certain checkpoints.

2. stray.py : This reward function is designed to encourage the car to stay near the center of the track. The closer the car is to the center, the higher the reward. The reward decreases as the car moves away from the center line.

3. waypoints.py : This reward function is designed to encourage the car to follow a specific path through the track. The reward increases as the car passes through specific waypoints on the track.

## Contributing

If you have a reward function that you would like to contribute to this repository, feel free to create a pull request. Please ensure that your reward function is well-documented and thoroughly tested before submitting.

## License

This repository is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgements

The reward functions in this repository are inspired by various sources, including the AWS DeepRacer documentation, community forums, and research papers. Special thanks to the AWS DeepRacer team for creating such a fun and engaging platform for reinforcement learning!