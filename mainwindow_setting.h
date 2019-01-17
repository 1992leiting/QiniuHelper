#ifndef MAINWINDOW_SETTING_H
#define MAINWINDOW_SETTING_H

#include <QMainWindow>

namespace Ui {
class MainWindow_setting;
}

class MainWindow_setting : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow_setting(QWidget *parent = nullptr);
    ~MainWindow_setting();

private:
    Ui::MainWindow_setting *ui;
};

#endif // MAINWINDOW_SETTING_H
