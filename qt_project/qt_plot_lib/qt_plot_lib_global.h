#ifndef QT_PLOT_LIB_GLOBAL_H
#define QT_PLOT_LIB_GLOBAL_H

#include <QtCore/qglobal.h>

#if defined(QT_PLOT_LIB_LIBRARY)
#  define QT_PLOT_LIBSHARED_EXPORT Q_DECL_EXPORT
#else
#  define QT_PLOT_LIBSHARED_EXPORT Q_DECL_IMPORT
#endif

#endif // QT_PLOT_LIB_GLOBAL_H
