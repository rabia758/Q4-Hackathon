# Chapter 3: Robot Kinematics

Kinematics is the branch of mechanics that describes the motion of points, bodies, and systems of bodies without considering the forces that cause the motion.

## 3.1 Forward Kinematics
Forward kinematics is the process of calculating the position and orientation of the robot's end-effector (e.g., its hand) given the joint angles.

For a humanoid robot with many joints, we use the **Denavit-Hartenberg (DH) Convention** or **Screw Theory** to systematically calculate these transformations.

## 3.2 Inverse Kinematics (IK)
Inverse kinematics is the opposite: given the desired position and orientation of the hand, what should the joint angles be?

IK is much harder than forward kinematics because:
- There may be multiple solutions (e.g., you can reach a point with your elbow up or down).
- There may be no solution if the point is out of reach.
- The equations are non-linear.

## 3.3 The Jacobian Matrix
The Jacobian relates joint velocities to Cartesian velocities. It is essential for:
- Smooth motion control.
- Avoiding singular configurations (where the robot loses a degree of freedom).
- Mapping forces from the hand to the joints.