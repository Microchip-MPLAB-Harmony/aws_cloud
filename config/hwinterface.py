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
autoConnectTableDebug = [["sys_debug", "sys_debug_SYS_CONSOLE_dependency", "sys_console_0","sys_console"]]
autoConnectTableCmd = [["sys_command", "sys_command_SYS_CONSOLE_dependency", "sys_console_0","sys_console"]]

# This component supports code generation of amazon-freertos and two different locations
#  1. As per amazon-freertos guidelines
#  2. As per Harmony 3 guidelines.
#
# The amazon-freertos guidelines are used only for the projects in MicrochipTech github.
AMAZON_FREERTOS_PATH_DEFAULT="../../../../../../../../../../"
AMAZON_FREERTOS_PATH_H3=""
AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_DEFAULT

# Based on where code is generated, the include folder settings would change accordingly.
AMAZON_FREERTOS_INC_PATH_DEFAULT="../../../../../../../"
AMAZON_FREERTOS_INC_H3="../"

CONFIG_FREERTOS="FreeRTOS"
CONFIG_MICRIUM="MicriumOSIII"
CONFIG_MIPS="MIPS"
CONFIG_M4="CORTEX-M4"
CONFIG_M7="CORTEX-M7"
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
CONFIG_DEMOS=0
CONFIG_DEVICE_TESTER=1
CONFIG_WIRED=0
CONFIG_WIRELESS=2
CONFIG_FLASH_PKCS11=0
CONFIG_SECURE_PKCS11=1

connected_components=["AmazonFreeRTOS", "AmazonDeviceTester"]
connected_elements=["aws_demos","aws_tests"]
connected_dep=["demos","DT"]
connected_dep_index=CONFIG_DEVICE_TESTER
hw_connection_index=CONFIG_WIRED
pkcs11_conn_index=CONFIG_FLASH_PKCS11

CONFIG_WIRED_FLASH=0
CONFIG_WIRED_ECC=1
CONFIG_WIRELESS_ECC=2

ETHERNET_CONFIG="Ethernet Only"
ETHERNET_ECC_CONFIG="Ethernet + ECC608"
WIRELESS_ECC_CONFIG="Wifi + ECC608"
WIRELESS_CONFIG="Wireless Only" # Not added, since it is not requested/tested.

config_aws_conf=[ETHERNET_CONFIG,ETHERNET_ECC_CONFIG,WIRELESS_ECC_CONFIG]

#global variables
# Below variables are used for settings, which are enabled/disabled at run time only.
freeRtosPreProc=[]
freeRtosdefSym1=[]
freeRtosdefSym2=[]
SAME54_INC_DIR=[]
SAME70_INC_DIR=[]
PIC32_INC_DIR=[]

global hw_interface, aws_cloud_h3_conf,aws_cloud_h3,awsSystemDefFile


