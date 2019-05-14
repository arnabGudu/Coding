#include "framer/framer.h"


std::string IMAGE_PATH = ros::package::getPath("framer") + "/utils/logo.jpeg";

Framer::Framer(QWidget *parent) :
	QMainWindow(parent),
	ui(new Ui::Framer)
{

	ui->setupUi(this);
	logo.load(IMAGE_PATH.c_str());
	int h = ui->logo_label->height(),w = ui->logo_label->width();
	ui->logo_label->setPixmap(logo.scaled(w,h,Qt::KeepAspectRatio));


	connect(ui->prev_frame,SIGNAL(pressed()),this,SLOT(show_prev_frame()));
	connect(ui->next_frame,SIGNAL(pressed()),this,SLOT(show_next_frame()));
	connect(ui->save_frame,SIGNAL(pressed()),this,SLOT(save_present_frame()));
}

Framer::~Framer()
{
	delete ui;
}


void Framer::show_next_frame(){
	count_proc++;
	ui->frame_proc->setText("eFrame processed: " + QString::number(count_proc));
	std::cout<<"next_button_pressed"<<std::endl;

}

void Framer::show_prev_frame(){
	count_proc--;
	ui->frame_proc->setText("Frame processed: " + QString::number(count_proc));
	std::cout<<"prev_button_pressed"<<std::endl;

}

void Framer::save_present_frame(){
	count_save++;
	ui->frame_save->setText("Frame saved: " + QString::number(count_save));

}

void Framer::frame_generator(){
	

}
