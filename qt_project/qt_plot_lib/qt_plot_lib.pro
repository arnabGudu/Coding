#-------------------------------------------------
#
# Project created by QtCreator 2019-07-02T23:21:21
#
#-------------------------------------------------

QT       += widgets

TARGET = qt_plot_lib
TEMPLATE = lib

DEFINES += QT_PLOT_LIB_LIBRARY

SOURCES += qt_plot_lib.cpp

HEADERS += qt_plot_lib.h\
        qt_plot_lib_global.h

unix {
    target.path = /usr/lib
    INSTALLS += target
}
