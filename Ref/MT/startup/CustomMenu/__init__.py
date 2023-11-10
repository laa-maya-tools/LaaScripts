import maya.cmds as cmds

import ProjectPath

import json, os, functools, logging

menus = [r"CommonMenu", r"Modelling", r"RiggingMenu", r"AnimationMenu"]

currentMenu = None
currentFilePath = None

def init():
    menuRoot = os.path.join(ProjectPath.getStartupFolder(), r"CustomMenu\Menus")
    for menu in menus:
        createMenuFromFile(os.path.join(menuRoot, "{}.json".format(menu)))
        
def createGenericMenuFromFile(filePath, menuCommand, useLabel=False, **commandArgs):
    file = open(filePath)
    try:
        jsonFile = json.load(file)
        
        menu = jsonFile["menuName"]
        if menuCommand(menu, q=True, ex=True):
            menuCommand(menu, e=True, deleteAllItems=True)
        else:
            if useLabel:
                commandArgs["label"] = menu
            menu = menuCommand(menu, postMenuCommand=functools.partial(updateMenuFromJsonFile, menu, filePath), **commandArgs)
        
        global currentMenu, currentFilePath
        currentMenu = menu
        currentFilePath = filePath
        
        configureMenuFromJson(menu, jsonFile)
        
        currentMenu = None
        currentFilePath = None

        return menu

    finally:
        file.close()

def createMenuFromFile(filePath, parent="MayaWindow", tearOff=True):
    return createGenericMenuFromFile(filePath, cmds.menu, useLabel=True, parent=parent, tearOff=tearOff)

def createPopUpMenuFromFile(filePath, parent="MayaWindow", button=1):
    return createGenericMenuFromFile(filePath, cmds.popupMenu, parent=parent, button=button)

def configureMenuFromJson(menu, jsonFile):
    for menuItem in jsonFile["menuItems"]:
        try:
            if menuItem["type"] == "subMenu":
                createSubMenuFromJson(menuItem, menu)
            elif menuItem["type"] == "action":
                createActionFromJson(menuItem, menu)
            elif menuItem["type"] == "toggle":
                createToggleFromJson(menuItem, menu)
            elif menuItem["type"] == "separator":
                createSeparator(menuItem, menu)
        except:
            logging.exception("Error while creating MenuItem!")

def createSubMenuFromJson(jsonFile, menu):
    floatable = jsonFile["floatable"] if "floatable" in jsonFile else False
    tooltip = jsonFile["tooltip"] if "tooltip" in jsonFile else ""
    icon = jsonFile["icon"] if "icon" in jsonFile else ""
    
    menuItem = cmds.menuItem(jsonFile["menuName"], label=jsonFile["menuName"], ann=tooltip, subMenu=True, tearOff=floatable, image=icon, parent=menu)
    
    configureMenuFromJson(menuItem, jsonFile)
    
    return menuItem

def createActionFromJson(jsonFile, menu):
    module = jsonFile["module"] if "module" in jsonFile else None
    if module != None:
        exec("import {}".format(module))
        moduleCommand = "{}.".format(module)
    else:
        moduleCommand = ""
    
    enabled = eval("{module}{enabledFn}".format(module=moduleCommand, enabledFn=jsonFile["enabled"])) if "enabled" in jsonFile else True
    tooltip = jsonFile["tooltip"] if "tooltip" in jsonFile else ""
    icon = jsonFile["icon"] if "icon" in jsonFile else ""
    
    executeModuleCommand = "" if module == None else "import {0}; {0}.".format(module)
    actionCommand = jsonFile["action"]
    paramsCommand = ",".join(jsonFile["params"]) if "params" in jsonFile else ""
    command = "{module}{action}({params})".format(module=executeModuleCommand, action=actionCommand, params=paramsCommand)
    
    menuItem = cmds.menuItem(jsonFile["label"], label=jsonFile["label"], ann=tooltip, image=icon, enable=enabled, command=command, parent=menu)

    if "optionBox" in jsonFile:
        createOptionBox(jsonFile["optionBox"], menu)

    return menuItem

