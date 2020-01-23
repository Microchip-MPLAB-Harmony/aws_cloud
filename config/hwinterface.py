# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""


import os
from xml.sax.saxutils import quoteattr as xml_quoteattr
import xml.etree.ElementTree as ET

# Fetch Core Architecture and Family details
CONFIG_NAME="config_name"
CONFIG_TYPE="config_type"
CONFIG_LABEL="config_label"
CONFIG_VISIBLE="config_visible"
CONFIG_DESC="config_descr"
CONFIG_DEFAULT_VAL="config_default"

coreArch     = Database.getSymbolValue("core", "CoreArchitecture")
coreFamily   = ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "family" )
autoConnectTableDebug = [["sys_debug", "sys_debug_SYS_CONSOLE_dependency", "sys_console"]]
autoConnectTableCmd = [["sys_command", "sys_command_SYS_CONSOLE_dependency", "sys_console"]]

AMAZON_FREERTOS_PATH="../../../../../../../../../../"

CONFIG_FREERTOS="FreeRTOS"
CONFIG_MICRIUM="MicriumOSIII"


XML_ATTRIB_NAME = "name"
XML_ATTRIB_DIR  = "dir"
XML_ATTRIB_FILE  = "file"
XML_ATTRIB_TEMPLATE = "template"
XML_ATTRIB_COMPONENTS="components"
XML_ATTRIB_COMPONENT="component"
XML_ATTRIB_MENU="menu"
XML_ATTRIB_COMBO="combo"
XML_ATTRIB_STRING="string"
XML_ATTRIB_BOOL="bool"
XML_ATTRIB_INC="include-files"

CONFIG_DEMOS=0
CONFIG_DEVICE_TESTER=1

connected_dep=["demos","DT"]
connected_dep_index=CONFIG_DEMOS

###############################################################################
########################## FreeRTOS Configurations ############################
###############################################################################

def deactivateActiveRtos():
    activeComponents = Database.getActiveComponentIDs()

    for i in range(0, len(activeComponents)):
        if (activeComponents[i] == CONFIG_FREERTOS):
            res = Database.deactivateComponents([CONFIG_FREERTOS])
        if (activeComponents[i] == CONFIG_MICRIUM):
            res = Database.deactivateComponents([CONFIG_MICRIUM])
            
