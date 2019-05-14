#ifndef NODE1_H
#define NODE1_H

#include "ros/ros.h"
#include "image_transport/image_transport.h"
#include "opencv2/opencv.hpp"
#include "cv_bridge/cv_bridge.h"
#include "std_msgs/Int32.h"

class Node1
{
public:
	Mat src;
	Node1(ros::NodeHandle _nh);
	void Callback(const std_msgs::Int32::ConstPtr& _msg);
	bool ok()
	{
		return state;
	}
	void publish()
	{
		msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", src).toImageMsg();
		
		if(ok())
			pub.publish(msg);
		
		std::cout<<state<<std::endl;
		waitKey(10);
	}
	
private:
	ros::NodeHandle nh;
	
	image_transport::ImageTransport it;
	image_transport::Publisher pub;
	sensor_msgs::ImagePtr msg;

	ros::Subscriber sub;
	bool state;
};

#endif

