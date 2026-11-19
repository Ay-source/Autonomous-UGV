import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Replace 'my_robot_description' and 'robot.urdf' with your actual names
    pkg_share = get_package_share_directory('a300_description')
    urdf_file_path = os.path.join(pkg_share, 'urdf', 'a300.urdf')

    # Read the plain URDF file directly into a string
    with open(urdf_file_path, 'r') as infp:
        robot_desc = infp.read()

    # 1. Publishes the robot's TF transforms
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_desc}]
    )

    # 2. Opens joint sliders for non-fixed joints
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

    # 3. Launches a blank RViz2 window
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])
