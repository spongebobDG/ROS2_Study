# launch 시스템에서 사용하는 클래스
from launch import LaunchDescription

# ROS2 노드를 실행하기 위한 클래스
from launch_ros.actions import Node


# launch 파일의 시작점 (main 같은 역할)
def generate_launch_description():

    return LaunchDescription([

        # Publisher 노드 실행

        Node(
            package = 'arduino_first',
            executable = 'arduino',
            name = 'arduino_first_node',
            output = 'screen',
        ),
        
        Node(package='arduino_first', executable='processing'),

        Node(package='arduino_first', executable='alert'),
    ])
