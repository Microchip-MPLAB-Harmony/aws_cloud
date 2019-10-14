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
# Fetch Core Architecture and Family details
coreArch     = Database.getSymbolValue("core", "CoreArchitecture")
coreFamily   = ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "family" )


###############################################################################
########################## FreeRTOS Configurations ############################
###############################################################################

def deactivateActiveRtos():
    activeComponents = Database.getActiveComponentIDs()

    for i in range(0, len(activeComponents)):
        if (activeComponents[i] == "FreeRTOS"):
            res = Database.deactivateComponents(["FreeRTOS"])




#Instatntiate FreeRTOS Component
def instantiateComponent(thirdPartyFreeRTOS):
    Log.writeInfoMessage("Running FreeRTOS")

    # Deactivate the active RTOS if any.
    deactivateActiveRtos()
    res = Database.activateComponents(["HarmonyCore"])


    #FreeRTOS Configuration Menu
    freeRtosSymMenu = thirdPartyFreeRTOS.createMenuSymbol("AWS_FREERTOS_MENU", None)
    freeRtosSymMenu.setLabel("AmazonFreeRTOS Configuration")
    freeRtosSymMenu.setDescription("List of AWS Options")



############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")