#Instatntiate FreeRTOS Component
def instantiateComponent(aws_cloud):
    global connected_dep_index, AMAZON_FREERTOS_PATH,AMAZON_FREERTOS_PATH_DEFAULT,aws_cloud_h3,connected_dep,pkcs11_conn_index,hw_connection_index
    global config_aws,config_aws_conf,aws_cloud_h3_conf,AMAZON_FREERTOS_INC_H3,awsSystemDefFile
    Log.writeInfoMessage("Running AmazonFreeRTOS interface")
    global hw_interface
    hw_interface=aws_cloud
    # Deactivate the active RTOS if any.
    deactivateActiveRtos()
    res = Database.activateComponents(["HarmonyCore"])
    configName = Variables.get("__CONFIGURATION_NAME")

    if(Database.getComponentByID("sys_time") == None):
        res = Database.activateComponents(["sys_time"])

    if(Database.getComponentByID("sys_console") == None):
        res = Database.activateComponents(["sys_console"])

    if(Database.getComponentByID("sys_debug") == None):
        res = Database.activateComponents(["sys_debug"])
        res = Database.connectDependencies(autoConnectTableDebug)
    if(Database.getComponentByID("sys_command") == None):
        res = Database.activateComponents(["sys_command"])
        res = Database.connectDependencies(autoConnectTableCmd)

    if ((coreArch == CONFIG_M4) or (coreArch == CONFIG_M7)):
        if(Database.getComponentByID("trng") == None):
            res = Database.activateComponents(["trng"])

    if ((coreArch == CONFIG_MIPS)):
        if(Database.getComponentByID("nvm") == None):
            res = Database.activateComponents(["nvm"])
        if(Database.getComponentByID("rng") == None):
            res = Database.activateComponents(["rng"])

    #FreeRTOS Configuration Menu
    if(Database.getComponentByID("AmazonFreeRTOS") != None):
        connected_dep_index=CONFIG_DEMOS
    else:
        connected_dep_index=CONFIG_DEVICE_TESTER
    freeRtosIntConfig()
    Database.setSymbolValue("HarmonyCore", "SELECT_RTOS","FreeRTOS")
    aws_cloud_h3 = hw_interface.createBooleanSymbol("HW_AWS_CLOUD_H3", None)
    aws_cloud_h3.setLabel("aws cloud")
    aws_cloud_h3.setVisible(False)
    aws_cloud_h3.setDefaultValue(False)
    aws_cloud_h3.setDependencies(setH3DirectoryEnable,["AmazonFreeRTOS.AWS_CLOUD_H3"])
    aws_cloud_h3_dt = hw_interface.createBooleanSymbol("DT_HW_AWS_CLOUD_H3", None)
    aws_cloud_h3_dt.setLabel("aws cloud_dt")
    aws_cloud_h3_dt.setVisible(False)
    aws_cloud_h3_dt.setDefaultValue(False)
    aws_cloud_h3_dt.setDependencies(setH3DirectoryEnable,["AmazonDeviceTester.AWS_CLOUD_H3"])
    aws_cloud_h3_conf = hw_interface.createComboSymbol("H3_AWS_CLOUD_CONF", None,config_aws_conf)
    aws_cloud_h3_conf.setLabel("Hardware Configuration")
    aws_cloud_h3_conf.setVisible(True)
    aws_cloud_h3_conf.setDefaultValue(config_aws_conf[0])
    aws_cloud_h3_conf.setDependencies(setH3ConfEnable,["H3_AWS_CLOUD_CONF"])
    Log.writeInfoMessage("Running AmazonFreeRTOS interface SSA  SS " + str(config_aws_conf.index(aws_cloud_h3_conf.getValue())))


    if(config_aws_conf.index(aws_cloud_h3_conf.getValue())==CONFIG_WIRED_FLASH):
        hw_interface.setDependencyEnabled("Amazon_Secure_Element", False)
        hw_interface.setDependencyEnabled("WDRV_WINC", False)
        hw_interface.setDependencyEnabled("NETCONFIG_MAC_Dependency", True)
    elif (config_aws_conf.index(aws_cloud_h3_conf.getValue())==CONFIG_WIRED_ECC):
        hw_interface.setDependencyEnabled("Amazon_Secure_Element", True)
        hw_interface.setDependencyEnabled("WDRV_WINC", False)
        hw_interface.setDependencyEnabled("NETCONFIG_MAC_Dependency", True)
    else:
        hw_interface.setDependencyEnabled("NETCONFIG_MAC_Dependency", False)
        hw_interface.setDependencyEnabled("Amazon_Secure_Element", True)
        hw_interface.setDependencyEnabled("WDRV_WINC", True)


    if(config_aws_conf.index(aws_cloud_h3_conf.getValue()) == CONFIG_WIRED_FLASH):
        pkcs11_conn_index=CONFIG_FLASH_PKCS11
        hw_connection_index=CONFIG_WIRED
    elif(config_aws_conf.index(aws_cloud_h3_conf.getValue()) == CONFIG_WIRED_ECC):
        pkcs11_conn_index=CONFIG_SECURE_PKCS11
        hw_connection_index=CONFIG_WIRED
    else:
        pkcs11_conn_index=CONFIG_SECURE_PKCS11
        hw_connection_index=CONFIG_WIRELESS

    if(hw_connection_index == CONFIG_WIRED):
        awsSystemDefFile = hw_interface.createFileSymbol("AWS_SYS_DEF_HEADER", None)
        awsSystemDefFile.setType("STRING")
        awsSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        awsSystemDefFile.setSourcePath("templates/definitions.h.ftl")
        awsSystemDefFile.setMarkup(True)
        awsSystemDefFile.setEnabled(True)
    
        


