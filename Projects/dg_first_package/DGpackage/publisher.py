import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MyPublisher(Node):

    def __init__(self):
        super().__init__('DG_publisher')

        # Publisher 생성 (메시지 타입, 토픽, 큐)
        self.publisher_ = self.create_publisher(String, 'DGtopic', 10)

        # 1초마다 실행
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello DG'

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
