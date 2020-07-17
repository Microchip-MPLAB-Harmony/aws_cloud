/*
 * Copyright (C) 2018 Amazon.com, Inc. or its affiliates.  All Rights Reserved.
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
 */

/* This file contains configuration settings for the demos. */

#ifndef IOT_CONFIG_H_
#define IOT_CONFIG_H_

/* How long the MQTT library will wait for PINGRESPs or PUBACKs. */
#define IOT_MQTT_RESPONSE_WAIT_MS            ( ${AWS_CLOUD_MQTT_RESP} ) 

#define IOT_NETWORK_SOCKET_POLL_MS     ( ${AWS_CLOUD_SOCKET_POLL} ) 

/* MQTT demo configuration. */
#define IOT_DEMO_MQTT_PUBLISH_BURST_COUNT    ( ${AWS_CLOUD_MQTT_BC} )
#define IOT_DEMO_MQTT_PUBLISH_BURST_SIZE     ( ${AWS_CLOUD_MQTT_BS} )

/* Shadow demo configuration. The demo publishes periodic Shadow updates and responds
 * to changing Shadows. */
#define AWS_IOT_DEMO_SHADOW_UPDATE_COUNT        ( ${AWS_CLOUD_SHADOW_UC} )   /* Number of updates to publish. */
#define AWS_IOT_DEMO_SHADOW_UPDATE_PERIOD_MS    ( ${AWS_CLOUD_SHADOW_UPS} ) /* Period of Shadow updates. */

/* Library logging configuration. IOT_LOG_LEVEL_GLOBAL provides a global log
 * level for all libraries; the library-specific settings override the global
 * setting. If both the library-specific and global settings are undefined,
 * no logs will be printed. */
#define IOT_LOG_LEVEL_GLOBAL                    ${AWS_CLOUD_LOG_GLOBAL}
#define IOT_LOG_LEVEL_DEMO                      ${AWS_CLOUD_LOG_DEMO}
#define IOT_LOG_LEVEL_PLATFORM                  ${AWS_CLOUD_LOG_PLATFORM}
#define IOT_LOG_LEVEL_NETWORK                   ${AWS_CLOUD_LOG_NETWORK}
#define IOT_LOG_LEVEL_TASKPOOL                  ${AWS_CLOUD_LOG_TASKPOOL}
#define IOT_LOG_LEVEL_MQTT                      ${AWS_CLOUD_LOG_MQTT}
#define AWS_IOT_LOG_LEVEL_SHADOW                ${AWS_CLOUD_LOG_SHADOW}
#define AWS_IOT_LOG_LEVEL_DEFENDER              ${AWS_CLOUD_LOG_DEFENDER}


/* Platform thread stack size and priority. */
#define IOT_THREAD_DEFAULT_STACK_SIZE    ${AWS_CLOUD_THREAD_STACK_SZ}
#define IOT_THREAD_DEFAULT_PRIORITY      ${AWS_CLOUD_THREAD_PRIORITY}

/* Include the common configuration file for FreeRTOS. */
#include "iot_config_common.h"

#endif /* ifndef IOT_CONFIG_H_ */
