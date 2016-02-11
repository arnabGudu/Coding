#include "qtnode3.h"
#include "ui_mainwindow.h"	

Node3::Node3(ros::NodeHandle _nh, QWidget *parent) : QMainWindow(parent), ui(new Ui::Node3), nh(_nh)
{
	ui->setupUi(this);
	//sub = nh.subscribe("numbers", 1, &MainWindow::callback, this);

	pub = nh.advertise<std_msgs::Int32>("power", 1000);
	sub1 = it.subscribe("camera/image1", 1, &Node3::node1Callback, this);
	sub2 = it.subscribe("camera/image2", 1, &Node3::node2Callback, this);
	
	connect(ui->prev_frame,SIGNAL(pressed()),this,SLOT(start()));
	connect(ui->next_frame,SIGNAL(pressed()),this,SLOT(stop()));
}

MainWindow::~MainWindow()
{
	delete ui;
}

/*void MainWindow::callback(const sensor_msgs::ImageConstPtr& msg1)
{
	ui->lcd->display(msg->data);
}*/


void Node3::node1Callback(const sensor_msgs::ImageConstPtr& msg1)
{
	try 
	{
		ui->label_node1->setPixmap(logo.scaled(w,h,Qt::KeepAspectRatio));
		//imshow("node_1", cv_bridge::toCvShare(msg1, "bgr8")->image);
		int k = waitKey(10);
		if (k == ' ')	
			publish(0);
	}
	catch (cv_bridge::Exception& e)
	{
		std::cout<<"could not receive node1 image"<<std::endl;
	}
}

void Node3::node2Callback(const sensor_msgs::ImageConstPtr& msg2)
{
        try 
	{
		ui->label_node2->setPixmap(logo.scaled(w,h,Qt::KeepAspectRatio));
                //imshow("node_2", cv_bridge::toCvShare(msg2, "mono8")->image);
                int k = waitKey(10);
		
	}
        catch (cv_bridge::Exception& e)
        {
		std::cout<<"could not receive node2 image"<<std::endl;
	}
}	

void Node3::publish(int sig)
{	
	msg.data = sig;
	pub.publish(msg);
}