def freeRtosIntConfig():
    if (coreArch == "MIPS"):
        Timer1InterruptHandlerIndex     = Interrupt.getInterruptIndex("TIMER_1")

        Timer1InterruptEnable           = "EVIC_"+ str(Timer1InterruptHandlerIndex) +"_ENABLE"

        if (Database.getSymbolValue("core", Timer1InterruptEnable) == False):
            Database.clearSymbolValue("core", Timer1InterruptEnable)
            Database.setSymbolValue("core", Timer1InterruptEnable, True)

        #Enable TMR1 Peripheral Clock for FreeRTOS Tick Interrupt Generation
        if (Database.getSymbolValue("core", "TMR1_CLOCK_ENABLE") == False):
            Database.clearSymbolValue("core", "TMR1_CLOCK_ENABLE")
            Database.setSymbolValue("core", "TMR1_CLOCK_ENABLE", True)

    else:
        SysTickInterruptEnable      = "SysTick_INTERRUPT_ENABLE"
        SysTickInterruptHandler     = "SysTick_INTERRUPT_HANDLER"
        SysTickInterruptHandlerLock = "SysTick_INTERRUPT_HANDLER_LOCK"

        if (Database.getSymbolValue("core", SysTickInterruptEnable) == False):
            Database.clearSymbolValue("core", SysTickInterruptEnable)
            Database.setSymbolValue("core", SysTickInterruptEnable, True)

        if (Database.getSymbolValue("core", SysTickInterruptHandler) != "xPortSysTickHandler"):
            Database.clearSymbolValue("core", SysTickInterruptHandler)
            Database.setSymbolValue("core", SysTickInterruptHandler, "xPortSysTickHandler")

        if (Database.getSymbolValue("core", SysTickInterruptHandlerLock) == False):
            Database.clearSymbolValue("core", SysTickInterruptHandlerLock)
            Database.setSymbolValue("core", SysTickInterruptHandlerLock, True)

        PendSVInterruptEnable       = "PendSV_INTERRUPT_ENABLE"
        PendSVInterruptHandler      = "PendSV_INTERRUPT_HANDLER"
        PendSVInterruptHandlerLock  = "PendSV_INTERRUPT_HANDLER_LOCK"

        if (Database.getSymbolValue("core", PendSVInterruptEnable) == False):
            Database.clearSymbolValue("core", PendSVInterruptEnable)
            Database.setSymbolValue("core", PendSVInterruptEnable, True)

        if (Database.getSymbolValue("core", PendSVInterruptHandler) != "xPortPendSVHandler"):
            Database.clearSymbolValue("core", PendSVInterruptHandler)
            Database.setSymbolValue("core", PendSVInterruptHandler, "xPortPendSVHandler")

        if (Database.getSymbolValue("core", PendSVInterruptHandlerLock) == False):
            Database.clearSymbolValue("core", PendSVInterruptHandlerLock)
            Database.setSymbolValue("core", PendSVInterruptHandlerLock, True)

        SVCallInterruptEnable       = "SVCall_INTERRUPT_ENABLE"
        SVCallInterruptHandler      = "SVCall_INTERRUPT_HANDLER"
        SVCallInterruptHandlerLock  = "SVCall_INTERRUPT_HANDLER_LOCK"

        if (Database.getSymbolValue("core", SVCallInterruptEnable) == False):
            Database.clearSymbolValue("core", SVCallInterruptEnable)
            Database.setSymbolValue("core", SVCallInterruptEnable, True)

        if (Database.getSymbolValue("core", SVCallInterruptHandler) != "vPortSVCHandler"):
            Database.clearSymbolValue("core", SVCallInterruptHandler)
            Database.setSymbolValue("core", SVCallInterruptHandler, "vPortSVCHandler")

        if (Database.getSymbolValue("core", SVCallInterruptHandlerLock) == False):
            Database.clearSymbolValue("core", SVCallInterruptHandlerLock)
            Database.setSymbolValue("core", SVCallInterruptHandlerLock, True)


#Instatntiate FreeRTOS Component
def instantiateComponent(hw_interface):
    global connected_dep_index
    Log.writeInfoMessage("Running AmazonFreeRTOS interface")

    # Deactivate the active RTOS if any.
    deactivateActiveRtos()
    res = Database.activateComponents(["HarmonyCore"])
    
    if(Database.getComponentByID("sys_debug") == None):
        res = Database.activateComponents(["sys_debug"])
        res = Database.connectDependencies(autoConnectTableDebug)    
    if(Database.getComponentByID("sys_command") == None):
        res = Database.activateComponents(["sys_command"])
        res = Database.connectDependencies(autoConnectTableCmd)  

    if ((coreArch == "CORTEX-M4") or (coreArch == "CORTEX-M7")):
        if(Database.getComponentByID("trng") == None):
            res = Database.activateComponents(["trng"])

    if ((coreArch == "MIPS")):
        if(Database.getComponentByID("nvm") == None):
            res = Database.activateComponents(["nvm"])
        if(Database.getComponentByID("rng") == None):
            res = Database.activateComponents(["rng"])    

    #FreeRTOS Configuration Menu
    if(Database.getComponentByID("AmazonFreeRTOS") == None):
        connected_dep_index=CONFIG_DEVICE_TESTER

    freeRtosIntConfig()
    Database.setSymbolValue("HarmonyCore", "SELECT_RTOS","FreeRTOS")


############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")
    AddAWSFile(hw_interface,"../", "",Module.getPath()+"config/"+ connected_dep[connected_dep_index] + "/" + coreArch+"_MAC.xml")
    freeRtosIncWarn = hw_interface.createSettingSymbol("AFR_XC32_WARNING", None)
    freeRtosIncWarn.setCategory("C32")
    freeRtosIncWarn.setKey("make-warnings-into-errors")
    freeRtosIncWarn.setValue("false")
    AddAWSConfig(hw_interface,Module.getPath()+"config/UI/" + connected_dep[connected_dep_index] + "_"+ coreArch+"_MAC.xml")
 

