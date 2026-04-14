import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


class ProcessingNode(Node):

    def __init__(self):
        super().__init__('processing_node')

        # 센서 데이터 구독
        self.subscription = self.create_subscription(
            Float32,
            'sensor_data',
            self.callback,
            10
        )

        # 결과 퍼블리셔
        self.publisher_ = self.create_publisher(
            String,
            'alert',
            10
        )

    def callback(self, msg):
        value = msg.data

        result = String()

        # 기준값 설정 (예: 50 이상 위험)
        if value > 50:
            result.data = 'DANGER'
        else:
            result.data = 'SAFE'

        self.publisher_.publish(result)

        self.get_logger().info(f'Processed: {value} → {result.data}')


def main(args=None):
    rclpy.init(args=args)
    node = ProcessingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
