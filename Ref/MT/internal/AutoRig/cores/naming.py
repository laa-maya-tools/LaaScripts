import maya.cmds as cmds
import sys

_naming_ = "{system}_{num}_{nodeType}"

# alphabetical order
_ndTyp_dict_ = {"addDoubleLinear":"addbl",
                "aimConstraint":"aimc",
                "animCurveUA":"dkUA",
                "auxiliar":"aux",
                "blendColors":"blcl",
                "choice":"chc",
                "clamp":"clp",
                "constraintAux":"mstc",
                "control":"ctr",
                "controller":"tag",
                "curve":"crv",
                "curveInfo":"cvinf",
                "distanceBetween":"dist",
                "doublePointConstraint":"pnc",
                "footRoll":"footroll",
                "floatMath":"fm",
                "group":"grp",
                "hierarchize":"hrch",
                "ikHandle":"ikh",
                "ikRPsolver":"ikrp",
                "ikSCsolver":"iksc",
                "ikSpline":"iksp",
                "ikrotate":"ikrp",
                "joint":"jnt",
                "linker":"link",
                "locator":"loc",
                "matrixMirror":"mtxMrr",
                "motionPath":"mp",
                "multDoubleLinear":"mdbl",
                "multiplyDivide":"mdv",
                "nurbsCurve":"crv",
                "offset":"off",
                "orientConstraint":"orc",
                "parentConstraint":"prc",
                "pointConstraint":"pnc",
                "pointOnCurveInfo":"poci",
                "poleVectorConstraint":"pvc",
                "plusMinusAverage":"pma",
                "reverse":"rev",
                "remapValue":"rmv",
                "root":"root",
                "scaleConstraint":"scc",
                "snapper":"snapper",
                "space":"spc",
                "template":"tpl",
                "transform":"tr",
                "unitConversion":"ucnv",
                }

def __split__(strInput):
    resultLs = []
    for token in strInput.split("_"):
        for each in token.split("}{"):
            if each.startswith("{"):
                each = each[1:]
            if each.endswith("}"):
                each = each[:-1]
            resultLs.append(each)
    return resultLs

def setName(system, nodeType, num=None):
    '''Creates not existing name'''
    namingDict = {'system':system,
                  'num':num,
                  'nodeType':_ndTyp_dict_[nodeType]}
    if not num:
        namingDict['num'] = '00'
    if type(namingDict['num']) != str:
        namingDict['num'] = str(num).zfill(2)
    result = _naming_.format(**namingDict)
    while cmds.objExists("{}:{}".format(cmds.namespaceInfo(currentNamespace=True), result)):
        namingDict['num'] = int(namingDict['num'])
        namingDict['num'] = str(namingDict['num'] + 1).zfill(2)
        result = _naming_.format(**namingDict)
    return result

def getName(node):
    '''Given a name, returns dictionary of naming convention tokens and its value. Based on ":" in name'''
    result = {}
    # do ---------------------------------------------
    for key, val in zip(__split__(_naming_), __split__(node.split(":")[-1])):
        if key == "num":
            val = val
        result[key] = val
    if 'nodeType' not in result.keys():
        return result
    for key, val in _ndTyp_dict_.items():
        if val == result['nodeType']:
            result['nodeType'] = key
            break
    return result