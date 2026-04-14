// processing_node.cpp

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float32.hpp"
#include "std_msgs/msg/string.hpp"

#include <memory>

class ProcessingNode : public rclcpp::Node
{
public:
    ProcessingNode() : Node("processing_node")
    {
        // 🔥 Subscriber 생성
        subscription_ = this->create_subscription<std_msgs::msg::Float32>(
            "sensor_data",
            10,
            std::bind(&ProcessingNode::callback, this, std::placeholders::_1)
        );

        // 🔥 Publisher 생성
        publisher_ = this->create_publisher<std_msgs::msg::String>(
            "alert",
            10
        );
    }

private:
    // 🔥 콜백 함수 (메시지 받으면 실행됨)
    void callback(const std_msgs::msg::Float32::SharedPtr msg)
    {
        float value = msg->data;

        auto result = std_msgs::msg::String();

        // 🔥 판단 로직
        if (value > 70)
        {
            result.data = "DANGER";
        }
        else if (value > 40)
        {
            result.data = "WARNING";
        }
        else
        {
            result.data = "SAFE";
        }

        publisher_->publish(result);

        RCLCPP_INFO(this->get_logger(),
                    "Processed: %.2f → %s",
                    value,
                    result.data.c_str());
    }

    // Subscriber 변수
    rclcpp::Subscription<std_msgs::msg::Float32>::SharedPtr subscription_;

    // Publisher 변수
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
};


// main 함수
int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    rclcpp::spin(std::make_shared<ProcessingNode>());

    rclcpp::shutdown();
    return 0;
}