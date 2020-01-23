/*
 * FreeRTOS Kernel V10.2.0
 * Copyright (C) 2017 Amazon.com, Inc. or its affiliates.  All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 * the Software, and to permit persons to whom the Software is furnished to do so,
 * subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 * FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 * COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 * http://aws.amazon.com/freertos
 * http://www.FreeRTOS.org
 */

#ifndef FREERTOS_CONFIG_H
#define FREERTOS_CONFIG_H

#include <xc.h>

#if defined( __LANGUAGE_C__ )
    #include "system/console/sys_console.h"
    #include "system/debug/sys_debug.h"
    #include "system/command/sys_command.h"
    #include "unity_internals.h"
#endif
/*-----------------------------------------------------------
* Application specific definitions.
*
* These definitions should be adjusted for your particular hardware and
* application requirements.
*
* THESE PARAMETERS ARE DESCRIBED WITHIN THE 'CONFIGURATION' SECTION OF THE
* FreeRTOS API DOCUMENTATION AVAILABLE ON THE FreeRTOS.org WEB SITE.
*
* See http://www.freertos.org/a00110.html.
*----------------------------------------------------------*/


#define configUSE_PREEMPTION                       <#if AWS_CLOUD_FREERTOS_USE_PREEMPTION == true>1<#else>0</#if> 
#define configUSE_PORT_OPTIMISED_TASK_SELECTION    <#if AWS_CLOUD_FREERTOS_USE_PORT_OPTIMIZED == true>1<#else>0</#if> 
#define configUSE_TICKLESS_IDLE                    <#if AWS_CLOUD_FREERTOS_TICLESS_IDLE == true>1<#else>0</#if> 
#define configCPU_CLOCK_HZ                      ( ${AWS_CLOUD_FREERTOS_CPU_CLOCK}UL )
#define configPERIPHERAL_CLOCK_HZ                  ( ${AWS_CLOUD_FREERTOS_PERI_CLOCK}UL )
#define configTICK_RATE_HZ                         ( ( TickType_t ) ${AWS_CLOUD_FREERTOS_TICK_RATE} )
#define configMAX_PRIORITIES                       (${AWS_CLOUD_FREERTOS_MAX_PRI}UL)
#define configMINIMAL_STACK_SIZE                   (${AWS_CLOUD_FREERTOS_MIN_STACK_SIZE})
#define configISR_STACK_SIZE                       (${AWS_CLOUD_FREERTOS_ISR_STACK_SIZE})
#define configSUPPORT_DYNAMIC_ALLOCATION           <#if AWS_CLOUD_FREERTOS_SUPP_DYNAMIC == true>1<#else>0</#if>
#define configSUPPORT_STATIC_ALLOCATION            <#if AWS_CLOUD_FREERTOS_SUPP_STATIC == true>1<#else>0</#if>
#define configTOTAL_HEAP_SIZE                      ( ( size_t ) ${AWS_CLOUD_FREERTOS_HEAP_SIZE})
#define configMAX_TASK_NAME_LEN                    (${AWS_CLOUD_FREERTOS_MAX_TASK_LEN} )
#define configUSE_16_BIT_TICKS                     <#if AWS_CLOUD_FREERTOS_USE_16B_TICKS == true>1<#else>0</#if> 
#define configIDLE_SHOULD_YIELD                    <#if AWS_CLOUD_FREERTOS_IDLE_YIELD == true>1<#else>0</#if> 
#define configUSE_MUTEXES                          <#if AWS_CLOUD_FREERTOS_USE_MUTEX == true>1<#else>0</#if> 
#define configUSE_RECURSIVE_MUTEXES                <#if AWS_CLOUD_FREERTOS_USE_RECURSIVE_MUTEX == true>1<#else>0</#if> 
#define configUSE_COUNTING_SEMAPHORES              <#if AWS_CLOUD_FREERTOS_USE_COUNT_SEMAPHORE == true>1<#else>0</#if> 
#define configUSE_TASK_NOTIFICATIONS               <#if AWS_CLOUD_FREERTOS_USE_TASK_NOTIFY == true>1<#else>0</#if> 
#define configQUEUE_REGISTRY_SIZE                  ${AWS_CLOUD_FREERTOS_QUEUE_REG_SIZE}
#define configUSE_QUEUE_SETS                       <#if AWS_CLOUD_FREERTOS_USE_QUEUE_SETS == true>1<#else>0</#if> 
#define configUSE_TIME_SLICING                     <#if AWS_CLOUD_FREERTOS_USE_TIME_SLICING == true>1<#else>0</#if> 
#define configUSE_NEWLIB_REENTRANT                 <#if AWS_CLOUD_FREERTOS_USE_NEWLIB_REENTRANT == true>1<#else>0</#if> 
#define configENABLE_BACKWARD_COMPATIBILITY        <#if AWS_CLOUD_FREERTOS_ENABLE_BW_COMPATIBILITY == true>1<#else>0</#if> 
#define configUSE_TASK_FPU_SUPPORT                 <#if AWS_CLOUD_FREERTOS_USE_FPU_SUPPORT == true>1<#else>0</#if> 
#define configUSE_POSIX_ERRNO                      <#if AWS_CLOUD_FREERTOS_USE_POSIX_ERR == true>1<#else>0</#if> 

