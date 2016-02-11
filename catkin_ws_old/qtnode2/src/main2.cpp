#define "qtnode2.h"

int main(int argc, char **argv)
{
	ros::init(argc, argv, "node2");
	ros::NodeHandle nh;
	Node2 n(nh);
	ros::spin();
}
