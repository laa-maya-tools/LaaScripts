try:
    from PySide6 import QtCore, QtGui, QtWidgets
    from shiboken6 import wrapInstance
    _v = 6
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets
    from shiboken2 import wrapInstance
    _v = 2

if _v == 6:
    Qt_Unchecked           = QtCore.Qt.CheckState.Unchecked
    Qt_PartiallyChecked    = QtCore.Qt.CheckState.PartiallyChecked
    Qt_Checked             = QtCore.Qt.CheckState.Checked
    Qt_ArrowCursor         = QtCore.Qt.CursorShape.ArrowCursor
    Qt_PointingHandCursor  = QtCore.Qt.CursorShape.PointingHandCursor
    Qt_IBeamCursor         = QtCore.Qt.CursorShape.IBeamCursor
    Qt_FramelessWindowHint = QtCore.Qt.WindowType.FramelessWindowHint
    Qt_AlignCenter         = QtCore.Qt.AlignmentFlag.AlignCenter
    Qt_red                 = QtCore.Qt.GlobalColor.red
    Qt_green               = QtCore.Qt.GlobalColor.green
    Qt_yellow              = QtCore.Qt.GlobalColor.yellow
    Qt_blue                = QtCore.Qt.GlobalColor.blue
    QSP_Fixed              = QtWidgets.QSizePolicy.Policy.Fixed
    QSP_Minimum            = QtWidgets.QSizePolicy.Policy.Minimum
    QSP_Expanding          = QtWidgets.QSizePolicy.Policy.Expanding
    QMB_Ok                 = QtWidgets.QMessageBox.StandardButton.Ok
    QMB_Yes                = QtWidgets.QMessageBox.StandardButton.Yes
    QMB_No                 = QtWidgets.QMessageBox.StandardButton.No
    Qt_UserRole            = QtCore.Qt.ItemDataRole.UserRole
    QAV_SingleSelection    = QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
else:
    Qt_Unchecked           = QtCore.Qt.Unchecked
    Qt_PartiallyChecked    = QtCore.Qt.PartiallyChecked
    Qt_Checked             = QtCore.Qt.Checked
    Qt_ArrowCursor         = QtCore.Qt.ArrowCursor
    Qt_PointingHandCursor  = QtCore.Qt.PointingHandCursor
    Qt_IBeamCursor         = QtCore.Qt.IBeamCursor
    Qt_FramelessWindowHint = QtCore.Qt.FramelessWindowHint
    Qt_AlignCenter         = QtCore.Qt.AlignCenter
    Qt_red                 = QtCore.Qt.red
    Qt_green               = QtCore.Qt.green
    Qt_yellow              = QtCore.Qt.yellow
    Qt_blue                = QtCore.Qt.blue
    QSP_Fixed              = QtWidgets.QSizePolicy.Fixed
    QSP_Minimum            = QtWidgets.QSizePolicy.Minimum
    QSP_Expanding          = QtWidgets.QSizePolicy.Expanding
    QMB_Ok                 = QtWidgets.QMessageBox.Ok
    QMB_Yes                = QtWidgets.QMessageBox.Yes
    QMB_No                 = QtWidgets.QMessageBox.No
    Qt_UserRole            = QtCore.Qt.UserRole
    QAV_SingleSelection    = QtWidgets.QAbstractItemView.SingleSelection