def AddFileTemplate(component, strPath, strFileName, strDestPath,strProjectPath,strType="SOURCE",bMarkup=True):
    global connected_dep_index
    configName = Variables.get("__CONFIGURATION_NAME")
    Log.writeInfoMessage(strPath.upper())
    Log.writeInfoMessage(strFileName.upper())
    Log.writeInfoMessage(strDestPath.upper())
    Log.writeInfoMessage(strProjectPath.upper())
    freeRtosAddFile = component.createFileSymbol(strPath.upper(), None)
    freeRtosAddFile.setSourcePath("templates/" + connected_dep[connected_dep_index] +"/" + coreArch + "/" + strFileName)

    if(strFileName.endswith(".ftl")):
       strFileName= strFileName[:-4]
       Log.writeInfoMessage(strPath.upper())
       Log.writeInfoMessage(strFileName.upper())
       Log.writeInfoMessage(strDestPath.upper())
       Log.writeInfoMessage(strProjectPath.upper())
    freeRtosAddFile.setOutputName(strFileName)
    freeRtosAddFile.setDestPath(strDestPath)
    freeRtosAddFile.setProjectPath(strProjectPath)
    freeRtosAddFile.setType(strType)
    freeRtosAddFile.setMarkup(bMarkup)


def AddFile(component, strPath, strFileName, strDestPath,strProjectPath,strType="SOURCE",bMarkup=False):
    configName = Variables.get("__CONFIGURATION_NAME")
    Log.writeInfoMessage(strPath.upper())
    Log.writeInfoMessage(strFileName.upper())
    Log.writeInfoMessage(strDestPath.upper())
    Log.writeInfoMessage(strProjectPath.upper())
    freeRtosAddFile = component.createFileSymbol(strPath.upper(), None)
    freeRtosAddFile.setSourcePath(strPath)
    freeRtosAddFile.setOutputName(strFileName)
    freeRtosAddFile.setDestPath(strDestPath)
    freeRtosAddFile.setProjectPath(strProjectPath)
    freeRtosAddFile.setType(strType)
    freeRtosAddFile.setMarkup(bMarkup)


def AddDir(root,component,strPath, strRelativeFilePath,strProjectPath):
    for child in root:
        if child.tag == XML_ATTRIB_DIR:
            NewstrPath = strPath + "/" + str(child.attrib[XML_ATTRIB_NAME])
            NewstrRelativeFilePath = strRelativeFilePath +  "/" + str(child.attrib[XML_ATTRIB_NAME])
            NewstrProjectPath = strProjectPath +  "/" + str(child.attrib[XML_ATTRIB_NAME])
            AddDir(child,component,NewstrPath, NewstrRelativeFilePath ,NewstrProjectPath)
        if child.tag == XML_ATTRIB_FILE:
            NewstrPath = strPath + "/" + str(child.attrib[XML_ATTRIB_NAME])
            AddFile(component,NewstrPath, str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath ,strProjectPath)

        elif child.tag == XML_ATTRIB_TEMPLATE:
            NewstrPath = strPath + "/" + str(child.attrib[XML_ATTRIB_NAME])
            AddFileTemplate(component,NewstrPath, str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath ,strProjectPath)



