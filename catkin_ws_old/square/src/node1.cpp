#include "ros/ros.h"
#include "std_msgs/Int32.h"

int main(int argc, char **argv)
{
	ros::init(argc, argv, "node1");
	ros::NodeHandle n;
	ros::Publisher p = n.advertise<std_msgs::Int32>("num",1000);
	ros::Rate r(10);

	int count = 0;
	
	while(ros::ok())
	{
		std_msgs::Int32 i;
		i.data = count;
		p.publish(i);
		ROS_INFO("Send %d", i.data);
		ros::spinOnce();
		r.sleep();
		count++;
	}
	return 0;
}

