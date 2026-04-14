import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan # LiDAR 데이터를 받기 위해 추가

class TurtleMover(Node):
    def __init__(self):
        super().__init__('turtle_mover')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        # LiDAR 데이터를 받기 위한 서브스크라이버 생성
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            10)
        self.msg = Twist()
        self.get_logger().info('장애물 회피 주행을 시작합니다!')

    def scan_callback(self, msg):
        # 정면(0도) 근처의 거리 데이터 추출 (인덱스 0~10, 350~359도)
        # LDS-03 센서 기준이며, 환경에 따라 인덱스는 다를 수 있음
        front_distance = min(msg.ranges[0:15] + msg.ranges[345:359])

        if front_distance < 0.5:  # 50cm 이내에 벽이 있다면
            self.get_logger().info(f'벽 감지! 거리: {front_distance:.2f}m - 회전합니다.')
            self.msg.linear.x = 0.0   # 정지
            self.msg.angular.z = 0.5  # 제자리 회전
        else:
            self.msg.linear.x = 0.15  # 전진
            self.msg.angular.z = 0.1  # 완만한 곡선으로 넓게 탐색
            
        self.publisher_.publish(self.msg)

def main():
    rclpy.init()
    node = TurtleMover()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        stop_msg = Twist()
        node.publisher_.publish(stop_msg)
        rclpy.shutdown()

if __name__ == '__main__':
    main()