############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")
    AMAZON_FREERTOS_INC_H3="../src/config/"+configName+"/amazon-freertos/"
    if(aws_cloud_h3.getValue() ==True):
        AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_DEFAULT
    else:
       AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_H3

    

    formatIncFiles()

    AddCommonIDEConfig(hw_interface,configName)	   

    if (coreArch == CONFIG_MIPS):
        AddMIPS(hw_interface,configName)

    AddAWSFile(hw_interface,"../", "",Module.getPath()+"config/"+ connected_dep[connected_dep_index] + "/" + coreArch+".xml", False)
    freeRtosIncWarn = hw_interface.createSettingSymbol("AFR_XC32_WARNING", None)
    freeRtosIncWarn.setCategory("C32")
    freeRtosIncWarn.setKey("make-warnings-into-errors")
    freeRtosIncWarn.setValue("false")
    AddAWSConfig(hw_interface,Module.getPath()+"config/UI/" + connected_dep[connected_dep_index] + "_"+ coreArch+".xml")


###############################################################################
########################## FreeRTOS Configurations ############################
###############################################################################
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


def deactivateActiveRtos():
    activeComponents = Database.getActiveComponentIDs()

    for i in range(0, len(activeComponents)):
        if (activeComponents[i] == CONFIG_FREERTOS):
            res = Database.deactivateComponents([CONFIG_FREERTOS])
        if (activeComponents[i] == CONFIG_MICRIUM):
            res = Database.deactivateComponents([CONFIG_MICRIUM])


#############################################################
### ADD DIR, ADD FILE, ADD Template methods
#############################################################

# Add File Template
def AddFileTemplate(boolFileEnable, boolDisableGen, component, strPath, strFileName, strDestPath,strProjectPath,strType="SOURCE",bMarkup=True):
    global coreArch 
    if  boolDisableGen:
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
        freeRtosAddFile.setEnabled(boolFileEnable)

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
    global pkcs11_conn_index
    global hw_connection_index
    temp_disable_file=True
    aws_config_temp="aws_config"
    list_ecc_wired=["NVM","WIFI"]
    list_wireless=["NVM","MAC"]
    list_wired=["ECC","WIFI"]
    if pkcs11_conn_index == 0:
        list_temp=list_wired
    elif hw_connection_index == 2:
        list_temp=list_wireless
    else:
        list_temp=list_ecc_wired
    
          
    if boolDirEnable == False or (aws_config_temp in child.attrib and (child.attrib[aws_config_temp] in list_temp)):
        temp_disable_file=False
        Log.writeInfoMessage( "Disable DIR " + str(hw_connection_index) +" " + str(pkcs11_conn_index) + " " + str(child.attrib[XML_ATTRIB_NAME]))

    return temp_disable_file

    

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


