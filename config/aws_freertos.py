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
CONFIG_DEVTEST="AmazonDeviceTester"
CONFIG_COMMON_AFR="config/demos/common_afr.xml"
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
global SAME54_PORT_DIR,SAME70_PORT_DIR,PIC32MZ_PORT_DIR,SAME54_INC_DIR,SAME70_INC_DIR,PIC32_INC_DIR

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

    formatIncFiles()
    AddAWSFile(symbol.getComponent(),"../",  "",Module.getPath()+CONFIG_COMMON_AFR , True )
    
    coreArch     = Database.getSymbolValue("core", "CoreArchitecture")

    if (coreArch == "MIPS"):
        freeRtosdefSym1.setValue(PIC32_INC_DIR)
        freeRtosIncDirForAsm.setValue(PIC32_INC_DIR)
    elif (coreArch == "CORTEX-M4"):
        freeRtosdefSym2.setValue(SAME54_INC_DIR)
    elif (coreArch == "CORTEX-M7"):
        freeRtosdefSym3.setValue(SAME70_INC_DIR)

def formatIncFiles():
    global SAME54_PORT_DIR,SAME70_PORT_DIR,PIC32MZ_PORT_DIR,AMAZON_FREERTOS_INC_PATH,SAME54_INC_DIR,SAME70_INC_DIR,PIC32_INC_DIR
    SAME54_PORT_DIR = (AMAZON_FREERTOS_INC_PATH +"vendors/microchip/boards/same54_xpro/ports/pkcs11;" +
                       AMAZON_FREERTOS_INC_PATH +"vendors/microchip/harmony3/afr;" +
                       AMAZON_FREERTOS_INC_PATH +"vendors/microchip/boards/same54_xpro/aws_demos/config_files;" +
                       AMAZON_FREERTOS_INC_PATH +"freertos_kernel/portable/GCC/ARM_CM4F;" +
                       AMAZON_FREERTOS_INC_PATH +"vendors/microchip/harmony3/afr/tcpip/src/common;" +
                       AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/NetworkInterface/same54;")


    SAME70_PORT_DIR = (AMAZON_FREERTOS_INC_PATH +"vendors/microchip/boards/same70_xult/ports/pkcs11;" +
                       AMAZON_FREERTOS_INC_PATH +"vendors/microchip/harmony3/afr;" +
                       AMAZON_FREERTOS_INC_PATH +"vendors/microchip/boards/same70_xult/aws_demos/config_files;" +
                       AMAZON_FREERTOS_INC_PATH +"freertos_kernel/portable/GCC/ARM_CM7/r0p1;" +
                       AMAZON_FREERTOS_INC_PATH +"vendors/microchip/harmony3/afr/tcpip/src/common;" +
                       AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/NetworkInterface/same70;")


    PIC32MZ_PORT_DIR = (AMAZON_FREERTOS_INC_PATH +"vendors/microchip/boards/curiosity2_pic32mzef/ports/pkcs11;" +
                        AMAZON_FREERTOS_INC_PATH +"vendors/microchip/harmony3/afr;" +
                        AMAZON_FREERTOS_INC_PATH +"vendors/microchip/boards/curiosity2_pic32mzef/aws_demos/config_files;" +
                        AMAZON_FREERTOS_INC_PATH +"freertos_kernel/portable/MPLAB/PIC32MZ;"  +
                        AMAZON_FREERTOS_INC_PATH +"vendors/microchip/harmony3/afr/tcpip/src/common;" +
                        AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/NetworkInterface/pic32mzef_h3;")


    AFR_COMMON_INC_DIR = (AMAZON_FREERTOS_INC_PATH +"demos/include;" +
                          AMAZON_FREERTOS_INC_PATH +"freertos_kernel/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/abstractions/platform/freertos/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/abstractions/secure_sockets/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/abstractions/pkcs11/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/c_sdk/aws/defender/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/c_sdk/aws/shadow/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/c_sdk/standard/common/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/c_sdk/standard/https/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/c_sdk/standard/mqtt/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/c_sdk/standard/serializer/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/aws/greengrass/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/aws/ota/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/standard/crypto/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/standard/utils/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/standard/tls/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/standard/pkcs11/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/standard/freertos_plus_tcp/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/abstractions/platform/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/c_sdk/standard/common/include/private;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/c_sdk/standard/common/include/types;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/Compiler/GCC;" +
                          AMAZON_FREERTOS_INC_PATH +"demos/network_manager;" +
                          AMAZON_FREERTOS_INC_PATH +"demos/https;" +
                          AMAZON_FREERTOS_INC_PATH +"demos/tcp;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/3rdparty/jsmn;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/3rdparty/mbedtls/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/3rdparty/tinycbor;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/3rdparty/pkcs11;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/3rdparty/tinycrypt/asn1;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/3rdparty/tinycrypt/lib/include;" +
                          AMAZON_FREERTOS_INC_PATH +"demos/dev_mode_key_provisioning/include;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/abstractions/pkcs11/mbedtls;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/3rdparty/http-parser;" +
                          AMAZON_FREERTOS_INC_PATH +"libraries/freertos_plus/aws/ota/src;")



    SAME54_INC_DIR = AFR_COMMON_INC_DIR + SAME54_PORT_DIR
    SAME70_INC_DIR = AFR_COMMON_INC_DIR + SAME70_PORT_DIR
    PIC32_INC_DIR = AFR_COMMON_INC_DIR + PIC32MZ_PORT_DIR


# Fetch Core Architecture and Family details
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
        if (activeComponents[i] == CONFIG_DEVTEST):
            res = Database.deactivateComponents([CONFIG_DEVTEST])


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



    awsSystemDefFile = aws_cloud.createFileSymbol("AWS_SYS_DEF_HEADER", None)
    awsSystemDefFile.setType("STRING")
    awsSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    awsSystemDefFile.setSourcePath("templates/definitions.h.ftl")
    awsSystemDefFile.setMarkup(True)



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
    freeRtosH3Dir.setDependencies(setH3DirectoryEnable,["AmazonFreeRTOS.AWS_CLOUD_H3"])

    if(freeRtosH3Dir.getValue() == 'True'):
        Log.writeInfoMessage("Amazon module")
        AMAZON_FREERTOS_INC_PATH=AMAZON_FREERTOS_INC_PATH_DEFAULT
        AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_DEFAULT
    else:
        Log.writeInfoMessage("Amazon module")
        AMAZON_FREERTOS_INC_PATH="../src/config/"+configName+"/amazon-freertos/"
        AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_H3


    formatIncFiles()
    AddAWSFile(aws_cloud,"../",  "",Module.getPath()+CONFIG_COMMON_AFR , False )
    if (coreArch == "MIPS"):
        AddMIPS(aws_cloud,configName)
    elif (coreArch == "CORTEX-M4"):
        AddSAME54(aws_cloud,configName)
    elif (coreArch == "CORTEX-M7"):
        AddSAME70(aws_cloud,configName)




def AddFileTemplate(updateOnlyPath, component, strPath, strFileName, strDestPath,strProjectPath,strType="SOURCE",bMarkup=True):
    if updateOnlyPath:
        component.getSymbolByID(strPath.upper()).setDestPath(strDestPath)
    else:
        configName = Variables.get("__CONFIGURATION_NAME")

        freeRtosAddFile = component.createFileSymbol(strPath.upper(), None)
        freeRtosAddFile.setSourcePath("templates/demos/" + strFileName)

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


def AddFile(updateOnlyPath, component, strPath, strFileName, strDestPath,strProjectPath,bOverWrite=True,strType="SOURCE",bMarkup=False):
    if updateOnlyPath:
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


def AddDir(root,component,strPath, strRelativeFilePath,strProjectPath, updateOnlyPath):
    for child in root:
        if child.tag == XML_ATTRIB_DIR:
            NewstrPath = strPath + "/" + str(child.attrib[XML_ATTRIB_NAME])
            NewstrRelativeFilePath = strRelativeFilePath +  "/" + str(child.attrib[XML_ATTRIB_NAME])
            NewstrProjectPath = strProjectPath +  "/" + str(child.attrib[XML_ATTRIB_NAME])
            AddDir(child,component,NewstrPath, NewstrRelativeFilePath ,NewstrProjectPath, updateOnlyPath)
        if child.tag == XML_ATTRIB_FILE:
            NewstrPath = strPath + "/" + str(child.attrib[XML_ATTRIB_NAME])
            if( (XML_ATTRIB_OVER_WRITE in child.attrib) and child.attrib[XML_ATTRIB_OVER_WRITE] == "false"):
                AddFile(updateOnlyPath, component,NewstrPath, str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath ,strProjectPath,False)
            else:
                AddFile(updateOnlyPath, component,NewstrPath, str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath ,strProjectPath)

        elif child.tag == XML_ATTRIB_TEMPLATE:
            NewstrPath = strPath + "/" + str(child.attrib[XML_ATTRIB_NAME])
            AddFileTemplate(updateOnlyPath, component,NewstrPath, str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath ,strProjectPath)



def AddAWSFile(component,strPath, strRelativeFilePath, strXmlFile, updateOnlyPath):
    global AMAZON_FREERTOS_PATH
    tree = ET.parse(strXmlFile)
    root = tree.getroot()
    for child in root:
        if child.tag == XML_ATTRIB_DIR:
            AddDir(child,component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), AMAZON_FREERTOS_PATH + strRelativeFilePath +  "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath +  "/" + str(child.attrib[XML_ATTRIB_NAME]), updateOnlyPath)
        if child.tag == XML_ATTRIB_FILE:
            if( (XML_ATTRIB_OVER_WRITE in child.attrib)):
                AddFile(updateOnlyPath, component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath+ "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath + "/" + str(child.attrib[XML_ATTRIB_NAME]),False)
            else:
                AddFile(updateOnlyPath, component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath+ "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath + "/" + str(child.attrib[XML_ATTRIB_NAME]))
        if child.tag == XML_ATTRIB_TEMPLATE:
            AddFileTemplate(updateOnlyPath, component,strPath + "/" + str(child.attrib[XML_ATTRIB_NAME]), str(child.attrib[XML_ATTRIB_NAME]), strRelativeFilePath+ "/" + str(child.attrib[XML_ATTRIB_NAME]),strRelativeFilePath + "/" + str(child.attrib[XML_ATTRIB_NAME]))



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
        freeRtosSymMenu = aws_cloud.createComboSymbol(config_name, parent_config,strValues)
        freeRtosSymMenu.setDefaultValue("SHADOW")
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


def AddMIPS(hw_interface,configName):
    global SAME54_PORT_DIR,SAME70_PORT_DIR,PIC32MZ_PORT_DIR,SAME54_INC_DIR,SAME70_INC_DIR,PIC32_INC_DIR
    global freeRtosdefSym1,freeRtosIncDirForAsm

    freeRtosIncDirForPre = hw_interface.createSettingSymbol("AFR1_XC32_AS_PRE_PROC_DIRS", None)
    freeRtosIncDirForPre.setCategory("C32")
    freeRtosIncDirForPre.setKey("preprocessor-macros")
    freeRtosIncDirForPre.setValue("PIC32_USE_ETHERNET;__free_rtos__;")
    freeRtosIncDirForPre.setAppend(True, ";")
    symOptions = hw_interface.createSettingSymbol(None, None)
    symOptions.setCategory("C32")
    symOptions.setKey("appendMe")
    symOptions.setValue("-mnewlib-libc -std=gnu99 -fgnu89-inline")
    symOptions.setAppend(True, ";")
    freeRtosdefSym1 = hw_interface.createSettingSymbol("AFR1_XC32_INCLUDE_DIRS", None)
    freeRtosdefSym1.setCategory("C32")
    freeRtosdefSym1.setKey("extra-include-directories")
    freeRtosdefSym1.setValue(PIC32_INC_DIR)
    freeRtosdefSym1.setAppend(True, ";")
    freeRtosIncDirForLd = hw_interface.createSettingSymbol("AFR_XC32_INCLUDE_LD", None)
    freeRtosIncDirForLd.setCategory("C32-LD")
    freeRtosIncDirForLd.setKey("oXC32ld-extra-opts")
    freeRtosIncDirForLd.setValue("-mnewlib-libc")
    freeRtosIncDirForLd.setAppend(True, ";")
    freeRtosIncDirForAsm = hw_interface.createSettingSymbol("AFR_XC32_INCLUDE_ASM1", None)
    freeRtosIncDirForAsm.setCategory("C32-AS")
    freeRtosIncDirForAsm.setKey("extra-include-directories-for-preprocessor")
    freeRtosIncDirForAsm.setValue(PIC32_INC_DIR)
    freeRtosIncDirForAsm.setAppend(True, ";")

def AddSAME54(hw_interface,configName):
    global SAME54_PORT_DIR,SAME70_PORT_DIR,PIC32MZ_PORT_DIR,SAME54_INC_DIR,SAME70_INC_DIR,PIC32_INC_DIR
    global freeRtosdefSym2
    freeRtosIncDirForPre = hw_interface.createSettingSymbol("AFR2_XC32_AS_PRE_PROC_DIRS", None)
    freeRtosIncDirForPre.setCategory("C32")
    freeRtosIncDirForPre.setKey("preprocessor-macros")
    freeRtosIncDirForPre.setValue("PIC32_USE_ETHERNET")
    freeRtosIncDirForPre.setAppend(True, ";")
    freeRtosdefSym2 = hw_interface.createSettingSymbol("AFR2_XC32_INCLUDE_DIRS", None)
    freeRtosdefSym2.setCategory("C32")
    freeRtosdefSym2.setKey("extra-include-directories")
    freeRtosdefSym2.setValue(SAME54_INC_DIR)
    freeRtosdefSym2.setAppend(True, ";")
    res = Database.activateComponents(["TRNG"])


def AddSAME70(hw_interface,configName):
    global SAME54_PORT_DIR,SAME70_PORT_DIR,PIC32MZ_PORT_DIR,SAME54_INC_DIR,SAME70_INC_DIR,PIC32_INC_DIR
    global freeRtosdefSym3

    freeRtosIncDirForPre = hw_interface.createSettingSymbol("AFR3_XC32_AS_PRE_PROC_DIRS", None)
    freeRtosIncDirForPre.setCategory("C32")
    freeRtosIncDirForPre.setKey("preprocessor-macros")
    freeRtosIncDirForPre.setValue("PIC32_USE_ETHERNET")
    freeRtosIncDirForPre.setAppend(True, ";")
    freeRtosdefSym3 = hw_interface.createSettingSymbol("AFR3_XC32_INCLUDE_DIRS", None)
    freeRtosdefSym3.setCategory("C32")
    freeRtosdefSym3.setKey("extra-include-directories")
    freeRtosdefSym3.setValue(SAME70_INC_DIR)
    freeRtosdefSym3.setAppend(True, ";")
