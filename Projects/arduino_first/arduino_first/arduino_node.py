import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

import serial  # 시리얼 통신 라이브러리


class ArduinoNode(Node):

    def __init__(self):
        super().__init__('arduino_node')

        # 🔥 포트 확인 필요 (/dev/ttyUSB0 or /dev/ttyACM0)
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)

        self.publisher_ = self.create_publisher(
            Float32,
            'sensor_data',
            10
        )

        # 계속 읽기
        self.timer = self.create_timer(1.0, self.read_serial)

    def read_serial(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').strip()

            try:
                value = float(line)

                msg = Float32()
                msg.data = value

                self.publisher_.publish(msg)

                self.get_logger().info(f'Arduino: {value}')

            except:
                self.get_logger().warn(f'Invalid data: {line}')


def main(args=None):
    rclpy.init(args=args)
    node = ArduinoNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
