#ifndef NODE3_H
#define NODE3_H

#include "ros/ros.h"
#include "image_transport/image_transport.h"
#include "opencv2/opencv.hpp"
#include "cv_bridge/cv_bridge.h"
#include "std_msgs/Int32.h"
#include <QMainWindow>
#include <QPixmap>
#include "ui_framer.h"

namespace Ui {
class Node3;
}

class Node3 : public QMainWindow
{
	Q_OBJECT

public:
	explicit Node3(ros::NodeHandle _nh,QWidget *parent = 0);
	~Node3();
	//void callback(const std_msgs::Int32::ConstPtr& msg);

	void publish(int sig);
	void node1Callback(const sensor_msgs::ImageConstPtr& msg1);
	void node2Callback(const sensor_msgs::ImageConstPtr& msg2);

private:
	Ui::Node3 *ui;			//name of ui mainwindow is node3
	ros::NodeHandle nh;
	//ros::Subscriber sub;

	std_msgs::Int32 msg;
	ros::Publisher pub;

	image_transport::ImageTransport it;
	image_transport::Subscriber sub1;
	image_transport::Subscriber sub2;
};


#endif