/* Hook function related definitions. */
#define configUSE_IDLE_HOOK                        <#if AWS_CLOUD_FREERTOS_USE_IDLE_HOOK == true>1<#else>0</#if> 
#define configUSE_TICK_HOOK                        <#if AWS_CLOUD_FREERTOS_USE_TICK_HOOK == true>1<#else>0</#if> 
#define configCHECK_FOR_STACK_OVERFLOW             ${AWS_CLOUD_FREERTOS_CHECK_STACK_OVRL_FLOW}
#define configUSE_MALLOC_FAILED_HOOK               <#if AWS_CLOUD_FREERTOS_MALLOC_FAILED_HOOK == true>1<#else>0</#if>

/* Run time and task stats gathering related definitions. */
#define configGENERATE_RUN_TIME_STATS              <#if AWS_CLOUD_FREERTOS_GEN_RUNTIME_STATS == true>1<#else>0</#if> 
#define configUSE_TRACE_FACILITY                   <#if AWS_CLOUD_FREERTOS_USE_TRACE_FACILITY == true>1<#else>0</#if>  

/* Co-routine related definitions. */
#define configUSE_CO_ROUTINES                      <#if AWS_CLOUD_FREERTOS_USE_CO_ROUTINES == true>1<#else>0</#if>
#define configMAX_CO_ROUTINE_PRIORITIES            ${AWS_CLOUD_FREERTOS_USE_CO_ROUTINES_PRI}

/* Software timer related definitions. */
#define configUSE_TIMERS                           <#if AWS_CLOUD_FREERTOS_USE_TIMERS == true>1<#else>0</#if> 
#define configTIMER_TASK_PRIORITY                  ${AWS_CLOUD_FREERTOS_USE_TIMER_TASK_PRIORITY}
#define configTIMER_QUEUE_LENGTH                   ${AWS_CLOUD_FREERTOS_USE_TIMER_QUEUE_LENGTH}
#define configTIMER_TASK_STACK_DEPTH               ${AWS_CLOUD_FREERTOS_TIMER_TASK_STACK_DEPTH}
#define configUSE_DAEMON_TASK_STARTUP_HOOK         <#if AWS_CLOUD_FREERTOS_USE_DAEMON_STARTUP_HOOK == true>1<#else>0</#if> 

/* Misc */
#define configUSE_APPLICATION_TASK_TAG             <#if AWS_CLOUD_FREERTOS_USE_APPLN_TAG == true>1<#else>0</#if>  


/* Interrupt nesting behaviour configuration. */

/* The priority at which the tick interrupt runs.  This should probably be kept at 1. */
#define configKERNEL_INTERRUPT_PRIORITY         1

/* The maximum interrupt priority from which FreeRTOS.org API functions can be called.
 * Only API functions that end in ...FromISR() can be used within interrupts. */
#define configMAX_SYSCALL_INTERRUPT_PRIORITY    5