####################################################################################################
############# 
####################################################################################################
def formatIncFiles():
    SAME54_PORT_DIR=[]
    global SAME54_INC_DIR,SAME70_INC_DIR,PIC32_INC_DIR
    global connected_dep_index,connected_elements
    global AMAZON_FREERTOS_INC_PATH_DEFAULT
    global AMAZON_FREERTOS_INC_H3
    SAME54_PORT_DIR=[]
    SAME70_PORT_DIR=[]
    PIC32MZ_PORT_DIR=[]
    AFR_COMMON_INC_DIR=[]
    AFR_TEST_INC_DIR=[]
    

    # For better code readability, some of the arrays are duplicated.
    include_dir_path=[AMAZON_FREERTOS_INC_H3,AMAZON_FREERTOS_INC_H3,AMAZON_FREERTOS_INC_PATH_DEFAULT,AMAZON_FREERTOS_INC_PATH_DEFAULT]

    for i in range(4):
        SAME54_PORT_DIR.append(include_dir_path[i] +"vendors/microchip/boards/same54_xpro/ports/pkcs11;" +
                           include_dir_path[i] +"libraries/abstractions/wifi/include;" +
                           include_dir_path[i] +"vendors/microchip/boards/same54/ports/wifi;" +
                           include_dir_path[i] +"vendors/microchip/harmony3/afr;" +
                           include_dir_path[i] +"vendors/microchip/boards/same54_xpro/"+ connected_elements[i % 2] + "/config_files;" +
                           include_dir_path[i] +"vendors/microchip/boards/same54_xpro/"+ connected_elements[i % 2] + "/application_code;" +
                           include_dir_path[i] +"vendors/microchip/boards/same54_xpro/ports/posix;" +
                           include_dir_path[i] +"freertos_kernel/portable/GCC/ARM_CM4F;" +
                           include_dir_path[i] +"vendors/microchip/harmony3/afr/tcpip/src/common;" +
                           include_dir_path[i] +"libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/NetworkInterface/same54;")


        SAME70_PORT_DIR.append(include_dir_path[i] +"vendors/microchip/boards/same70_xult/ports/pkcs11;" +
                           include_dir_path[i] +"libraries/abstractions/wifi/include;" +
                           include_dir_path[i] +"vendors/microchip/harmony3/afr;" +
                           include_dir_path[i] +"vendors/microchip/boards/same70_xult/ports/wifi;" +
                           include_dir_path[i] +"vendors/microchip/boards/same70_xult/ports/posix;" +
                           include_dir_path[i] +"vendors/microchip/boards/same70_xult/"+ connected_elements[i % 2] + "/config_files;" +
                           include_dir_path[i] +"vendors/microchip/boards/same70_xult/"+ connected_elements[i % 2] + "/application_code;" +
                           include_dir_path[i] +"freertos_kernel/portable/GCC/ARM_CM7/r0p1;" +
                           include_dir_path[i] +"vendors/microchip/harmony3/afr/tcpip/src/common;" +
                           include_dir_path[i] +"libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/NetworkInterface/same70;")


        PIC32MZ_PORT_DIR.append(include_dir_path[i] +"vendors/microchip/boards/curiosity2_pic32mzef/ports/pkcs11;" +
                            include_dir_path[i] +"vendors/microchip/harmony3/afr;" +
                            include_dir_path[i] +"vendors/microchip/boards/curiosity2_pic32mzef/ports/posix;" +
                            include_dir_path[i] +"vendors/microchip/boards/curiosity2_pic32mzef/"+ connected_elements[i % 2] + "/config_files;" +
                            include_dir_path[i] +"vendors/microchip/boards/curiosity2_pic32mzef/"+ connected_elements[i % 2] + "/application_code;" +
                            include_dir_path[i] +"freertos_kernel/portable/MPLAB/PIC32MZ;"  +
                            include_dir_path[i] +"vendors/microchip/harmony3/afr/tcpip/src/common;" +
                            include_dir_path[i] +"libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/NetworkInterface/pic32mzef_h3;")

        AFR_COMMON_INC_DIR.append(include_dir_path[i] +"demos/include;" +
                          include_dir_path[i] +"freertos_kernel/include;" +
                          include_dir_path[i] +"libraries/abstractions/platform/freertos/include;" +
                          include_dir_path[i] +"libraries/abstractions/secure_sockets/include;" +
                          include_dir_path[i] +"libraries/abstractions/pkcs11/include;" +
                          include_dir_path[i] +"libraries/c_sdk/aws/defender/include;" +
                          include_dir_path[i] +"libraries/c_sdk/aws/shadow/include;" +
                          include_dir_path[i] +"libraries/c_sdk/standard/common/include;" +
                          include_dir_path[i] +"libraries/c_sdk/standard/https/include;" +
                          include_dir_path[i] +"libraries/c_sdk/standard/mqtt/include;" +
                          include_dir_path[i] +"libraries/c_sdk/standard/serializer/include;" +
                          include_dir_path[i] +"libraries/freertos_plus/aws/greengrass/include;" +
                          include_dir_path[i] +"libraries/freertos_plus/aws/ota/include;" +
                          include_dir_path[i] +"libraries/freertos_plus/standard/crypto/include;" +
                          include_dir_path[i] +"libraries/freertos_plus/standard/utils/include;" +
                          include_dir_path[i] +"libraries/freertos_plus/standard/tls/include;" +
                          include_dir_path[i] +"libraries/freertos_plus/standard/pkcs11/include;" +
                          include_dir_path[i] +"libraries/freertos_plus/standard/freertos_plus_tcp/include;" +
                          include_dir_path[i] +"libraries/abstractions/platform/include;" +
                          include_dir_path[i] +"libraries/c_sdk/standard/common/include/private;" +
                          include_dir_path[i] +"libraries/c_sdk/standard/common/include/types;" +
                          include_dir_path[i] +"libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/Compiler/GCC;" +
                          include_dir_path[i] +"demos/network_manager;" +
                          include_dir_path[i] +"demos/https;" +
                          include_dir_path[i] +"demos/tcp;" +
                          include_dir_path[i] +"libraries/3rdparty/jsmn;" +
                          include_dir_path[i] +"libraries/3rdparty/mbedtls/include;" +
                          include_dir_path[i] +"libraries/3rdparty/tinycbor;" +
                          include_dir_path[i] +"libraries/3rdparty/pkcs11;" +
                          include_dir_path[i] +"libraries/3rdparty/tinycrypt/asn1;" +
                          include_dir_path[i] +"libraries/3rdparty/tinycrypt/lib/include;" +
                          include_dir_path[i] +"demos/dev_mode_key_provisioning/include;" +
                          include_dir_path[i] +"libraries/abstractions/pkcs11/mbedtls;" +
                          include_dir_path[i] +"libraries/3rdparty/http_parser;" +
                          include_dir_path[i] +"libraries/freertos_plus/aws/ota/src;")

        AFR_TEST_INC_DIR.append(include_dir_path[i] + "freertos_kernel/include;" +
                        include_dir_path[i] + "libraries/c_sdk/standard/common/include;" +
                        include_dir_path[i] + "libraries/freertos_plus/standard/crypto/include;" +
                        include_dir_path[i] +"libraries/freertos_plus/standard/tls/include;" +
                        include_dir_path[i] + "libraries/freertos_plus/standard/freertos_plus_tcp/include;" +
                        include_dir_path[i] + "libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/Compiler/GCC;" +
                        include_dir_path[i] + "libraries/abstractions/pkcs11/include;" +
                        include_dir_path[i] +  "tests/include;" +
                        include_dir_path[i] + "libraries/c_sdk/standard/common/include/private;" +
                        include_dir_path[i] + "libraries/abstractions/platform/include;" +
                        include_dir_path[i] + "libraries/abstractions/platform/freertos/include;" +
                        include_dir_path[i] + "libraries/abstractions/secure_sockets/include;" +
                        include_dir_path[i] + "libraries/freertos_plus/standard/freertos_plus_tcp/test;" +
                        include_dir_path[i] + "libraries/freertos_plus/standard/pkcs11/include;" +
                        include_dir_path[i] + "libraries/freertos_plus/aws/ota/test;" +
                        include_dir_path[i] + "libraries/freertos_plus/standard/utils/include;" +
                        include_dir_path[i] + "demos/dev_mode_key_provisioning/include;" +
                        include_dir_path[i] + "libraries/c_sdk/aws/defender/include;" +
                        include_dir_path[i] + "libraries/c_sdk/standard/mqtt/test/access;" +
                        include_dir_path[i] + "libraries/c_sdk/standard/mqtt/include;" +
                        include_dir_path[i] + "libraries/c_sdk/standard/mqtt/src;" +
                        include_dir_path[i] + "libraries/c_sdk/standard/serializer/include;" +
                        include_dir_path[i] + "libraries/c_sdk/aws/shadow/include;" +
                        include_dir_path[i] + "libraries/c_sdk/aws/shadow/src;" +
                        include_dir_path[i] + "libraries/c_sdk/standard/https/test/access;" +
                        include_dir_path[i] + "libraries/c_sdk/standard/https/include;" +
                        include_dir_path[i] + "libraries/c_sdk/standard/https/src;" +
                        include_dir_path[i] + "libraries/freertos_plus/aws/greengrass/test;" +
                        include_dir_path[i] + "libraries/freertos_plus/aws/greengrass/include;" +
                        include_dir_path[i] + "libraries/freertos_plus/aws/greengrass/src;" +
                        include_dir_path[i] +"libraries/freertos_plus/aws/ota/src;" +
                        include_dir_path[i] +"libraries/freertos_plus/aws/ota/include;" +
                        include_dir_path[i] + "libraries/3rdparty/mbedtls/include;" +
                        include_dir_path[i] + "libraries/abstractions/posix/include;" +
                        include_dir_path[i] + "libraries/freertos_plus/standard/freertos_plus_posix/include;" +
                        include_dir_path[i] + "libraries/c_sdk/aws/defender/src/private;" +
                        include_dir_path[i] + "libraries/3rdparty/jsmn;" +
                        include_dir_path[i] + "libraries/3rdparty/pkcs11;" +
                        include_dir_path[i] + "libraries/3rdparty/tinycbor;" +
                        include_dir_path[i] + "libraries/3rdparty/tinycrypt/asn1;" +
                        include_dir_path[i] + "libraries/3rdparty/tinycrypt/lib/include;" +
                        include_dir_path[i] + "libraries/3rdparty/mbedtls/include/mbedtls;" +
                        include_dir_path[i] + "libraries/abstractions/pkcs11/mbedtls;" +
                        include_dir_path[i] + "libraries/3rdparty/unity/src;" +
                        include_dir_path[i] + "libraries/3rdparty/unity/extras/fixture/src;" +
                        include_dir_path[i] + "libraries/3rdparty/http_parser;" +
                        include_dir_path[i] + "libraries/freertos_plus/standard/freertos_plus_tcp/source/portable/Compiler/GCC;")

    for i in range(4):
        if (i % 2 == 0):
            SAME54_INC_DIR.append(AFR_COMMON_INC_DIR[i] + SAME54_PORT_DIR[i])
            SAME70_INC_DIR.append(AFR_COMMON_INC_DIR[i] + SAME70_PORT_DIR[i])
            PIC32_INC_DIR.append(AFR_COMMON_INC_DIR[i] + PIC32MZ_PORT_DIR[i])
        else:
            SAME54_INC_DIR.append(AFR_TEST_INC_DIR[i] + SAME54_PORT_DIR[i])
            SAME70_INC_DIR.append(AFR_TEST_INC_DIR[i] + SAME70_PORT_DIR[i])
            PIC32_INC_DIR.append(AFR_TEST_INC_DIR[i] + PIC32MZ_PORT_DIR[i])

