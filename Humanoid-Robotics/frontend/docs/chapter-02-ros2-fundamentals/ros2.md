---
id: ros2
title: "Chapter 2: ROS 2 Fundamentals"
---
# Chapter 2: ROS 2 Fundamentals (The Robotic Nervous System)

## Focus: Middleware for robot control
ROS 2 (Robot Operating System) serves as the "nervous system" of our humanoid robot, handling the communication between different software components (nodes).

---

## 2.1 ROS 2 Architecture and Core Concepts
Unlike its predecessor, ROS 2 is built on DDS (Data Distribution Service), providing a robust, industrial-grade communication framework.

### Key Concepts:
- **Nodes:** Single-purpose executable programs (e.g., one node for the camera, one for the motor controller).
- **Topics:** A bus over which nodes exchange messages (Publisher/Subscriber model).
- **Services:** A Request/Response communication pattern for synchronous tasks.
- **Actions:** For long-running tasks with feedback (e.g., "Walk to the kitchen").

---

## 2.2 Building ROS 2 Packages with Python
Students will learn to create custom ROS 2 packages using `rclpy`.

### Workspace Structure:
```bash
dev_ws/
└── src/
    └── humanoid_control/
        ├── package.xml
        ├── setup.py
        └── humanoid_control/
            ├── __init__.py
            └── controller_node.py
```

---

## 2.3 Bridging Python Agents to ROS Controllers
One of the core skills in this module is connecting high-level AI agents (written in Python) to low-level robot controllers.
- Using `rclpy` to publish velocity commands.
- Subscribing to sensor data to inform AI decision-making.

---

## 2.4 Understanding URDF for Humanoids
The **Unified Robot Description Format (URDF)** is an XML file that describes the physical structure of the robot.
- **Links:** The "bones" of the robot (arms, legs, torso).
- **Joints:** The "articulations" (elbows, knees, hips) including their limits and types (revolute, fixed).
- **Visual vs. Collision:** Defining how the robot looks vs. how it interacts with the physical world.

---

## 2.5 Launch Files and Parameter Management
Learn to use Python-based launch files to start complex systems with multiple nodes and manage configurations using YAML parameters.

---

## Learning Outcomes:
- Design and implement a multi-node ROS 2 system.
- Create custom URDF models for humanoid structures.
- Master the rclpy library for AI-to-Robot bridging.
