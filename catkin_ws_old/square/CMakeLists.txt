cmake_minimum_required(VERSION 2.8.3)
project(square)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)


include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(node1 src/node1.cpp)
target_link_libraries(node1 ${catkin_LIBRARIES})


add_executable(node2 src/node2.cpp)
target_link_libraries(node2 ${catkin_LIBRARIES})


add_executable(node3 src/node3.cpp)
target_link_libraries(node3 ${catkin_LIBRARIES})