############################################################################
#### Add MPLAB Additional configurations (AddSAME54, AddSAME70, ADDMIPS)
############################################################################

############################################################################
#### Methods to support run time Directory location Change, Files Change ####
############################################################################
def setH3DirectoryEnable(symbol, event):
    global AMAZON_FREERTOS_PATH,AMAZON_FREERTOS_PATH_H3,AMAZON_FREERTO,S_PATH_DEFAULTconnected_dep_index,connected_dep
    global coreArch
    global freeRtosdefSym2,freeRtosdefSym1
    
    configName = Variables.get("__CONFIGURATION_NAME")
    symbol.setValue(event['symbol'].getValue())
    iIndex=0
    if(connected_dep_index == CONFIG_DEVICE_TESTER):
        iIndex=1
        
    if(event['symbol'].getValue() == True):
        AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_DEFAULT
        iIndex = iIndex + 2
    else:
        AMAZON_FREERTOS_PATH=AMAZON_FREERTOS_PATH_H3

    for i in range(4):
        if(i== iIndex):
            freeRtosdefSym1[i].setEnabled(True)
            if(coreArch == CONFIG_MIPS):
                freeRtosdefSym2[i].setEnabled(True)  # MIPS only
        else:
            freeRtosdefSym1[i].setEnabled(False)
            if(coreArch == CONFIG_MIPS):
                freeRtosdefSym2[i].setEnabled(False)# MIPS only

    #Change include directory enable/disable.
    
    if(Database.getComponentByID(connected_components[connected_dep_index]) != None):
        Log.writeInfoMessage("Running X " + connected_components[connected_dep_index] +" Component *" + str(event['symbol'].getValue()))
        AddAWSFile(symbol.getComponent(),"../", "",Module.getPath()+"config/"+ connected_dep[connected_dep_index] + "/" + coreArch+".xml", True)


