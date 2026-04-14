import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import time

class JointPublisher(Node):
    def __init__(self):
        super().__init__('joint_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.publish_joint_state)
        self.angle = 0.0

    def publish_joint_state(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        # URDF에 정의된 관절 이름과 정확히 일치해야 함 
        msg.name = ['wheel1_joint', 'wheel2_joint']
        self.angle += 0.1
        msg.position = [self.angle, self.angle]
        
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = JointPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
