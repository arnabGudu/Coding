#include "ros/ros.h"
#include "std_msgs/Int32.h"

using namespace std;

void callBackNum(const std_msgs::Int32::ConstPtr& i)
{
	cout<<"Num : "<<i->data<<endl;
}

void callBackSq(const std_msgs::Int32::ConstPtr& i)
{
	cout<<"Square : "<<i->data<<endl;
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "node3");
	ros::NodeHandle n;
	ros::Subscriber sub1 = n.subscribe("num", 1000, callBackNum);
	ros::Subscriber sub2 = n.subscribe("square", 1000, callBackSq);

	ros::spin();
	return 0;
}