def createToggleFromJson(jsonFile, menu):
    module = jsonFile["module"] if "module" in jsonFile else None
    if module != None:
        exec("import {}".format(module))
        moduleCommand = "{}.".format(module)
    else:
        moduleCommand = ""
        
    icon = jsonFile["icon"] if "icon" in jsonFile else ""
    tooltip = jsonFile["tooltip"] if "tooltip" in jsonFile else ""
    enabled = eval("{module}{enabledFn}".format(module=moduleCommand, enabledFn=jsonFile["enabled"])) if "enabled" in jsonFile else True
    
    updateMenus = jsonFile["updateMenus"] if "updateMenus" in jsonFile else False
    toggleCommand = eval("{module}{action}".format(module=moduleCommand, action=jsonFile["toggleFn"]))
    state = eval("{module}{stateFn}".format(module=moduleCommand, stateFn=jsonFile["state"]))
    
    if updateMenus:
        global currentMenu, currentFilePath
        toggleCommand = functools.partial(toggleCommandAndUpdate, currentMenu, currentFilePath, toggleCommand)
    
    return cmds.menuItem(jsonFile["label"], label=jsonFile["label"], ann=tooltip, image=icon, enable=enabled, command=toggleCommand, checkBox=state, parent=menu)

def createSeparator(jsonFile, menu):
    if "label" in jsonFile:
        divider = cmds.menuItem(divider=True, dividerLabel=jsonFile["label"], parent=menu)
    else:
        divider = cmds.menuItem(divider=True, parent=menu)
    return divider

def createOptionBox(jsonFile, menu):
    module = jsonFile["module"] if "module" in jsonFile else None
    if module != None:
        exec("import {}".format(module))
    
    executeModuleCommand = "" if module == None else "import {0}; {0}.".format(module)
    actionCommand = jsonFile["action"]
    paramsCommand = ",".join(jsonFile["params"]) if "params" in jsonFile else ""
    command = "{module}{action}({params})".format(module=executeModuleCommand, action=actionCommand, params=paramsCommand)
    
    return cmds.menuItem(optionBox=True, command=command, parent=menu)

def toggleCommandAndUpdate(menu, filePath, command, state):
    command(state)
    updateMenuFromJsonFile(menu, filePath)

def updateMenuFromJsonFile(menu, filePath, *args):
    file = open(filePath)
    try:
        jsonFile = json.load(file)
        updateMenuFromJson(menu, jsonFile)
        
    finally:
        file.close()

def updateMenuFromJson(menu, jsonFile):
    menuItems = jsonFile["menuItems"]
    children = cmds.menu(menu, q=True, ia=True)
    
    childIndex = 0
    for i in range(len(menuItems)):
        menuItem = menuItems[i]
        if menuItem["type"] == "subMenu":
            updateMenuFromJson(children[childIndex], menuItem)
        elif menuItem["type"] == "action":
            updateActionFromJson(children[childIndex], menuItem)
        elif menuItem["type"] == "toggle":
            updateToggleFromJson(children[childIndex], menuItem)
            
        childIndex += 1
        if "optionBox" in menuItem:
            childIndex += 1 # Option Boxes appear as children of the menus, but are not an item on the Json
            
def updateActionFromJson(item, jsonFile, *args):
    module = jsonFile["module"] if "module" in jsonFile else None
    if module != None:
        exec("import {}".format(module))
        moduleCommand = "{}.".format(module)
    else:
        moduleCommand = ""
        
    enabled = eval("{module}{enabledFn}".format(module=moduleCommand, enabledFn=jsonFile["enabled"])) if "enabled" in jsonFile else True
    
    cmds.menuItem(item, e=True, enable=enabled)

def updateToggleFromJson(item, jsonFile, *args):
    module = jsonFile["module"] if "module" in jsonFile else None
    if module != None:
        exec("import {}".format(module))
        moduleCommand = "{}.".format(module)
    else:
        moduleCommand = ""
        
    enabled = eval("{module}{enabledFn}".format(module=moduleCommand, enabledFn=jsonFile["enabled"])) if "enabled" in jsonFile else True
    state = eval("{module}{stateFn}".format(module=moduleCommand, stateFn=jsonFile["state"]))
    
    cmds.menuItem(item, e=True, enable=enabled, checkBox=state)
