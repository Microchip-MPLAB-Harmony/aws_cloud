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

coreArch     = Database.getSymbolValue("core", "CoreArchitecture")
coreFamily   = ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "family" )
AMAZON_FREERTOS_PATH="../../../../../../../../../../"

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

SAME54_PORT_DIR = ("../../../../../../../vendors/microchip/boards/same54_xpro/ports/pkcs11;"
                   "../../../../../../../vendors/microchip/harmony3/afr;"
                   "../../../../../../../vendors/microchip/boards/same54_xpro/aws_demos/config_files;"
                   "../../../../../../../freertos_kernel/portable/GCC/ARM_CM4F;"
                   "../../../../../../../vendors/microchip/harmony3/afr/tcpip/src/common;"
                   "../../../../../../../libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/NetworkInterface/same54;")


SAME70_PORT_DIR = ("../../../../../../../vendors/microchip/boards/same70_xult/ports/pkcs11;"
		   "../../../../../../../vendors/microchip/harmony3/afr;"
		   "../../../../../../../vendors/microchip/boards/same70_xult/aws_demos/config_files;"
		   "../../../../../../../freertos_kernel/portable/GCC/ARM_CM7/r0p1;"
		   "../../../../../../../vendors/microchip/harmony3/afr/tcpip/src/common;"
                   "../../../../../../../libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/NetworkInterface/same70;")
				

PIC32MZ_PORT_DIR = ("../../../../../../../vendors/microchip/boards/curiosity2_pic32mzef/ports/pkcs11;"
		    "../../../../../../../vendors/microchip/harmony3/afr;"
		    "../../../../../../../vendors/microchip/boards/curiosity2_pic32mzef/aws_demos/config_files;"
		    "../../../../../../../freertos_kernel/portable/MPLAB/PIC32MZ;"
		    "../../../../../../../vendors/microchip/harmony3/afr/tcpip/src/common;"
                    "../../../../../../../libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/NetworkInterface/pic32mzef_h3;")
			

AFR_COMMON_INC_DIR = ("../../../../../../../demos/include;"
                      "../../../../../../../freertos_kernel/include;"
                      "../../../../../../../libraries/abstractions/platform/freertos/include;"
                      "../../../../../../../libraries/abstractions/secure_sockets/include;"
                      "../../../../../../../libraries/abstractions/pkcs11/include;"
                      "../../../../../../../libraries/c_sdk/aws/defender/include;"
                      "../../../../../../../libraries/c_sdk/aws/shadow/include;"
                      "../../../../../../../libraries/c_sdk/standard/common/include;"
                      "../../../../../../../libraries/c_sdk/standard/https/include;"
                      "../../../../../../../libraries/c_sdk/standard/mqtt/include;"
                      "../../../../../../../libraries/c_sdk/standard/serializer/include;"
                      "../../../../../../../libraries/freertos_plus/aws/greengrass/include;"
                      "../../../../../../../libraries/freertos_plus/aws/ota/include;"
                      "../../../../../../../libraries/freertos_plus/standard/crypto/include;"
                      "../../../../../../../libraries/freertos_plus/standard/utils/include;"
                      "../../../../../../../libraries/freertos_plus/standard/tls/include;"
                      "../../../../../../../libraries/freertos_plus/standard/pkcs11/include;"
                      "../../../../../../../libraries/freertos_plus/standard/freertos_plus_tcp/include;"
                      "../../../../../../../libraries/abstractions/platform/include;"
                      "../../../../../../../libraries/c_sdk/standard/common/include/private;"
                      "../../../../../../../libraries/c_sdk/standard/common/include/types;"
                      "../../../../../../../libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/Compiler/GCC;"
                      "../../../../../../../demos/network_manager;../../../../../../../demos/https;"
                      "../../../../../../../demos/tcp;../../../../../../../libraries/3rdparty/jsmn;"
                      "../../../../../../../libraries/3rdparty/mbedtls/include;"
                      "../../../../../../../libraries/3rdparty/tinycbor;"
                      "../../../../../../../libraries/3rdparty/pkcs11;"
                      "../../../../../../../libraries/3rdparty/tinycrypt/asn1;"
                      "../../../../../../../libraries/3rdparty/tinycrypt/lib/include;"
                      "../../../../../../../demos/dev_mode_key_provisioning/include;"
                      "../../../../../../../libraries/abstractions/pkcs11/mbedtls;"
                      "../../../../../../../libraries/3rdparty/http-parser;"
                      "../../../../../../../libraries/freertos_plus/aws/ota/src;")



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
    Log.writeInfoMessage("Running AmazonFreeRTOS")

    # Deactivate the active RTOS if any.
    deactivateActiveRtos()
    autoComponentIDTable = ["stdio"]
    res = Database.activateComponents(autoComponentIDTable)
    #AmazonFreeRTOS Configuration Menu
    
    AddAWSConfig(aws_cloud,Module.getPath()+ CONFIG_UI_COMMON_AFR)
    configName = Variables.get("__CONFIGURATION_NAME")
    
    if (coreArch == "MIPS"):
        AddMIPS(aws_cloud,configName)
    elif (coreArch == "CORTEX-M4"):
        AddSAME54(aws_cloud,configName)
    elif (coreArch == "CORTEX-M7"):
        AddSAME70(aws_cloud,configName)


    Log.writeInfoMessage(Module.getPath())
	
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
    AddAWSFile(aws_cloud,"../",  "",Module.getPath()+CONFIG_COMMON_AFR)
    