def setH3ConfEnable(symbol, event):
    global AMAZON_FREERTOS_PATH,AMAZON_FREERTOS_PATH_H3,connected_dep_index,connected_dep
    global coreArch
    global config_aws_conf, hw_interface
    configName = Variables.get("__CONFIGURATION_NAME")
    localComponent = event["symbol"].getComponent()
    global pkcs11_conn_index,awsSystemDefFile
    global hw_connection_index,freeRtosPreProc

    if(config_aws_conf.index(event['symbol'].getValue())==CONFIG_WIRED_FLASH):
        
        localComponent.setDependencyEnabled("WDRV_WINC", False)
        localComponent.setDependencyEnabled("NETCONFIG_MAC_Dependency", True)
        localComponent.setDependencyEnabled("Amazon_Secure_Element", False)
        pkcs11_conn_index=CONFIG_FLASH_PKCS11
        hw_connection_index=CONFIG_WIRED
        awsSystemDefFile.setEnabled(True)
    elif (config_aws_conf.index(event['symbol'].getValue())==CONFIG_WIRED_ECC):
        
        localComponent.setDependencyEnabled("WDRV_WINC", False)
        localComponent.setDependencyEnabled("NETCONFIG_MAC_Dependency", True)
        localComponent.setDependencyEnabled("Amazon_Secure_Element", False)
        pkcs11_conn_index=CONFIG_SECURE_PKCS11
        hw_connection_index=CONFIG_WIRED
        awsSystemDefFile.setEnabled(True)
    else:
        localComponent.setDependencyEnabled("NETCONFIG_MAC_Dependency", False)
        localComponent.setDependencyEnabled("WDRV_WINC", True)
        localComponent.setDependencyEnabled("Amazon_Secure_Element", False)
        pkcs11_conn_index=CONFIG_SECURE_PKCS11
        hw_connection_index=CONFIG_WIRELESS
        awsSystemDefFile.setEnabled(False)


    iIndex=0
    if(connected_dep_index == CONFIG_DEVICE_TESTER):
        iIndex=3
    if(hw_connection_index==CONFIG_WIRED):
        if(pkcs11_conn_index==CONFIG_SECURE_PKCS11):
            iIndex = iIndex + 1
    else:
        iIndex = iIndex + 2

    for i in range(6):
        if(i== iIndex):
            freeRtosPreProc[i].setEnabled(True);
        else:
            freeRtosPreProc[i].setEnabled(False);
       
    if(Database.getComponentByID(connected_components[connected_dep_index]) != None):
        AddAWSFile(symbol.getComponent(),"../", "",Module.getPath()+"config/"+ connected_dep[connected_dep_index] + "/" + coreArch+".xml", True)
        

