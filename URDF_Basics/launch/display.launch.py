import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # 패키지 이름에 맞춰 수정하세요
    pkg_name = 'my_urdf_package'
    urdf_file = os.path.join(get_package_share_directory(pkg_name), 'urdf', 'jdamr.urdf')

    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        # 1. robot_state_publisher: URDF를 파싱하여 TF 정보를 발행
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}]
        ),
        # 2. joint_state_publisher_gui: GUI 슬라이더로 관절 제어
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),
        # 3. rviz2: 시각화 도구
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', os.path.join(get_package_share_directory(pkg_name), 'rviz', 'config.rviz')]
        )
    ])
