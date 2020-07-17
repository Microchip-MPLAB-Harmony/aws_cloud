/*******************************************************************************
  MPLAB Harmony Application Source File

  Company:
    Microchip Technology Inc.

  File Name:
    app_sensor.c

  Summary:
    This file contains the source code for the MPLAB Harmony application.

  Description:
    This file contains the source code for the MPLAB Harmony application.  It
    implements the logic of the application's state machine and it may call
    API routines of other MPLAB Harmony modules in the system, such as drivers,
    system services, and middleware.  However, it does not call any of the
    system interfaces (such as the "Initialize" and "Tasks" functions) of any of
    the modules in the system or make any assumptions about when those functions
    are called.  That is the responsibility of the configuration-specific system
    files.
 *******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "app_sensor.h"
#include "bme280_definitions.h"
#include "bme280_driver.h"
#include "FreeRTOSConfig.h"
// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************
#define APP_SENSOR_I2C_CLOCK_SPEED             100000
#define APP_SENSOR_I2C_SLAVE_ADDR              0x004B
#define APP_SENSOR_TEMPERATURE_REG_ADDR        0x00
#define APP_SENSOR_SAMPLING_RATE_IN_HZ         1


// *****************************************************************************
/* Application Data

  Summary:
    Holds application data

  Description:
    This structure holds the application's data.

  Remarks:
    This structure should be initialized by the APP_SENSOR_Initialize function.

    Application strings and buffers are be defined outside this structure.
*/

APP_SENSOR_DATA app_sensorData;


volatile BME_SENSOR_DATA BME280SensorData;


// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Functions
// *****************************************************************************
// *****************************************************************************

/******************************************************************************
  Function:
    void APP_SENSOR_I2CEventHandler (
    DRV_I2C_TRANSFER_EVENT event,
    DRV_I2C_TRANSFER_HANDLE transferHandle,
    uintptr_t context
   )

  Remarks:
    This function is registered by the Sensor application client with the I2C
    driver. It is called by the I2C Driver when the requested I2C transfer is
    complete.
 */
void APP_SENSOR_I2CEventHandler(
    DRV_I2C_TRANSFER_EVENT event,
    DRV_I2C_TRANSFER_HANDLE transferHandle,
    uintptr_t context
)
{
    switch(event)
    {
        case DRV_I2C_TRANSFER_EVENT_COMPLETE:
            /* I2C read complete. */
            BME280SensorData.isBufferCompleteEvent = true;
            break;
        case DRV_I2C_TRANSFER_EVENT_ERROR:
            /* Handle error case here.*/
        default:
            break;
    }
}






/******************************************************************************
  Function:
    void APP_SENSOR_TimerEventHandler ( uintptr_t )

  Remarks:
    This function is called by the Timer System Service when the requested time
    period has elapsed.
 */
void APP_SENSOR_TimerEventHandler( uintptr_t context )
{
    /* Timer expired. */

}

/******************************************************************************
  Function:
    void APP_SENSOR_SoftReset_TimerEventHandler ( uintptr_t )

  Remarks:
    This function is called by the Timer System Service when the requested time
    period has elapsed.
 */
void APP_SENSOR_SoftReset_TimerEventHandler( uintptr_t context )
{
    /* Timer expired. */
     app_sensorData.isTimerExpired = true;
}

// *****************************************************************************
// *****************************************************************************
// Section: Application Local Functions
// *****************************************************************************
// *****************************************************************************




// *****************************************************************************
// *****************************************************************************
// Section: Application Initialization and State Machine Functions
// *****************************************************************************
// *****************************************************************************

/*******************************************************************************
  Function:
    void APP_SENSOR_Initialize ( void )

  Remarks:
    See prototype in app_sensor.h.
 */

void APP_SENSOR_Initialize ( void )
{
    /* Place the sensor application state machine in its initial state. */
    app_sensorData.state = APP_SENSOR_STATE_INIT;

}


