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


coreArch     = Database.getSymbolValue("core", "CoreArchitecture")
coreFamily   = ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "family" )
autoConnectTableDebug = [["sys_debug", "sys_debug_SYS_CONSOLE_dependency", "sys_console"]]
autoConnectTableCmd = [["sys_command", "sys_command_SYS_CONSOLE_dependency", "sys_console"]]


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




AMAZON_FREERTOS_PATH="../../../../../../../../../../"
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
        if (activeComponents[i] == "FreeRTOS"):
            res = Database.deactivateComponents(["FreeRTOS"])
        if (activeComponents[i] == "MicriumOSIII"):
            res = Database.deactivateComponents(["MicriumOSIII"])


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
        if child.tag == "dir":
            NewstrPath = strPath + "/" + str(child.attrib["name"])
            NewstrRelativeFilePath = strRelativeFilePath +  "/" + str(child.attrib["name"])
            NewstrProjectPath = strProjectPath +  "/" + str(child.attrib["name"])
            AddDir(child,component,NewstrPath, NewstrRelativeFilePath ,NewstrProjectPath)
        if child.tag == "file":
            NewstrPath = strPath + "/" + str(child.attrib["name"])
            AddFile(component,NewstrPath, str(child.attrib["name"]), strRelativeFilePath ,strProjectPath)

def AddAWSFile(component,strPath, strRelativeFilePath, strXmlFile):
    tree = ET.parse(strXmlFile)
    root = tree.getroot()
    for child in root:
        if child.tag == "dir":
            AddDir(child,component,strPath + "/" + str(child.attrib["name"]), AMAZON_FREERTOS_PATH + strRelativeFilePath +  "/" + str(child.attrib["name"]),strRelativeFilePath +  "/" + str(child.attrib["name"]))
        if child.tag == "file":
            AddFile(component,strPath + "/" + str(child.attrib["name"]), str(child.attrib["name"]), strRelativeFilePath+ "/" + str(child.attrib["name"]),strRelativeFilePath + "/" + str(child.attrib["name"]))
        
   
#Instatntiate FreeRTOS Component
def instantiateComponent(aws_cloud):
    Log.writeInfoMessage("Running AmazonFreeRTOS")

    # Deactivate the active RTOS if any.
    deactivateActiveRtos()
    autoComponentIDTable = ["stdio"]
    res = Database.activateComponents(autoComponentIDTable)
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

    freeRtosIntConfig()
    Database.setSymbolValue("HarmonyCore", "SELECT_RTOS","FreeRTOS")

    #AmazonFreeRTOS Configuration Menu
    freeRtosSymMenu = aws_cloud.createMenuSymbol("AWS_FREERTOS_MENU", None)
    freeRtosSymMenu.setLabel("AmazonFreeRTOS Configuration")
    freeRtosSymMenu.setDescription("List of AWS Options")
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
    AddAWSFile(aws_cloud,"",  "",Module.getPath()+"config/Generated_"+coreArch+".xml")
    
    if (coreArch == "MIPS"):
        AddMIPS(aws_cloud,configName)
    elif (coreArch == "CORTEX-M4"):
        AddSAME54(aws_cloud,configName)
    elif (coreArch == "CORTEX-M7"):
        AddSAME70(aws_cloud,configName)

    freeRtosIncWarn = aws_cloud.createSettingSymbol("AFR_XC32_WARNING", None)
    freeRtosIncWarn.setCategory("C32")
    freeRtosIncWarn.setKey("make-warnings-into-errors")
    freeRtosIncWarn.setValue("false")
    


def AddMIPS(aws_cloud,configName):
    freeRtosIncDirForPre = aws_cloud.createSettingSymbol("AFR1_XC32_AS_PRE_PROC_DIRS", None)
    freeRtosIncDirForPre.setCategory("C32")
    freeRtosIncDirForPre.setKey("preprocessor-macros")
    freeRtosIncDirForPre.setValue("PIC32_USE_ETHERNET;__free_rtos__;")
    freeRtosIncDirForPre.setAppend(True, ";")
    freeRtosdefSym = aws_cloud.createSettingSymbol("AFR1_XC32_INCLUDE_DIRS", None)
    freeRtosdefSym.setCategory("C32")
    freeRtosdefSym.setKey("extra-include-directories")
    freeRtosdefSym.setValue(PIC32_INC_DIR)
    freeRtosdefSym.setAppend(True, ";")
    freeRtosIncDirForAsm = aws_cloud.createSettingSymbol("AFR_XC32_INCLUDE_ASM1", None)
    freeRtosIncDirForAsm.setCategory("C32-AS")
    freeRtosIncDirForAsm.setKey("extra-include-directories-for-preprocessor")
    freeRtosIncDirForAsm.setValue(PIC32_INC_DIR)
    freeRtosIncDirForAsm.setAppend(True, ";")

def AddSAME54(aws_cloud,configName):
    freeRtosIncDirForPre = aws_cloud.createSettingSymbol("AFR2_XC32_AS_PRE_PROC_DIRS", None)
    freeRtosIncDirForPre.setCategory("C32")
    freeRtosIncDirForPre.setKey("preprocessor-macros")
    freeRtosIncDirForPre.setValue("PIC32_USE_ETHERNET")
    freeRtosIncDirForPre.setAppend(True, ";")
    freeRtosdefSym = aws_cloud.createSettingSymbol("AFR2_XC32_INCLUDE_DIRS", None)
    freeRtosdefSym.setCategory("C32")
    freeRtosdefSym.setKey("extra-include-directories")
    freeRtosdefSym.setValue(SAME54_INC_DIR)
    freeRtosdefSym.setAppend(True, ";")
    res = Database.activateComponents(["TRNG"])


def AddSAME70(aws_cloud,configName):
    freeRtosIncDirForPre = aws_cloud.createSettingSymbol("AFR3_XC32_AS_PRE_PROC_DIRS", None)
    freeRtosIncDirForPre.setCategory("C32")
    freeRtosIncDirForPre.setKey("preprocessor-macros")
    freeRtosIncDirForPre.setValue("PIC32_USE_ETHERNET")
    freeRtosIncDirForPre.setAppend(True, ";")
    freeRtosdefSym = aws_cloud.createSettingSymbol("AFR3_XC32_INCLUDE_DIRS", None)
    freeRtosdefSym.setCategory("C32")
    freeRtosdefSym.setKey("extra-include-directories")
    freeRtosdefSym.setValue(SAME70_INC_DIR)
    freeRtosdefSym.setAppend(True, ";")



