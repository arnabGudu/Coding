#include "ros/ros.h"
#include "std_msgs/Int32.h"

using namespace std;

class node2
{
public:
	node2()
	{
		pub = n.advertise<std_msgs::Int32>("square", 1000);
		sub = n.subscribe("num", 1000, callBack, this);
	}
	void callBack(const std_msgs::Int32::ConstPtr& i)
	{	std_msgs::Int32 j;
		j.data = i->data * i->data;
	
		cout<<"Num : "<<i->data<<endl;	
		pub.publish(j);
	}
private:
	ros::NodeHandle n;
	ros::Publisher pub;
	ros::Subscriber sub;
};

int main(int argc, char **argv)
{
	ros::init(argc, argv, "node2");
	node2 n2;
	ros::spin();
	return 0;
}
