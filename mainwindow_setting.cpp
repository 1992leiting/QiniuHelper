#include "mainwindow_setting.h"
#include "ui_mainwindow_setting.h"

MainWindow_setting::MainWindow_setting(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow_setting)
{
    ui->setupUi(this);
}

MainWindow_setting::~MainWindow_setting()
{
    delete ui;
}
