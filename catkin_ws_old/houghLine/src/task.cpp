#include "opencv2/opencv.hpp"

using namespace cv;

Mat src,hsv,thresh,blr;
int h=0,s=0,v=0;
int mh=255,ms=255,mv=255;

void createtrackbar()
{
	namedWindow("threshold");
	createTrackbar("h","threshsold",&h,255,NULL);
	createTrackbar("mh","threshsold",&mh,255,NULL);
	createTrackbar("s","threshsold",&s,255,NULL);
	createTrackbar("ms","threshsold",&ms,255,NULL);
	createTrackbar("v","threshsold",&v,255,NULL);
	createTrackbar("mv","threshsold",&mv,255,NULL);
}

void show(){
	imshow("original", src);
	imshow("blur" ,blr);
	imshow("threshold",thresh);
}

void perform(){
	
        cvtColor(src, hsv, CV_BGR2HSV);
	blur(hsv, blr, Size(10,10));
	inRange(blr, Scalar(h, s, v), Scalar(mh, ms, mv), thresh);
}

int main(int argc, char **argv)
{
	VideoCapture cap(argv[1]);

	if (!cap.isOpened())
		return -1;

	createtrackbar();

	while (cap.isOpened())
	{
		cap >> src;

		if (src.empty())
			break;

	
		int k=waitKey(10);

		if (k==' ')
			while((k=waitKey(10)) != ' ')
			{
				if (k=='q')	return 0;
				perform();
				show();
			}

		else if(k=='q')
			return 0;

		perform();
		show();
	}
}
	
	