def AddFileTemplate(component, strPath, strFileName, strDestPath,strProjectPath,strType="SOURCE",bMarkup=True):
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
    freeRtosIncDirForPre = hw_interface.createSettingSymbol("AFR1_XC32_AS_PRE_PROC_DIRS", None)
    freeRtosIncDirForPre.setCategory("C32")
    freeRtosIncDirForPre.setKey("preprocessor-macros")
    freeRtosIncDirForPre.setValue("PIC32_USE_ETHERNET;__free_rtos__;")
    freeRtosIncDirForPre.setAppend(True, ";")
    freeRtosdefSym = hw_interface.createSettingSymbol("AFR1_XC32_INCLUDE_DIRS", None)
    freeRtosdefSym.setCategory("C32")
    freeRtosdefSym.setKey("extra-include-directories")
    freeRtosdefSym.setValue(PIC32_INC_DIR)
    freeRtosdefSym.setAppend(True, ";")
    freeRtosIncDirForAsm = hw_interface.createSettingSymbol("AFR_XC32_INCLUDE_ASM1", None)
    freeRtosIncDirForAsm.setCategory("C32-AS")
    freeRtosIncDirForAsm.setKey("extra-include-directories-for-preprocessor")
    freeRtosIncDirForAsm.setValue(PIC32_INC_DIR)
    freeRtosIncDirForAsm.setAppend(True, ";")

def AddSAME54(hw_interface,configName):
    freeRtosIncDirForPre = hw_interface.createSettingSymbol("AFR2_XC32_AS_PRE_PROC_DIRS", None)
    freeRtosIncDirForPre.setCategory("C32")
    freeRtosIncDirForPre.setKey("preprocessor-macros")
    freeRtosIncDirForPre.setValue("PIC32_USE_ETHERNET")
    freeRtosIncDirForPre.setAppend(True, ";")
    freeRtosdefSym = hw_interface.createSettingSymbol("AFR2_XC32_INCLUDE_DIRS", None)
    freeRtosdefSym.setCategory("C32")
    freeRtosdefSym.setKey("extra-include-directories")
    freeRtosdefSym.setValue(SAME54_INC_DIR)
    freeRtosdefSym.setAppend(True, ";")
    res = Database.activateComponents(["TRNG"])


def AddSAME70(hw_interface,configName):
    freeRtosIncDirForPre = hw_interface.createSettingSymbol("AFR3_XC32_AS_PRE_PROC_DIRS", None)
    freeRtosIncDirForPre.setCategory("C32")
    freeRtosIncDirForPre.setKey("preprocessor-macros")
    freeRtosIncDirForPre.setValue("PIC32_USE_ETHERNET")
    freeRtosIncDirForPre.setAppend(True, ";")
    freeRtosdefSym = hw_interface.createSettingSymbol("AFR3_XC32_INCLUDE_DIRS", None)
    freeRtosdefSym.setCategory("C32")
    freeRtosdefSym.setKey("extra-include-directories")
    freeRtosdefSym.setValue(SAME70_INC_DIR)
    freeRtosdefSym.setAppend(True, ";")
