// alert_node.cpp

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

#include <memory>

class AlertNode : public rclcpp::Node
{
public:
    AlertNode() : Node("alert_node")
    {
        // Subscriber 생성
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "alert",
            10,
            std::bind(&AlertNode::callback, this, std::placeholders::_1)
        );
    }

private:
    void callback(const std_msgs::msg::String::SharedPtr msg)
    {
        // 상태에 따라 로그 출력
        if (msg->data == "DANGER")
        {
            RCLCPP_ERROR(this->get_logger(), "🚨 DANGER!!!");
        }
        else if (msg->data == "WARNING")
        {
            RCLCPP_WARN(this->get_logger(), "⚠️ WARNING");
        }
        else
        {
            RCLCPP_INFO(this->get_logger(), "SAFE");
        }
    }

    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};


// main
int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    rclcpp::spin(std::make_shared<AlertNode>());

    rclcpp::shutdown();
    return 0;
}
