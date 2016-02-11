#include "qtnode3.h"
#include <QApplication>
	
int main(int argc, char **argv)
{
	ros::init(argc, argv, "node3");
	ros::NodeHandle nh;

	QApplication a(argc, argv);
    	MainWindow w(nh);
    	w.show();
	
	Node3 n(nh);
	a.processEvents();
	ros::spin();
}
