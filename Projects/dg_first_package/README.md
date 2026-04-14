이 패키지는 ROS 2 Humble을 기반으로 노드 간의 기본적인 메시지 통신(Topic)을 구현한 예제입니다.

1. 개발 환경
OS: Ubuntu 22.04 LTS (VirtualBox)

ROS 2: Humble Hawksbill

Language: [C++ 또는 Python - 본인이 쓴 언어로 적으세요]

2. 시스템 아키텍처
본 패키지는 두 개의 노드로 구성되어 있으며, std_msgs/msg/String 타입의 토픽을 통해 데이터를 주고받습니다.

Talker (Publisher): "Hello ROS 2: [count]" 메시지를 일정 간격으로 발행합니다.

Listener (Subscriber): 발행된 메시지를 수신하여 터미널에 출력합니다.

3. 설치 및 빌드 방법
Bash
# 워크스페이스 이동 및 빌드
cd ~/ros2_wc
colcon build --packages-select dg_first_package

# 환경 설정 적용
source install/setup.bash
4. 실행 방법
두 개의 터미널을 열어 각각 실행합니다.

터미널 1 (Publisher):

Bash
ros2 run dg_first_package [talker_node_name]
터미널 2 (Subscriber):

Bash
ros2 run dg_first_package [listener_node_name]