static bool BME280Sensor_WriteReg(uint8_t wrAddr, uint8_t wrData) 
{    
    BME280SensorData.txBuffer[0]            = wrAddr;
    BME280SensorData.txBuffer[1]            = wrData;
    BME280SensorData.isBufferCompleteEvent  = false;
    
    DRV_I2C_WriteTransferAdd( app_sensorData.i2cHandle,
            BME280SensorData.slaveID, (void*)BME280SensorData.txBuffer, 2, &app_sensorData.transferHandle );

    if (app_sensorData.transferHandle == DRV_I2C_TRANSFER_HANDLE_INVALID)
    {
        /* Handle error condition */
    }
    
    while(false == BME280SensorData.isBufferCompleteEvent);
    
    return true;
}

static uint8_t BME280Sensor_ReadReg(uint8_t rAddr) 
{
    BME280SensorData.txBuffer[0]            = rAddr;
    BME280SensorData.isBufferCompleteEvent  = false;
    
    DRV_I2C_WriteReadTransferAdd( app_sensorData.i2cHandle,
            BME280SensorData.slaveID, (void*)BME280SensorData.txBuffer, 1,
            (void *)BME280SensorData.rxBuffer, 1, &app_sensorData.transferHandle );

    if (app_sensorData.transferHandle == DRV_I2C_TRANSFER_HANDLE_INVALID)
    {
        /* Handle error condition */
    }
    
    while(false == BME280SensorData.isBufferCompleteEvent);
            
    return BME280SensorData.rxBuffer[0];    
}

static bool BME280Sensor_Read(uint8_t rAddr, uint8_t* const pReadBuffer, uint8_t nBytes) 
{
    BME280SensorData.txBuffer[0]            = rAddr;
    BME280SensorData.isBufferCompleteEvent  = false;
    
    DRV_I2C_WriteReadTransferAdd( app_sensorData.i2cHandle,
            BME280SensorData.slaveID, (void*)BME280SensorData.txBuffer, 1,
            (void *)pReadBuffer, nBytes, &app_sensorData.transferHandle );

    if (app_sensorData.transferHandle == DRV_I2C_TRANSFER_HANDLE_INVALID)
    {
        /* Handle error condition */
    }
    
    while(false == BME280SensorData.isBufferCompleteEvent);
            
    return true;
}

void BME280Sensor_Initialize(void)
{
    BME280SensorData.temperature = BME280SensorData.humidity = 0.0;
    BME280SensorData.pressure=0;
    BME280SensorData.slaveID        = BME280_I2C_ADDRESS;
    BME280SensorData.isBufferCompleteEvent = false;
    
    /* Register with BME280 sensor */        
    BME280_RegisterDrvWriteReg(BME280Sensor_WriteReg);
    BME280_RegisterDrvReadReg(BME280Sensor_ReadReg);        
    BME280_RegisterDrvRead(BME280Sensor_Read);

    BME280_SoftReset();
    /* 100 m.sec delay */
    app_sensorData.sysTimeHandle = SYS_TIME_CallbackRegisterMS(APP_SENSOR_SoftReset_TimerEventHandler, 0,
                (100*APP_SENSOR_SAMPLING_RATE_IN_HZ), SYS_TIME_SINGLE);
    while(false == app_sensorData.isTimerExpired);

    if (BME280_CHIP_ID != BME280_ID_Get())
    {
        while(1);       /* Error Occurred */
    }
    BME280_CalibParams_Get();
    BME280_SetOversampling(BME280_PARAM_TEMP, BME280_OVERSAMPLING_1X);
    BME280_PowerMode_Set(BME280_NORMAL_MODE);
}

/******************************************************************************
  Function:
    void APP_SENSOR_Tasks ( void )

  Remarks:
    See prototype in app_sensor.h.
 */

