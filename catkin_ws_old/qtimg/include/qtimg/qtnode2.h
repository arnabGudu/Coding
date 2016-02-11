#ifndef NODE2_H
#define NODE2_H

#include "ros/ros.h"
#include "opencv2/opencv.hpp"
#include "image_transport/image_transport.h"
#include "cv_bridge/cv_bridge.h"

using namespace cv;

class Node2
{
public:
	Node2(ros::NodeHandle _nh);
	~Node2();
	void node1Callback(const sensor_msgs::ImageConstPtr& msg);
	void publish();
	void show();

private:
	ros::NodeHandle nh;

	image_transport::ImageTransport it;
	image_transport::Subscriber sub;

	image_transport::Publisher pub;
	sensor_msgs::ImagePtr msg;

	int mh, ms, mv;
	int Mh, Ms, Mv;
	Mat src, thres; 

	void perform();
};

#endif
