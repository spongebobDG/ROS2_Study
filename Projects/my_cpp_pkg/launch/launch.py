from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='my_cpp_pkg',
            executable='sensor_node',
            name='sensor_node',
            output='screen'
        ),

        Node(
            package='my_cpp_pkg',
            executable='processing_node',
            name='processing_node',
            output='screen'
        ),

        Node(
            package='my_cpp_pkg',
            executable='alert_node',
            name='alert_node',
            output='screen'
        ),
    ])