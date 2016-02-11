cmake_minimum_required(VERSION 2.8.3)
project(taskrosqt)


find_package(catkin REQUIRED COMPONENTS
  OpenCV
  qt_build
  roscpp
  std_msgs
)

## System dependencies are found with CMake's conventions
find_package(Qt4 REQUIRED COMPONENTS QtCore QtGui)
include(${QT_USE_FILE})
include_directories(${CMAKE_CURRENT_BINARY_DIR})

################################################
## Find files 
################################################
file(GLOB QT_FORMS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} ui/*.ui)
set(QT_MOC include/mainwindow.h)
SET(QT_SOURCES src/mainwindow.cpp)

################################################
## Setup QT
################################################
QT4_WRAP_UI(QT_FORMS_HPP ${QT_FORMS})
QT4_WRAP_CPP(QT_MOC_HPP ${QT_MOC})


###################################
## catkin specific configuration ##
###################################
catkin_package()

###########
## Build ##
###########
include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
	${QT_INCLUDE_DIRS}
)

add_library(appLib ${QT_SOURCES} ${QT_FORMS_HPP} ${QT_MOC_HPP})
target_link_libraries(appLib ${QT_LIBRARIES} ${catkin_LIBRARIES})

add_executable(node2qt src/node2.cpp)
target_link_libraries(node2qt appLib)

add_executable(node3qt src/node3.cpp)
target_link_libraries(node3qt appLib)

add_library(Node1 include/tiburon_trainees_2019/task1/node1.h src/task1/node1.cpp)
add_executable(node1 src/task1/node1_creator.cpp)
target_link_libraries(node1 Node1 ${catkin_LIBRARIES})
add_dependencies(node1 Node1 ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

