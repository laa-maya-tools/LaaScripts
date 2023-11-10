from ConnectionManager.window.constraint.constraintMainWidget import ConstraintMainWidgetWin
from ConnectionManager.window.constraint.orientConstraintWidget import OrientConstraintWidgetWin
from ConnectionManager.window.constraint.parentConstraintWidget import ParentConstraintWidgetWin
from ConnectionManager.window.constraint.pointConstraintWidget import PointConstraintWidgetWin
from ConnectionManager.window.constraint.scaleConstraintWidget import ScaleConstraintWidgetWin
from ConnectionManager.window.constraint.aimConstraintWidget import AimConstraintWidgetWin

subWidgetsDict = {'pointConstraint':
                      {'widgetClass':PointConstraintWidgetWin,
                      },
                  'orientConstraint':
                      {'widgetClass':OrientConstraintWidgetWin,
                      },
                  'parentConstraint':
                      {'widgetClass':ParentConstraintWidgetWin,
                      },
                  'scaleConstraint':
                      {'widgetClass':ScaleConstraintWidgetWin,
                      },
                  'aimConstraint':
                      {'widgetClass':AimConstraintWidgetWin,
                      },
    }

mainWidgetsDict = {'constraint':
                        {'mayaNodeTypeFilter':'constraint',
                         'widgetClass':ConstraintMainWidgetWin,
                        },
                  }