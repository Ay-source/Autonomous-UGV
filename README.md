# Autonomous-UGV
This is my project on simulating a fully autonomous UGV

Robot used: Husky a300 robot 

Steps:
1. Build the project from the ros2_ws directory
2. Source the ros2 workspace

Launching each package
- a300_description: can be launched using the launch file `view_robot.launch.py` by running:
```
ros2 launch a300_description view_robot_launch.py
```
- gazebo: launch process:
After launching the a300_description, in a new bash shell from the .ros2_ws/src/ folder run:
```
export $GAZEBO_SIM_RESOURCE_PATH="$PWD/src"
gz sim -r src/gazebo/worlds/sand_island_seabed/model.sdf
```
In a new bash shell, run
```
export $GAZEBO_SIM_RESOURCE_PATH="$PWD/src"
ros2 run ros_gz_sim create -topic robot_description -name a300
```