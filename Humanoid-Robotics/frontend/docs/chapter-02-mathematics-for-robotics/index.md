# Chapter 2: Mathematics for Robotics

Robotics is fundamentally about describing the position, orientation, and motion of objects in space. To build a humanoid robot, you must be fluent in the language of mathematics.

This chapter covers the essential mathematical tools needed for robot kinematics, dynamics, and control.

## 2.1 Linear Algebra
Linear algebra is the most important mathematical tool for a roboticist. It allows us to represent positions and rotations using **vectors** and **matrices**.

### Vectors
A vector represents a quantity with both magnitude and direction.
*   **Position Vector**: Describes the location of a point in 3D space (e.g., $(x, y, z)$).
*   **Velocity Vector**: Describes how fast an object is moving and in what direction.

### Matrices
Matrices are rectangular arrays of numbers used to perform transformations.
*   **Rotation Matrix**: Represents the orientation of a rigid body relative to a reference frame.
*   **Transformation Matrix**: Combines rotation and translation into a single $4 \times 4$ matrix.

## 2.2 Coordinate Transformations
Robots are made of many rigid links connected by joints. Each link has its own coordinate frame. To control the robot, we must transform coordinates from one frame to another.

### Homogeneous Coordinates
We use homogeneous coordinates to represent points and vectors in a unified way. A 3D point $(x, y, z)$ is represented as a 4D vector $(x, y, z, 1)$.

$$ 
T = \begin{bmatrix}
 R & p \\ 0 & 1
\end{bmatrix}
$$ 

where $R$ is a $3 \times 3$ rotation matrix and $p$ is a $3 \times 1$ translation vector.

## 2.3 Calculus
Calculus is essential for understanding motion and optimization.

### Derivatives
*   **Velocity**: The rate of change of position with respect to time ($v = \frac{dx}{dt}$). 
*   **Acceleration**: The rate of change of velocity with respect to time ($a = \frac{dv}{dt}$). 
*   **Jacobian Matrix**: A matrix of partial derivatives that relates joint velocities to end-effector velocities.

### Optimization
Robots often need to find the "best" solution to a problem, such as the shortest path or the most energy-efficient motion. This involves minimizing a cost function using techniques like **Gradient Descent**.

## 2.4 Probability and Statistics
Robots operate in the real world, which is inherently uncertain. Sensors are noisy, and models are imperfect.

### Probability Distributions
*   **Gaussian Distribution**: Often used to model sensor noise.
*   **Bayes' Theorem**: A fundamental rule for updating beliefs based on new evidence.

### State Estimation
Techniques like the **Kalman Filter** and **Particle Filter** use probability to estimate the robot's true state (position, velocity) from noisy sensor measurements.

## Summary
Understanding these mathematical concepts is crucial for the chapters ahead.
*   **Kinematics** relies heavily on **Linear Algebra** and **Trigonometry**.
*   **Dynamics** uses **Calculus** and **Differential Equations**.
*   **Perception** and **Localization** depend on **Probability and Statistics**.
