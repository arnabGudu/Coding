#include "qtnode2.h"

///////////////////constructor/////////////////////////////
Node2::Node2(ros::NodeHandle _nh) : it(_nh)
{
	sub = it.subscribe("camera/image1", 1, &Node2::node1Callback, this);
	pub = it.advertise("camera/image2", 1);

	mh = 0;
	ms = 140;
	mv = 50;
	Mh = 40;
	Ms = 255;
	Mv = 255;

	namedWindow("trackbar");
	createTrackbar("mHue", "trackbar", &mh, 255, NULL);
	createTrackbar("MHue", "trackbar", &Mh, 255, NULL);	
	createTrackbar("mSat", "trackbar", &ms, 255, NULL);
	createTrackbar("MSat", "trackbar", &Ms, 255, NULL);
	createTrackbar("mVal", "trackbar", &mv, 255, NULL);
        createTrackbar("MVal", "trackbar", &Mv, 255, NULL);
}

///////////////////destructor/////////////////////////////
Node2::~Node2()
{
	destroyWindow("view");
	destroyWindow("trackbar");
}

////////////////////PERFORM///////////////////////////////
void Node2::perform()
{
	Mat hsv, blr;

	cvtColor(src, hsv, CV_BGR2HSV);
	blur(hsv, blr, Size(15,15));
	thres = blr;
	inRange(blr, Scalar(mh,ms,mv), Scalar(Mh,Ms,Mv), thres);
}

///////////////////SHOW///////////////////////////////////
void Node2::show()
{
	perform();
	//imshow("view", src);
	imshow("trackbar", thres);
	waitKey(10);
} 

////////////////////PUBLISH//////////////////////////////
void Node2::publish()
{
	msg = cv_bridge::CvImage(std_msgs::Header(), "mono8", thres).toImageMsg();
	pub.publish(msg);
}

//////////////////////CALLBACK//////////////////////////////
void Node2::node1Callback(const sensor_msgs::ImageConstPtr& _msg)
{
	try
	{	src = cv_bridge::toCvShare(_msg, "bgr8")->image;
		show();
		publish();

		std::cout<<"recieved"<<std::endl;
	}
	catch (cv_bridge::Exception& e)
	{
		std::cout<<"could not convert image"<<std::endl;
	}
}
