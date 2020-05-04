
'''
A robot is located at x = 1.0 m, y = 0.5 m, θ = pi/4. Its laser range finder is mounted
on the robot at x = 0.2 m, y = 0.0 m, θ = π with respect to the robot’s frame of
reference.
The distance measurements of one laser scan can be found in the file laserscan.dat,
which is provided on the website of this lecture. The first distance measurement is
taken in the angle α = −pi/2
(in the frame of reference of the laser range finder), the
last distance measurement has α = pi/2
(i.e., the field of view of the sensor is π), and
all neighboring measurements are in equal angular distance (all angles in radians).
'''


import numpy as np 
import math
import matplotlib.pyplot as plt 


# Load the Laser scan data file
scan = np.loadtxt('txtFile.dat')
angle = np.linspace(-math.pi/2, math.pi/2,
np.shape(scan)[0], endpoint='true')

# Laser end-points in the laser frame of reference
x_laser_co = scan * np.cos(angle)
y_laser_co = scan * np.sin(angle)

# Plot all laser end-points in the frame of reference of the laser range finder

fig = plt.figure()
plt.plot(x_laser_co,y_laser_co, '.')
plt.show()

# Homogeneous Transformation matrix of Robot frame w.r.t to Global frame
g_T_O = np.array([[np.cos(math.pi/4), -np.sin(math.pi/4), 1], [np.sin(math.pi/4), np.cos(math.pi/4), 0.5], [0, 0, 1]])

# Homogeneous Transformation matrix of Laser frame w.r.t to Robot frame
O_T_S = np.array([[np.cos(math.pi), -np.sin(math.pi), 0.2], [np.sin(math.pi), np.cos(math.pi), 0], [0, 0, 1]])

# Homogeneous Transformation matrix of Laser frame w.r.t to global frame
g_T_S = g_T_O.dot(O_T_S)

global_laser_center_x, global_laser_center_y = g_T_S[0, 2], g_T_S[1, 2] 

global_robot_x, global_robot_y = g_T_O[0, 2], g_T_O[1, 2]

laserEndPoints = np.array([x_laser_co, y_laser_co, np.ones(np.shape(x_laser_co)[0]) ])

print(laserEndPoints)

global_laser_x, global_laser_y = g_T_S.dot(laserEndPoints)[0, :], g_T_S.dot(laserEndPoints)[1, :]

fig = plt.figure()

# Plot the Laser end points w.r.t Global Frame of reference
plt.plot(global_laser_x, global_laser_y, '.')

#Mark the Robot center in Blue
plt.plot(global_robot_x, global_robot_y, '+b')
#Mark the Laser center in Red
plt.plot(global_laser_center_x, global_laser_center_y, '+r')
plt.show()









