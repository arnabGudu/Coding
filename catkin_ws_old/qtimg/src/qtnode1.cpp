#include "qtnode1.h"

Node1::Node1(ros::NodeHandle _nh) : it(_nh), nh(_nh)
{
	state = 1;
	pub = it.advertise("camera/image1", 1);
	sub = nh.subscribe("power", 1000, &Node1::Callback, this);
}

void Node1::Callback(const std_msgs::Int32::ConstPtr& _msg)
{	
	state = !state;
}

