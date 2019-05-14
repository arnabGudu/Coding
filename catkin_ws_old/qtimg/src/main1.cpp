#include "qtnode1.h"

using namespace cv;

int main(int argc, char **argv)
{
	ros::init(argc, argv, "node1");
	ros::NodeHandle nh;	
	
	Node1 n(nh);
	
	//Mat image = imread(argv[1], CV_LOAD_IMAGE_COLOR);
	
	VideoCapture cap(0);
	ros::Rate r(10);
	
	while(ros::ok() && cap.isOpened())
	{	
		cap >> n.src;
		
		if (n.src.empty())
			break;

		n.publish();
		ros::spinOnce();
		r.sleep();
	}
	return 0;
}
