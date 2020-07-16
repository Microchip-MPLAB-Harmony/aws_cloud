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
import time
from xml.sax.saxutils import quoteattr as xml_quoteattr
import xml.etree.ElementTree as ET

CONFIG_NAME="config_name"
CONFIG_TYPE="config_type"
CONFIG_LABEL="config_label"
CONFIG_VISIBLE="config_visible"
CONFIG_DESC="config_descr"
CONFIG_DEFAULT_VAL="config_default"

AMAZON_FREERTOS_PATH_DEFAULT="../../../../../../../../../../"
AMAZON_FREERTOS_PATH_H3=""
AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_DEFAULT
AMAZON_FREERTOS_INC_PATH_DEFAULT="../../../../../../../"
AMAZON_FREERTOS_INC_H3="../"
CONFIG_FREERTOS="FreeRTOS"
CONFIG_MICRIUM="MicriumOSIII"
CONFIG_FREERTOS="AmazonFreeRTOS"
CONFIG_COMMON_AFR="config/DT/common_afr.xml"
CONFIG_UI_COMMON_AFR="config/UI/aws_config_only.xml"

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
XML_ATTRIB_OVER_WRITE="overwrite"


#setH3DirectoryEnable
def setH3DirectoryEnable(symbol, event):
    global AMAZON_FREERTOS_PATH,AMAZON_FREERTOS_PATH_H3,AMAZON_FREERTOS_PATH_DEFAULT,AMAZON_FREERTOS_INC_PATH
    global AMAZON_FREERTOS_INC_PATH_DEFAULT,AMAZON_FREERTOS_INC_H3,coreFamily,coreArch
    global freeRtosdefSym1,freeRtosIncDirForAsm, freeRtosdefSym2,freeRtosdefSym3
    Log.writeInfoMessage("Running AWS Changes +*" + str(symbol.getValue()))
    configName = Variables.get("__CONFIGURATION_NAME")
    if(event['symbol'].getValue()):
        AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_DEFAULT
        AMAZON_FREERTOS_INC_PATH=AMAZON_FREERTOS_INC_PATH_DEFAULT
    else:
        AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_H3
        AMAZON_FREERTOS_INC_PATH="../src/config/"+configName+"/amazon-freertos/"
    AddAWSFile(symbol.getComponent(),"../",  "",Module.getPath()+CONFIG_COMMON_AFR , True )

# Deactivate Other RTOS
def deactivateActiveRtos():
    activeComponents = Database.getActiveComponentIDs()

    for i in range(0, len(activeComponents)):
        if (activeComponents[i] == CONFIG_FREERTOS):
            res = Database.deactivateComponents([CONFIG_FREERTOS])
        if (activeComponents[i] == CONFIG_MICRIUM):
            res = Database.deactivateComponents([CONFIG_MICRIUM])
        if (activeComponents[i] == CONFIG_FREERTOS):
            res = Database.deactivateComponents([CONFIG_FREERTOS])


#Instatntiate FreeRTOS Component
def instantiateComponent(aws_cloud):
    global AMAZON_FREERTOS_PATH, AMAZON_FREERTOS_INC_PATH,AMAZON_FREERTOS_PATH_DEFAULT,AMAZON_FREERTOS_PATH_H3,coreArch,coreFamily
    Log.writeInfoMessage("Running AmazonFreeRTOS")

    coreArch     = Database.getSymbolValue("core", "CoreArchitecture")
    coreFamily   = ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "family" )


    # Deactivate the active RTOS if any.
    deactivateActiveRtos()
    autoComponentIDTable = ["stdio"]
    res = Database.activateComponents(autoComponentIDTable)
    #AmazonFreeRTOS Configuration Menu

    AddAWSConfig(aws_cloud,Module.getPath()+ CONFIG_UI_COMMON_AFR)
############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")
    freeRtosIncWarn = aws_cloud.createSettingSymbol("AFR_XC32_WARNING", None)
    freeRtosIncWarn.setCategory("C32")
    freeRtosIncWarn.setKey("make-warnings-into-errors")
    freeRtosIncWarn.setValue("false")

    freeRtosH3Dir = aws_cloud.createBooleanSymbol("AWS_CLOUD_H3", None)
    freeRtosH3Dir.setLabel("Use Amazon FreeRTOS Directory Structure")
    freeRtosH3Dir.setDescription("Use Amazon FreeRTOS Directory Structure")
    freeRtosH3Dir.setVisible(True)
    freeRtosH3Dir.setDependencies(setH3DirectoryEnable,["AmazonDeviceTester.AWS_CLOUD_H3"])

    if(freeRtosH3Dir.getValue() == 'True'):
        Log.writeInfoMessage("Amazon module")
        AMAZON_FREERTOS_INC_PATH=AMAZON_FREERTOS_INC_PATH_DEFAULT
        AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_DEFAULT
    else:
        Log.writeInfoMessage("Amazon module")
        AMAZON_FREERTOS_INC_PATH="../src/config/"+configName+"/amazon-freertos/"
        AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_H3
    AddAWSFile(aws_cloud,"../",  "",Module.getPath()+CONFIG_COMMON_AFR , False )

#############################################################
### ADD DIR, ADD FILE, ADD Template methods
#############################################################

