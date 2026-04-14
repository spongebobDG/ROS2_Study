cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 🔥 반드시 추가 (C++ ROS2 필수)
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# 🔥 여기 추가 (핵심)
add_executable(sensor_node src/sensor_node.cpp)

ament_target_dependencies(sensor_node
  rclcpp
  std_msgs
)

install(TARGETS
  sensor_node
  DESTINATION lib/${PROJECT_NAME}
)

add_executable(processing_node src/processing_node.cpp)

ament_target_dependencies(processing_node
  rclcpp
  std_msgs
)

install(TARGETS
  sensor_node
  processing_node
  DESTINATION lib/${PROJECT_NAME}
)

add_executable(alert_node src/alert_node.cpp)

ament_target_dependencies(alert_node
  rclcpp
  std_msgs
)

install(TARGETS
  sensor_node
  processing_node
  alert_node
  DESTINATION lib/${PROJECT_NAME}
)

# launch 폴더의 모든 내용을 설치 경로로 복사하는 설정
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# 테스트 부분은 그대로 둬도 됨
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()