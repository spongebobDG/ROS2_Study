import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class AlertNode(Node):

    def __init__(self):
        super().__init__('alert_node')

        self.subscription = self.create_subscription(
            String,
            'alert',
            self.callback,
            10
        )

    def callback(self, msg):
        # 위험 시 강조 출력
        if msg.data == 'DANGER':
            self.get_logger().warn(f'⚠️ WARNING: {msg.data}')
        else:
            self.get_logger().info(f'Status: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = AlertNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
