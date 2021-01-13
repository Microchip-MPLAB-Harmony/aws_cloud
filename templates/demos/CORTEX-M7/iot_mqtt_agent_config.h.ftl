/*
 * FreeRTOS V1.1.4
 * Copyright (C) 2020 Amazon.com, Inc. or its affiliates.  All Rights Reserved.
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

/**
 * @file iot_mqtt_agent_config.h
 * @brief MQTT agent config options.
 */

#ifndef _AWS_MQTT_AGENT_CONFIG_H_
#define _AWS_MQTT_AGENT_CONFIG_H_

#include "FreeRTOS.h"
#include "task.h"

/**
 * @brief Controls whether or not to report usage metrics to the
 * AWS IoT broker.
 *
 * If mqttconfigENABLE_METRICS is set to 1, a string containing
 * metric information will be included in the "username" field of
 * the MQTT connect messages.
 */
#define mqttconfigENABLE_METRICS    ( <#if AWS_CLOUD_MQTT_ENABLE_METRICS == true>1<#else>0</#if> )

/**
 * @brief The maximum time interval in seconds allowed to elapse between 2 consecutive
 * control packets.
 */
#define mqttconfigKEEP_ALIVE_INTERVAL_SECONDS         ( ${AWS_CLOUD_MQTT_KEEP_ALIVE_INTERVAL} )

/**
 * @brief Defines the frequency at which the client should send Keep Alive messages.
 *
 * Even though the maximum time allowed between 2 consecutive control packets
 * is defined by the mqttconfigKEEP_ALIVE_INTERVAL_SECONDS macro, the user
 * can and should send Keep Alive messages at a slightly faster rate to ensure
 * that the connection is not closed by the server because of network delays.
 * This macro defines the interval of inactivity after which a keep alive messages
 * is sent.
 */
#define mqttconfigKEEP_ALIVE_ACTUAL_INTERVAL_TICKS    ( pdMS_TO_TICKS( ${AWS_CLOUD_MQTT_KEEP_ALIVE_INTERVAL_TICKS} ) )

/**
 * @brief The maximum interval in ticks to wait for PINGRESP.
 *
 * If PINGRESP is not received within this much time after sending PINGREQ,
 * the client assumes that the PINGREQ timed out.
 */
#define mqttconfigKEEP_ALIVE_TIMEOUT_TICKS            ( ${AWS_CLOUD_MQTT_KEEP_ALIVE_TIMEOUT} )

/**
 * @brief The maximum time in ticks for which the MQTT task is permitted to block.
 *
 * The MQTT task blocks until the user initiates any action or until it receives
 * any data from the broker. This macro controls the maximum time the MQTT task can
 * block. It should be set to a low number for the platforms which do not have any
 * mechanism to wake up the MQTT task whenever data is received on a connected socket.
 * This ensures that the MQTT task keeps waking up frequently and processes the
 * publish messages received from the broker, if any.
 */
#define mqttconfigMQTT_TASK_MAX_BLOCK_TICKS           ( ${AWS_CLOUD_MQTT_TASK_BLOCK_TICKS} )

/**
 * @defgroup MQTTTask MQTT task configuration parameters.
 */
/** @{ */
#define mqttconfigMQTT_TASK_STACK_DEPTH    ( ${AWS_CLOUD_MQTT_TASK_STACK} )
#define mqttconfigMQTT_TASK_PRIORITY       ( tskIDLE_PRIORITY + ${AWS_CLOUD_MQTT_TASK_PRI} )
/** @} */

/**
 * @brief Maximum number of MQTT clients that can exist simultaneously.
 */
#define mqttconfigMAX_BROKERS            ( ${AWS_CLOUD_MQTT_MAX_BROKERS} )

/**
 * @brief Maximum number of parallel operations per client.
 */
#define mqttconfigMAX_PARALLEL_OPS       ( ${AWS_CLOUD_MQTT_PARALLEL_OPS} )

/**
 * @brief Time in milliseconds after which the TCP send operation should timeout.
 */
#define mqttconfigTCP_SEND_TIMEOUT_MS    ( ${AWS_CLOUD_MQTT_TCP_TIMEOUT} )

/**
 * @brief Length of the buffer used to receive data.
 */
#define mqttconfigRX_BUFFER_SIZE               ( 1024 + 128 )

/**
 * @brief The maximum time in ticks for which the MQTT task is permitted to block.
 */
#define mqttconfigMQTT_TASK_MAX_BLOCK_TICKS    ( ~( ( uint32_t ) 0 ) )

#endif /* _AWS_MQTT_AGENT_CONFIG_H_ */
