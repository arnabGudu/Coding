cmake_minimum_required(VERSION 2.8.3)
project(ros_cvbridge)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  roscpp
  sensor_msgs
  std_msgs
)

find_package(OpenCV 3.2 REQUIRED)


include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

add_executable(node_cv src/node1.cpp)
target_link_libraries(node_cv ${catkin_LIBRARIES} ${OpenCV_LIBS}})
add_dependencies(node_cv ros_cvbridge_generate_messages_cpp)
