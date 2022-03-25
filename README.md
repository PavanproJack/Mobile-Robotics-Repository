# Introduction to Mobile Robotics -- Wheeled Locomotion

Locomotion is the power of motion from place to place. Different kinds of Drive:

1. Differential Drive
2. Car Drive (Ackerman Steering)
3. Synchronous Drive (B21)
4. XR4000
5. Mecanum Wheels

### Differential Drive
It consists of 2 drive wheels
mounted on a common axis, and each wheel can independently being driven by their own motor either forward or backward . Sometimes there are other passive wheels that keep the robot from tipping
over.

One way robots have of determining their position in their environment is odometry. Odometry is the use of motion sensors to determine the robot's change in pose relative to some known pose.

Feedback:
A wheel encoder tracks how much a wheel turns. Given that information and wheel radius, we can detect how far the wheel has moved and how fast the wheel is moving.

