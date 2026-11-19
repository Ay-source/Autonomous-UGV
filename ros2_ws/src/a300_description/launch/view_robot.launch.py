#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Adapted for the trimmed a300_description package (base platform only --
# chassis, top plate, suspension, wheels/drivetrain). The full MYBOTSHOP
# hsky_description repo builds robot_description at runtime from
# augments.urdf.xacro (which also layers in accessory sensors and the
# optional xArm850 manipulator via env vars); this package ships a single
# pre-flattened urdf/a300.urdf for the base platform instead, so no xacro
# processing or extra `hsky_viz` package is required to view it.

from launch_ros.actions import Node
from launch import LaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="cat")]),
            " ",
            PathJoinSubstitution(
                [FindPackageShare("a300_description"), "urdf", "a300.urdf"]
            ),
        ]
    )

    robot_description = {
        "robot_description": ParameterValue(
            robot_description_content,
            value_type=str
        )
    }
"""
    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    node_joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
        output="screen",
    )
"""
    node_rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
    )

    ld = LaunchDescription()
    ld.add_action(node_robot_state_publisher)
    ld.add_action(node_joint_state_publisher_gui)
    ld.add_action(node_rviz)

    return ld