/* Optional functions - most linkers will remove unused functions anyway. */
#define INCLUDE_vTaskPrioritySet                <#if AWS_CLOUD_FREERTOS_INC_TASK_PRIORITY_SET == true>1<#else>0</#if> 
#define INCLUDE_uxTaskPriorityGet               <#if AWS_CLOUD_FREERTOS_INC_TASK_PRIORITY_GET == true>1<#else>0</#if> 
#define INCLUDE_vTaskDelete                     <#if AWS_CLOUD_FREERTOS_INC_TASK_DELETE == true>1<#else>0</#if> 
#define INCLUDE_vTaskSuspend                    <#if AWS_CLOUD_FREERTOS_INC_TASK_SUSPEND == true>1<#else>0</#if> 
#define INCLUDE_vTaskDelayUntil                 <#if AWS_CLOUD_FREERTOS_INC_TASK_DELAY_UNTIL == true>1<#else>0</#if> 
#define INCLUDE_vTaskDelay                      <#if AWS_CLOUD_FREERTOS_INC_TASK_DELAY == true>1<#else>0</#if> 
#define INCLUDE_xTaskGetSchedulerState          <#if AWS_CLOUD_FREERTOS_INC_TASK_GET_SCHDL_STATE == true>1<#else>0</#if> 
#define INCLUDE_xTaskGetCurrentTaskHandle       <#if AWS_CLOUD_FREERTOS_INC_TASK_CURRENT_HANDLE == true>1<#else>0</#if> 
#define INCLUDE_uxTaskGetStackHighWaterMark     <#if AWS_CLOUD_FREERTOS_INC_TASK_STACK_HWM_GET == true>1<#else>0</#if> 
#define INCLUDE_xTaskGetIdleTaskHandle          <#if AWS_CLOUD_FREERTOS_INC_TASK_IDLE_TASK_HANDLE == true>1<#else>0</#if> 
#define INCLUDE_eTaskGetState                   <#if AWS_CLOUD_FREERTOS_INC_TASK_GET_STATE == true>1<#else>0</#if> 
#define INCLUDE_xEventGroupSetBitFromISR        <#if AWS_CLOUD_FREERTOS_INC_TASK_EVENT_GRP_SET_BIT_ISR == true>1<#else>0</#if> 
#define INCLUDE_xTimerPendFunctionCall          <#if AWS_CLOUD_FREERTOS_INC_TASK_TIMER_PENDING_FN_CALL == true>1<#else>0</#if> 
#define INCLUDE_xTaskAbortDelay                 <#if AWS_CLOUD_FREERTOS_INC_TASK_ABORT_DELAY == true>1<#else>0</#if> 
#define INCLUDE_xTaskGetHandle                  <#if AWS_CLOUD_FREERTOS_INC_TASK_GET_HANDLE == true>1<#else>0</#if> 
#define INCLUDE_xSemaphoreGetMutexHolder        1

/* This demo makes use of one or more example stats formatting functions.  These
 * format the raw data provided by the uxTaskGetSystemState() function in to human
 * readable ASCII form.  See the notes in the implementation of vTaskList() within
 * FreeRTOS/Source/tasks.c for limitations.  configUSE_STATS_FORMATTING_FUNCTIONS
 * is set to 2 so the formatting functions are included without the stdio.h being
 * included in tasks.c.  That is because this project defines its own sprintf()
 * functions. */
#define configUSE_STATS_FORMATTING_FUNCTIONS    ${AWS_CLOUD_FREERTOS_LOGGING_USE_STATS_FORMATTING}

/* Assert call defined for debug builds. */
#if defined( __LANGUAGE_C__ )
    #define configASSERT( x ) \
    if( ( x ) == 0 ) TEST_ABORT()
extern void vLoggingPrint( const char * pcMessage );

/* The function that implements FreeRTOS printf style output, and the macro
 * that maps the configPRINTF() macros to that function. */
    extern void vLoggingPrintf( const char * pcFormat,
                                ... );
    #define configPRINTF( X )          vLoggingPrintf X

/* Map the logging task's printf to the board specific output function. */
    #define configPRINT_STRING( x )    printf( x )


/* Sets the length of the buffers into which logging messages are written - so
 * also defines the maximum length of each log message. */
    #define configLOGGING_MAX_MESSAGE_LENGTH            ${AWS_CLOUD_FREERTOS_LOGGING_MAX_MSG_LEN}

/* Set to 1 to prepend each log message with a message number, the task name,
 * and a time stamp. */
    #define configLOGGING_INCLUDE_TIME_AND_TASK_NAME    <#if AWS_CLOUD_FREERTOS_LOGGING_TASK_TIME == true>1<#else>0</#if> 

#endif /* defined(__LANGUAGE_C__) */

/* Application specific definitions follow. **********************************/

/* If configINCLUDE_DEMO_DEBUG_STATS is set to one, then a few basic IP trace
 * macros are defined to gather some UDP stack statistics that can then be viewed
 * through the CLI interface. */
#define configINCLUDE_DEMO_DEBUG_STATS       <#if AWS_CLOUD_FREERTOS_DEMO_STATS_ENABLE == true>1<#else>0</#if> 

