// sensor_node.cpp

#include "rclcpp/rclcpp.hpp"         // ROS2 C++ 핵심 라이브러리
#include "std_msgs/msg/float32.hpp" // 메시지 타입

#include <chrono>
#include <memory>
#include <cstdlib> // rand()

using namespace std::chrono_literals;

// Node 클래스 상속
class SensorNode : public rclcpp::Node
{
public:
    // 생성자
    SensorNode() : Node("sensor_node")
    {
        // Publisher 생성
        publisher_ = this->create_publisher<std_msgs::msg::Float32>(
            "sensor_data", 10);

        // 타이머 생성 (1초마다 실행)
        timer_ = this->create_wall_timer(
            1s,
            std::bind(&SensorNode::timer_callback, this)
        );
    }

private:
    // 타이머 콜백 함수
    void timer_callback()
    {
        auto msg = std_msgs::msg::Float32();

        // 랜덤 값 생성 (0~100)
        msg.data = rand() % 100;

        publisher_->publish(msg);

        RCLCPP_INFO(this->get_logger(), "Sensor: %.2f", msg.data);
    }

    // Publisher 변수
    rclcpp::Publisher<std_msgs::msg::Float32>::SharedPtr publisher_;

    // Timer 변수
    rclcpp::TimerBase::SharedPtr timer_;
};

// main 함수 (시작점)
int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    rclcpp::spin(std::make_shared<SensorNode>());

    rclcpp::shutdown();
    return 0;
}