def AddAWSFile(component,strPath, strRelativeFilePath, strXmlFile):
    tree = ET.parse(strXmlFile)
    root = tree.getroot()
    for child in root:
        if child.tag == XML_ATTRIB_DIR:
            AddDir(child,component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), AMAZON_FREERTOS_PATH + strRelativeFilePath +  "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath +  "/" + str(child.attrib[XML_ATTRIB_NAME]))
        if child.tag == XML_ATTRIB_FILE:
            AddFile(component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath+ "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath + "/" + str(child.attrib[XML_ATTRIB_NAME]))
        if child.tag == XML_ATTRIB_TEMPLATE:
            AddFileTemplate(component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath+ "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath + "/" + str(child.attrib[XML_ATTRIB_NAME]))
        

def AddAWSConfig(aws_cloud,strXmlFile):
    tree = ET.parse(strXmlFile)
    root = tree.getroot()
    for child in root:
        if child.tag == XML_ATTRIB_COMPONENTS:
            temp_elem = AddAWSConfiguration(aws_cloud,None,child.attrib[CONFIG_NAME],child.attrib[CONFIG_TYPE],child.attrib[CONFIG_LABEL], child.attrib[CONFIG_DESC], child.attrib[CONFIG_DEFAULT_VAL], child.attrib[CONFIG_VISIBLE])
            AddAWSComponent(aws_cloud,child,temp_elem,child.attrib[CONFIG_NAME],child.attrib[CONFIG_TYPE],child.attrib[CONFIG_LABEL], child.attrib[CONFIG_DESC], child.attrib[CONFIG_DEFAULT_VAL], child.attrib[CONFIG_VISIBLE])
        if child.tag == XML_ATTRIB_COMPONENT:
            AddAWSConfiguration(aws_cloud,None,child.attrib[CONFIG_NAME],child.attrib[CONFIG_TYPE],child.attrib[CONFIG_LABEL], child.attrib[CONFIG_DESC], child.attrib[CONFIG_DEFAULT_VAL], child.attrib[CONFIG_VISIBLE])


def AddAWSComponent(aws_cloud,root,parent_config,config_name,config_type,strLabel,strDesc,strDefaultValue,bVisible):
    for child in root:
        if child.tag == XML_ATTRIB_COMPONENTS:
            AddAWSComponent(aws_cloud,parent_config,child.attrib[CONFIG_NAME],child.attrib[CONFIG_TYPE],child.attrib[CONFIG_LABEL], child.attrib[CONFIG_DESC], child.attrib[CONFIG_DEFAULT_VAL], child.attrib[CONFIG_VISIBLE])
        if child.tag == XML_ATTRIB_COMPONENT:
            AddAWSConfiguration(aws_cloud,parent_config,child.attrib[CONFIG_NAME],child.attrib[CONFIG_TYPE],child.attrib[CONFIG_LABEL], child.attrib[CONFIG_DESC], child.attrib[CONFIG_DEFAULT_VAL], child.attrib[CONFIG_VISIBLE])

def AddAWSConfiguration(aws_cloud,parent_config,config_name,config_type,strLabel,strDesc,strDefaultValue,bVisible):
    if str(config_type).lower() == XML_ATTRIB_MENU:
        freeRtosSymMenu = aws_cloud.createMenuSymbol(config_name, parent_config)
    elif str(config_type).lower() == XML_ATTRIB_STRING:
        freeRtosSymMenu = aws_cloud.createStringSymbol(config_name, parent_config)
        freeRtosSymMenu.setDefaultValue(str(strDefaultValue))
    elif str(config_type).lower() == XML_ATTRIB_BOOL:
        freeRtosSymMenu = aws_cloud.createBooleanSymbol(config_name, parent_config)
        freeRtosSymMenu.setDefaultValue(bool(strDefaultValue))
    elif str(config_type).lower() == XML_ATTRIB_COMBO:
        strValues = strDefaultValue.split(' ')
        freeRtosSymMenu = aws_cloud.createComboSymbol(config_name, parent_config,strValues)
        freeRtosSymMenu.setDefaultValue(strValues[0])
    else: #if type.lower() == "integer": considered integer.
        freeRtosSymMenu = aws_cloud.createIntegerSymbol(config_name, parent_config)
        freeRtosSymMenu.setDefaultValue(int(strDefaultValue))
        freeRtosSymMenu.setMin(0)
        freeRtosSymMenu.setMax(999999999)
	
    freeRtosSymMenu.setLabel(strLabel)
    freeRtosSymMenu.setDescription(strDesc)
    freeRtosSymMenu.setVisible(False)
	
    #How to set generic Default Value.
    if(str(bVisible).lower()=="true"):
        freeRtosSymMenu.setVisible(True)
    return freeRtosSymMenu