/* The size of the global output buffer that is available for use when there
 * are multiple command interpreters running at once (for example, one on a UART
 * and one on TCP/IP).  This is done to prevent an output buffer being defined by
 * each implementation - which would waste RAM.  In this case, there is only one
 * command interpreter running, and it has its own local output buffer, so the
 * global buffer is just set to be one byte long as it is not used and should not
 * take up unnecessary RAM. */
#define configCOMMAND_INT_MAX_OUTPUT_SIZE    1

/* Only used when running in the FreeRTOS Windows simulator.  Defines the
 * priority of the task used to simulate Ethernet interrupts. */
#define configMAC_ISR_SIMULATOR_PRIORITY     ( configMAX_PRIORITIES - 1 )

/* This demo creates a virtual network connection by accessing the raw Ethernet
 * or WiFi data to and from a real network connection.  Many computers have more
 * than one real network port, and configNETWORK_INTERFACE_TO_USE is used to tell
 * the demo which real port should be used to create the virtual port.  The ports
 * available are displayed on the console when the application is executed.  For
 * example, on my development laptop setting configNETWORK_INTERFACE_TO_USE to 4
 * results in the wired network being used, while setting
 * configNETWORK_INTERFACE_TO_USE to 2 results in the wireless network being
 * used. */
#define configNETWORK_INTERFACE_TO_USE       ${AWS_CLOUD_FREERTOS_NETWORK_INTERFACE_ID}L

/* The address of an echo server that will be used by the two demo echo client
 * tasks.
 * http://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_TCP/TCP_Echo_Clients.html
 * http://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_TCP/UDP_Echo_Clients.html */
#define configECHO_SERVER_ADDR0              192
#define configECHO_SERVER_ADDR1              168
#define configECHO_SERVER_ADDR2              2
#define configECHO_SERVER_ADDR3              6
#define configTCP_ECHO_CLIENT_PORT           7

/* Default MAC address configuration.  The demo creates a virtual network
 * connection that uses this MAC address by accessing the raw Ethernet/WiFi data
 * to and from a real network connection on the host PC.  See the
 * configNETWORK_INTERFACE_TO_USE definition above for information on how to
 * configure the real network connection to use. */

/* PIC32 note: PIC32 processors have a factory programmed MAC address.
 * This address setting will override the factory programmed address.
 * Use all 0's to use the factory programmed address */
#define configMAC_ADDR0           0x00
#define configMAC_ADDR1           0x11
#define configMAC_ADDR2           0x22
#define configMAC_ADDR3           0x33
#define configMAC_ADDR4           0x44
#define configMAC_ADDR5           0x21
    

/* Default IP address configuration.  Used in ipconfigUSE_DHCP is set to 0, or
 * ipconfigUSE_DHCP is set to 1 but a DNS server cannot be contacted. */
#define configIP_ADDR0            192
#define configIP_ADDR1            168
#define configIP_ADDR2            0
#define configIP_ADDR3            105

/* Default gateway IP address configuration.  Used in ipconfigUSE_DHCP is set to
 * 0, or ipconfigUSE_DHCP is set to 1 but a DNS server cannot be contacted. */
#define configGATEWAY_ADDR0       192
#define configGATEWAY_ADDR1       168
#define configGATEWAY_ADDR2       0
#define configGATEWAY_ADDR3       1

/* Default DNS server configuration.  OpenDNS addresses are 208.67.222.222 and
 * 208.67.220.220.  Used in ipconfigUSE_DHCP is set to 0, or ipconfigUSE_DHCP is
 * set to 1 but a DNS server cannot be contacted.*/
#define configDNS_SERVER_ADDR0    208
#define configDNS_SERVER_ADDR1    67
#define configDNS_SERVER_ADDR2    222
#define configDNS_SERVER_ADDR3    222

/* Default netmask configuration.  Used in ipconfigUSE_DHCP is set to 0, or
 * ipconfigUSE_DHCP is set to 1 but a DNS server cannot be contacted. */
#define configNET_MASK0           255
#define configNET_MASK1           255
#define configNET_MASK2           255
#define configNET_MASK3           0

/* The UDP port to which print messages are sent. */
#define configPRINT_PORT          ( 15000 )

#define configPROFILING           ( 0 )

#if defined( __LANGUAGE_C__ )
/* Pseudo random number generater used by some demo tasks. */
    extern uint32_t ulRand();
    #define configRAND32()    ulRand()
#endif /* defined(__LANGUAGE_C__) */

/* The platform FreeRTOS is running on. */
#define configPLATFORM_NAME    "${AWS_CLOUD_FREERTOS_PLAT_NAME}"

#endif /* FREERTOS_CONFIG_H */