# Add File Template
def AddFileTemplate(boolFileEnable, boolDisableGen, component, strPath, strFileName, strDestPath,strProjectPath,strType="SOURCE",bMarkup=True):
    if boolDisableGen:
        component.getSymbolByID(strPath.upper()).setEnabled(boolFileEnable)
        component.getSymbolByID(strPath.upper()).setDestPath(strDestPath)
    else:
        global connected_dep,connected_dep_index
        configName = Variables.get("__CONFIGURATION_NAME")
        Log.writeInfoMessage(strPath.upper())
        Log.writeInfoMessage(strFileName.upper())
        Log.writeInfoMessage(strDestPath.upper())
        Log.writeInfoMessage(strProjectPath.upper())
        freeRtosAddFile = component.createFileSymbol(strPath.upper(), None)
        freeRtosAddFile.setSourcePath("templates/" + strFileName)

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
        freeRtosAddFile.setEnabled(boolFileEnable)


# Add File
def AddFile(boolFileEnable, boolDisableGen, component, strPath, strFileName, strDestPath,strProjectPath,bOverWrite=True,strType="SOURCE",bMarkup=False):
    if boolDisableGen:
        component.getSymbolByID(strPath.upper()).setEnabled(boolFileEnable)
        component.getSymbolByID(strPath.upper()).setDestPath(strDestPath)
        
    else:
        configName = Variables.get("__CONFIGURATION_NAME")
        Log.writeInfoMessage(strPath.upper())
        Log.writeInfoMessage(strFileName.upper())
        Log.writeInfoMessage(strDestPath.upper())
        Log.writeInfoMessage(strProjectPath.upper())
        freeRtosAddFile = component.createFileSymbol(strPath.upper(), None)
        freeRtosAddFile.setSourcePath(strPath)
        freeRtosAddFile.setOverwrite(bOverWrite)
        freeRtosAddFile.setOutputName(strFileName)
        freeRtosAddFile.setDestPath(strDestPath)
        freeRtosAddFile.setProjectPath(strProjectPath)
        freeRtosAddFile.setType(strType)
        freeRtosAddFile.setMarkup(bMarkup)

def AddDir(boolDirEnable,root,component,strPath, strRelativeFilePath,strProjectPath, boolDisableGen):
    for child in root:
        if child.tag == XML_ATTRIB_DIR:
            NewstrPath = strPath + "/" + str(child.attrib[XML_ATTRIB_NAME])
            NewstrRelativeFilePath = strRelativeFilePath +  "/" + str(child.attrib[XML_ATTRIB_NAME])
            NewstrProjectPath = strProjectPath +  "/" + str(child.attrib[XML_ATTRIB_NAME])
            AddDir(CheckAttrib(child,boolDirEnable),child,component,NewstrPath, NewstrRelativeFilePath ,NewstrProjectPath, boolDisableGen)
        if child.tag == XML_ATTRIB_FILE:
            NewstrPath = strPath + "/" + str(child.attrib[XML_ATTRIB_NAME])
            if( (XML_ATTRIB_OVER_WRITE in child.attrib) and child.attrib[XML_ATTRIB_OVER_WRITE] == "false"):
                AddFile(CheckAttrib(child,boolDirEnable),boolDisableGen, component,NewstrPath, str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath ,strProjectPath,False)
            else:
                AddFile(CheckAttrib(child,boolDirEnable),boolDisableGen, component,NewstrPath, str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath ,strProjectPath)
        elif child.tag == XML_ATTRIB_TEMPLATE:
            NewstrPath = strPath + "/" + str(child.attrib[XML_ATTRIB_NAME])
            AddFileTemplate(CheckAttrib(child,boolDirEnable), boolDisableGen, component,NewstrPath, str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath ,strProjectPath)



# CheckAttrib not applicable for Amazon FreeRTOS Component, all files to be added.
def CheckAttrib(child,boolDirEnable):
    return boolDirEnable
    

def AddAWSFile(component,strPath, strRelativeFilePath, strXmlFile, boolDisableGen,boolDirEnable=True):
    global AMAZON_FREERTOS_PATH
    tree = ET.parse(strXmlFile)
    root = tree.getroot()
    for child in root:
        if child.tag == XML_ATTRIB_DIR:
            AddDir(CheckAttrib(child,boolDirEnable),child,component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), AMAZON_FREERTOS_PATH + strRelativeFilePath +  "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath +  "/" + str(child.attrib[XML_ATTRIB_NAME]), boolDisableGen)
        if child.tag == XML_ATTRIB_FILE:
            if( (XML_ATTRIB_OVER_WRITE in child.attrib)):
                AddFile(CheckAttrib(child,boolDirEnable),boolDisableGen, component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath+ "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath + "/" + str(child.attrib[XML_ATTRIB_NAME]),False)
            else:
                AddFile(CheckAttrib(child,boolDirEnable),boolDisableGen,component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath+ "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath + "/" + str(child.attrib[XML_ATTRIB_NAME]))
        if child.tag == XML_ATTRIB_TEMPLATE:
            AddFileTemplate(CheckAttrib(child,boolDirEnable),boolDisableGen, component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath+ "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath + "/" + str(child.attrib[XML_ATTRIB_NAME]))


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
