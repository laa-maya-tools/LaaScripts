import maya.cmds as cmds

from Utils.Maya.UndoContext import UndoContext

dataTypeAttributes = [
    "string",
    "stringArray",
    "matrix",
    "reflectanceRGB",
    "spectrumRGB",
    "doubleArray",
    "floatArray",
    "Int32Array",
    "vectorArray",
    "nurbsCurve",
    "nurbsSurface",
    "mesh",
    "lattice",
    "pointArray",
]    

def copyNodeAttribute(sourceNode, targetNode, attribute):
    with UndoContext("Copy Node Attribute"):
        attrString = "{}.{}".format(sourceNode, attribute)
        
        extraParams = ""
        
        attributeType = cmds.ls(attrString, showType=True)[1]
        attributeIsMulti = cmds.attributeQuery(attribute, n=sourceNode, multi=True)
        attributeIsKeyable = cmds.attributeQuery(attribute, n=sourceNode, keyable=True)
        
        if cmds.attributeQuery(attribute, n=sourceNode, rangeExists=True):
            attributeRange = cmds.attributeQuery(attribute, n=sourceNode, range=True)
            extraParams += ", min={}, max={}".format(attributeRange[0], attributeRange[1])
            
        attributeListParent = (cmds.attributeQuery(attribute, n=sourceNode, listParent=True) or [None])[0]
        if attributeListParent:
            extraParams += ", p=\"{}\"".format(attributeListParent)
            
        attributeDefault = (cmds.attributeQuery(attribute, n=sourceNode, listDefault=True) or [None])[0]
        if attributeDefault != None:
            extraParams += ", dv={}".format(attributeDefault)
        
        if attributeIsMulti:
            indexMatters = cmds.addAttr(attrString, q=True, indexMatters=True)
            if indexMatters != None:
                extraParams += ", im={}".format(indexMatters)
        
        if attributeType == "enum":
            enumName = cmds.addAttr(attrString, q=True, enumName=True)
            if enumName:
                extraParams += ", en=\"{}\"".format(enumName)
        
        shortName = cmds.addAttr(attrString, q=True, shortName=True)
        if shortName:
            extraParams += ", sn=\"{}\"".format(shortName)
        
        niceName = cmds.addAttr(attrString, q=True, niceName=True)
        if niceName:
            extraParams += ", nn=\"{}\"".format(niceName)
        
        category = cmds.addAttr(attrString, q=True, category=True)
        if category:
            extraParams += ", ct=\"{}\"".format(category)
        
        disconnectBehaviour = cmds.addAttr(attrString, q=True, disconnectBehaviour=True)
        if disconnectBehaviour != None:
            extraParams += ", dcb={}".format(disconnectBehaviour)
        
        hidden = cmds.addAttr(attrString, q=True, hidden=True)
        if hidden != None:
            extraParams += ", h={}".format(hidden)
        
        readable = cmds.addAttr(attrString, q=True, readable=True)
        if readable != None:
            extraParams += ", r={}".format(readable)
        
        writable = cmds.addAttr(attrString, q=True, writable=True)
        if writable != None:
            extraParams += ", w={}".format(writable)
        
        storable = cmds.addAttr(attrString, q=True, storable=True)
        if storable != None:
            extraParams += ", s={}".format(storable)
        
        usedAsColor = cmds.addAttr(attrString, q=True, usedAsColor=True)
        if usedAsColor != None:
            extraParams += ", uac={}".format(usedAsColor)
        
        usedAsFilename = cmds.addAttr(attrString, q=True, usedAsFilename=True)
        if usedAsFilename != None:
            extraParams += ", uaf={}".format(usedAsFilename)
        
        usedAsProxy = cmds.addAttr(attrString, q=True, usedAsProxy=True)
        if usedAsProxy != None:
            extraParams += ", uap={}".format(usedAsProxy)
        
        proxy = cmds.addAttr(attrString, q=True, proxy=True)
        if proxy and proxy != attribute:
            extraParams += ", pxy=\"{}\"".format(proxy)
        
        if attributeType in dataTypeAttributes:
            attributeTypeParam = "dt=\"{}\"".format(attributeType)
        else:
            attributeTypeParam = "at=\"{}\"".format(attributeType)
            
        cmds.select(targetNode)
        command = "cmds.addAttr(ln=\"{attribute}\", {attributeParam}, m={multi}, k={keyable}{extraParams})"
        eval(command.format(attribute=attribute, attributeParam=attributeTypeParam, attributeType=attributeType, multi=attributeIsMulti, keyable=attributeIsKeyable, extraParams=extraParams))