void APP_SENSOR_Tasks ( void )
{
    /* Check the application's current state. */
    switch ( app_sensorData.state )
    {
        /* Application's initial state. */
        case APP_SENSOR_STATE_INIT:

            /* Open I2C Driver to interface with Sensor. */
            app_sensorData.i2cHandle = DRV_I2C_Open( DRV_I2C_INDEX_0, DRV_IO_INTENT_READWRITE );

            if (app_sensorData.i2cHandle != DRV_HANDLE_INVALID)
            {
                app_sensorData.i2cSetup.clockSpeed = APP_SENSOR_I2C_CLOCK_SPEED;

                /* Setup I2C transfer @ 100 kHz to interface with Sensor. */
                DRV_I2C_TransferSetup(app_sensorData.i2cHandle, &app_sensorData.i2cSetup);

                /* Register I2C transfer complete Event Handler for Sensor. */
                DRV_I2C_TransferEventHandlerSet(app_sensorData.i2cHandle, APP_SENSOR_I2CEventHandler, 0);
                        
                        
                BME280Sensor_Initialize();

                /* Register Timer Expiry Event Handler with Timer System Service. */
                SYS_TIME_CallbackRegisterMS(APP_SENSOR_TimerEventHandler, 0,
                        (1000*APP_SENSOR_SAMPLING_RATE_IN_HZ), SYS_TIME_PERIODIC);

                if (app_sensorData.sysTimeHandle != SYS_TIME_HANDLE_INVALID)
                {
                   /* Open USART Driver. */
           app_sensorData.state = APP_SENSOR_STATE_IDLE;
                }
                else
                {
                    /* Handle error condition */
                    app_sensorData.state = APP_SENSOR_STATE_ERROR;
                }
            }
            else
            {
                /* Handle error condition */
                app_sensorData.state = APP_SENSOR_STATE_ERROR;
            }
            break;

        case APP_SENSOR_STATE_READ_TEMPERATURE:
            app_sensorData.i2cTxBuffer[0] = APP_SENSOR_TEMPERATURE_REG_ADDR;

            /* Submit I2C transfer to read temperature sensor value. */

            BME280_ReadRawWeatherData();

            /* The getting temperature is in DegC and resolution is 0.01 DegC. 
             * It means, if the output value is 5123 equals to 51.23 DegC */
            BME280SensorData.temperature   = ((BME280_GetTempReading()));
            BME280SensorData.pressure =  BME280_GetPressReading();
            BME280SensorData.humidity =  BME280_GetHumReading();
            BME280SensorData.temperature  = (BME280SensorData.temperature * 0.01);
            app_sensorData.isTemperatureReadComplete = true;
            configPRINTF( ( "BME280SensorData.temperature pressure humidity %f, %d %f \r\n\r\n", BME280SensorData.temperature,  BME280SensorData.pressure, BME280SensorData.humidity ) );
            /* Go back to the idle state and wait for events */
            //app_sensorData.state = APP_SENSOR_STATE_READ_TEMPERATURE;

            break;

        case APP_SENSOR_STATE_PRINT_TEMPERATURE:
            /* Calculate the temperature from raw value and print on the terminal */

            /* Make sure the USART is ready to write new data */
                /* Celcius to Fahrenheit (°C to °F) Conversion (°F = (°C × 9/5) + 32) */
                app_sensorData.temperature = ((BME280SensorData.temperature * 9 / 5) * 0.01) + 32;

                /* Print the latest read temperature value on the serial terminal */
                printf("Latest Temperature = %d", app_sensorData.temperature);

                /* Notify the EEPROM task to log the temperature value to EEPROM. */


                /* Go back to the idle state and wait for events */
                app_sensorData.state = APP_SENSOR_STATE_IDLE;
            break;

        case APP_SENSOR_STATE_IDLE:
            /* Transition to the appropriate state based on the events */
            if (app_sensorData.isTimerExpired == true)
            {
                /* Periodic timer has expired. Time to read temperature. */
                app_sensorData.isTimerExpired = false;
                app_sensorData.state = APP_SENSOR_STATE_READ_TEMPERATURE;
            }
            else if (app_sensorData.isTemperatureReadComplete == true)
            {
                /* Temperature read successfully. Time to display on serial terminal.*/
                app_sensorData.isTemperatureReadComplete = false;
                app_sensorData.state = APP_SENSOR_STATE_PRINT_TEMPERATURE;
            }

            break;

        case APP_SENSOR_STATE_ERROR:
            /* Handle error conditions here */
            break;

        default:

            break;

    }
}


/*******************************************************************************
 End of File
 */
