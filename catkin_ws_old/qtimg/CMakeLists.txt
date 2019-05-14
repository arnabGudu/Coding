cmake_minimum_required(VERSION 2.8.3)
project(qtimg)

find_package(catkin REQUIRED COMPONENTS
  OpenCV
  cv_bridge
  image_transport
  roscpp
  roslib
  sensor_msgs
  qt_build
)

find_package(Qt4 REQUIRED COMPONENTS QtCore QtGui)
include(${QT_USE_FILE})
include_directories(${CMAKE_CURRENT_BINARY_DIR})

include_directories(

  ${catkin_INCLUDE_DIRS}

)

file(GLOB QT_FORMS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} ui/*.ui)
set(QT_MOC include/qtnode1.h)
SET(QT_SOURCES src/qtnode1.cpp)

set(QT_MOC include/qtnode2.h)
SET(QT_SOURCES src/qtnode2.cpp)

set(QT_MOC include/qtnode3.h)
SET(QT_SOURCES src/qtnode3.cpp)

QT4_WRAP_UI(QT_FORMS_HPP ${QT_FORMS})
QT4_WRAP_CPP(QT_MOC_HPP ${QT_MOC})

include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
  ${QT_INCLUDE_DIRS}
)

add_library(qtimgLib ${QT_SOURCES} ${QT_FORMS_HPP} ${QT_MOC_HPP})
target_link_libraries(qtimgLib ${QT_LIBRARIES} ${catkin_LIBRARIES} ${OpenCV_LIBS} ${catkin_LIBRARIES}) 

add_executable(qtnode1 src/main1.cpp)
target_link_libraries(qtnode1 qtimgLib)

add_executable(qtnode2 src/main2.cpp)
target_link_libraries(qtnode2 qtimgLib)

add_executable(qtnode3 src/main3.cpp)
target_link_libraries(qtnode3 qtimgLib)
