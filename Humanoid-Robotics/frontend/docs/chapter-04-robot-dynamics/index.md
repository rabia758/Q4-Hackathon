# Chapter 4: Robot Dynamics

While kinematics describes *how* a robot moves, dynamics describes the *forces* and *torques* required to create that motion.

## 4.1 Inertial Properties
Every link of a humanoid robot has:
- **Mass**: The amount of matter.
- **Center of Mass (CoM)**: The point where the weight is concentrated.
- **Inertia Tensor**: Describes how the mass is distributed around the axes of rotation.

## 4.2 Equations of Motion
We use two main methods to derive the equations of motion:
1. **Newton-Euler Formulation**: Based on force and moment balance for each link. It is computationally efficient for real-time control.
2. **Lagrangian Formulation**: Based on the energy of the system. It provides a more structured form of the equations, useful for analysis.

## 4.3 Gravity Compensation
For a humanoid robot to stand or move smoothly, the motors must provide enough torque to counteract gravity. This is called gravity compensation.

## 4.4 Contact Dynamics
Humanoid robots are constantly in contact with the ground. Understanding the forces at the feet (Ground Reaction Forces) is critical for maintaining balance and preventing the robot from falling.