def AddCommonIDEConfig(hw_interface,configName):
    global PIC32_INC_DIR,SAME70_INC_DIR,SAME54_INC_DIR
    global freeRtosdefSym1,freeRtosdefSym2
    global connected_dep_index
    global hw_connection_index
    global pkcs11_conn_index
    global aws_cloud_h3,config_aws_conf
    

    strIncludeWired=";PIC32_USE_ETHERNET;__free_rtos__"
    strIncludeWiredecc=";PIC32_USE_ECC;PIC32_USE_ETHERNET;__free_rtos__"
    strIncludeWireless=";PIC32_USE_ECC;__free_rtos__"
    strDT=";UNITY_INCLUDE_CONFIG_H;AMAZON_FREERTOS_ENABLE_UNIT_TESTS"
    strIncludeWiredDT=strDT+strIncludeWired
    strIncludeWiredeccDT=strDT+strIncludeWiredecc
    strIncludeWirelessDT=strDT+strIncludeWireless
    
    strInclude =[strIncludeWired,strIncludeWiredecc,strIncludeWireless,strIncludeWiredDT,strIncludeWiredeccDT,strIncludeWirelessDT]
   
    for i in range(6):
        freeRtosPreProc.append(hw_interface.createSettingSymbol("AFR2_XC32_AS_PRE_PROC_DIRS" + str(i), None))
        freeRtosPreProc[i].setCategory("C32")
        freeRtosPreProc[i].setKey("preprocessor-macros")
        freeRtosPreProc[i].setValue(strInclude[i])
        freeRtosPreProc[i].setAppend(True, ";")
        freeRtosPreProc[i].setEnabled(False)

    for i in range(4):
        freeRtosdefSym1.append(hw_interface.createSettingSymbol("AFR1_XC32_INCLUDE_DIRS"+ str(i), None))
        if(coreArch == CONFIG_MIPS):
            freeRtosdefSym2.append(hw_interface.createSettingSymbol("AFR_XC32_INCLUDE_ASM"+ str(i), None))
        freeRtosdefSym1[i].setCategory("C32")
        freeRtosdefSym1[i].setKey("extra-include-directories")
        if(coreArch == CONFIG_MIPS):
            freeRtosdefSym1[i].setValue(PIC32_INC_DIR[i])
        if(coreArch == CONFIG_M4):
            freeRtosdefSym1[i].setValue(SAME54_INC_DIR[i])
        if(coreArch == CONFIG_M7):
            freeRtosdefSym1[i].setValue(SAME70_INC_DIR[i])            
        freeRtosdefSym1[i].setAppend(True, ";")
        freeRtosdefSym1[i].setEnabled(False)

        if(coreArch == CONFIG_MIPS):
            freeRtosdefSym2[i].setCategory("C32-AS")
            freeRtosdefSym2[i].setKey("extra-include-directories-for-preprocessor")
            freeRtosdefSym2[i].setValue(PIC32_INC_DIR[i])
            freeRtosdefSym2[i].setAppend(True, ";")
            freeRtosdefSym2[i].setEnabled(False)


    iIndex = config_aws_conf.index(aws_cloud_h3_conf.getValue())
    
    freeRtosPreProc[3*connected_dep_index + iIndex].setEnabled(True) #[MAC,MAC+ECC,WIFI (demos), MAC,MAC+ECC,WIFI (DT)]
    if(aws_cloud_h3.getValue() == True):
        Log.writeInfoMessage("Running H3 Config " + str(iIndex))
        freeRtosdefSym1[connected_dep_index + 2].setEnabled(True)  #[H3 demo,H3 DT, AFR demo,AFR (DT)]
        if(coreArch == CONFIG_MIPS):
            freeRtosdefSym2[connected_dep_index + 2].setEnabled(True)  #[H3 demo,H3 DT, AFR demo,AFR (DT)]
    else:
        Log.writeInfoMessage("Running H3 Config 2 " + str(iIndex))
        freeRtosdefSym1[connected_dep_index].setEnabled(True)  #[H3 demo,H3 DT, AFR demo,AFR (DT)]
        if(coreArch == CONFIG_MIPS):
            freeRtosdefSym2[connected_dep_index].setEnabled(True)  #[H3 demo,H3 DT, AFR demo,AFR (DT)]

            
def AddMIPS(hw_interface,configName):
    symOptions = hw_interface.createSettingSymbol(None, None)
    symOptions.setCategory("C32")
    symOptions.setKey("appendMe")
    symOptions.setValue("-mnewlib-libc -std=gnu99 -fgnu89-inline")
    symOptions.setAppend(True, ";")
    freeRtosIncDirForLd = hw_interface.createSettingSymbol("AFR_XC32_INCLUDE_LD", None)
    freeRtosIncDirForLd.setCategory("C32-LD")
    freeRtosIncDirForLd.setKey("oXC32ld-extra-opts")
    freeRtosIncDirForLd.setValue("-mnewlib-libc")
    freeRtosIncDirForLd.setAppend(True, ";")
