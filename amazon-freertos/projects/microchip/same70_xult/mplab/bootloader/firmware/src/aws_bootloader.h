/****************************************************************
  Module for Microchip Bootloader Library

  Company:
    Microchip Technology Inc.

  File Name:
    aws_bootloader.h

  Summary:
    The header file joins all header files used in the Bootloader Library
    and contains compile options and defaults.

  Description:
    This header file includes all the header files required to use the
    Microchip Bootloader Library. Library features and options defined
    in the Bootloader Library configurations will be included in each build.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/


#ifndef _AWS_BOOTLOADER_H_
#define _AWS_BOOTLOADER_H_

#include <stdint.h>
#include <stdbool.h>

// enable launching if no valid image descriptor was found
// (the 1st time the part is programmed, for example)
#define     AWS_ENABLE_DEFAULT_START            1

// this is the default start address:
// the address where the OTA project builds the application
#define     AWS_DEFAULT_FLASH_IMAGE_START       (AWS_FLASH_RUN_APP_START)


// bootloader launch app signature 
#define AWS_BOOT_LAUNCH_SIGNATURE   "@AWS_Launch@"

// descriptor used to launch the application
typedef struct
{
    char        launch_sign[sizeof(AWS_BOOT_LAUNCH_SIGNATURE)];
    const void* launch_vector;
}AWS_BOOT_LAUNCH_DCPT;

extern AWS_BOOT_LAUNCH_DCPT aws_launch_dcpt;    // descriptor used to launch the application

// interface

// initialization
// returns true for success, 
// false otherwise
bool    AWS_Bootloader_Initialize(void);

// bootloader task, doing the job
void    AWS_Bootloader_Task(void);


#endif  // _AWS_BOOTLOADER_H_


