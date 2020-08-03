![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

# Microchip MPLAB® Harmony 3 Release Notes
## AWS Cloud Release Notes v3.1.0

### New Features
- Supports ECC608 Integeration with FreeRTOS and Wi-Fi Support (WINC1500/WINC3400) for  SAM D5x/E5x MCUs.
- [Updated version of FreeRTOS 202002.00](https://github.com/MicrochipTech/amazon-freertos/tree/v3.1.0) to add support for following
[SAM S70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-s-mcus),
[SAM E70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus),
[SAM V70/V71](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-v-mcus),
[SAME5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus),
[SAMD5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus),
[PIC32MZ EF](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mz-ef-family) families of 32-bit microcontrollers to securely connect to the AWS Cloud.


- **Development kit and demo application support** - The following table provides number of demo application available for different development kits

	| Development kits                                                                                                                  | Applications |
	| --------------------------------------------------------------------------------------------------------------------------------- | ---          |
	| [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT)      |  1           |
	| [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsame54-xpro)                    |  3           |
	| [Curiosity PIC32MZ EF 2.0 Development Board](https://www.microchip.com/Developmenttools/ProductDetails/DM320209)                  |  1           |


### Known Issues
* Same as 3.0.0

### Development Tools
* [MPLAB® X IDE v5.4](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.41](https://www.microchip.com/mplab/compilers)
* MPLAB® X IDE plug-ins:
    * MPLAB® Harmony Configurator (MHC) v3.4.1 and above.

### Dependent Components
* [CSP v3.7.1](https://github.com/Microchip-MPLAB-Harmony/csp/tree/v3.7.1)
* [CORE v3.7.2](https://github.com/Microchip-MPLAB-Harmony/core/tree/v3.7.2)
* [BSP v3.7.0](https://github.com/Microchip-MPLAB-Harmony/bsp/tree/v3.7.0)
* [DEV_PACKS v3.7.0](https://github.com/Microchip-MPLAB-Harmony/dev_packs/tree/v3.7.0)
* [NET v3.6.1](https://github.com/Microchip-MPLAB-Harmony/net/tree/v3.6.1)
* [Updated version of FreeRTOS 202002.00 for Microchip Products](https://github.com/MicrochipTech/amazon-freertos/tree/v3.1.0)
* [MHC v3.4.1](https://github.com/Microchip-MPLAB-Harmony/mhc/tree/v3.4.1)
* [Cryptoauthlib v3.2.2](https://github.com/MicrochipTech/cryptoauthlib)



# Microchip MPLAB® Harmony 3 Release Notes
## AWS Cloud Release Notes v3.0.0

### New Features
- [Updated version of Amazon FreeRTOS 201908.00](https://github.com/MicrochipTech/amazon-freertos/tree/v3.0.0) to add support for [SAM S70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-s-mcus),
[SAM E70](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus),
[SAM V70/V71](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-v-mcus),
[SAME5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-e-mcus),
[SAMD5x](https://www.microchip.com/design-centers/32-bit/sam-32-bit-mcus/sam-d-mcus),
[PIC32MZ EF](https://www.microchip.com/design-centers/32-bit/pic-32-bit-mcus/pic32mz-ef-family) families of 32-bit microcontrollers to securely connect to the AWS Cloud

- **Development kit and demo application support** - The following table provides number of demo application available for different development kits

	| Development kits                                                                                                                  | Applications |
	| --------------------------------------------------------------------------------------------------------------------------------- | ---          |
	| [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT)      |  1           |
	| [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsame54-xpro)                    |  1           |
	| [Curiosity PIC32MZ EF 2.0 Development Board](https://www.microchip.com/Developmenttools/ProductDetails/DM320209)                  |  1           |


### Known Issues
* PIC32MZ Ethernet MAC driver does not provide configuration option to configure Unicast Hash and Multicast Hash filter. It must be enabled manually by changing the configuration macro to connect to AWS cloud. 

### Development Tools
* [MPLAB® X IDE v5.30](https://www.microchip.com/mplab/mplab-x-ide)
* [MPLAB® XC32 C/C++ Compiler v2.30](https://www.microchip.com/mplab/compilers)
* MPLAB® X IDE plug-ins:
    * MPLAB® Harmony Configurator (MHC) v3.3.5 and above.

### Dependent Components
* [CSP v3.6.0](https://github.com/Microchip-MPLAB-Harmony/csp/tree/v3.6.0)
* [CORE v3.6.0](https://github.com/Microchip-MPLAB-Harmony/core/tree/v3.6.0)
* [BSP v3.6.0](https://github.com/Microchip-MPLAB-Harmony/bsp/tree/v3.6.0)
* [DEV_PACKS v3.6.0](https://github.com/Microchip-MPLAB-Harmony/dev_packs/tree/v3.6.0)
* [NET v3.5.1](https://github.com/Microchip-MPLAB-Harmony/net/tree/v3.5.1)
* [Updated version of Amazon FreeRTOS 201908.00 for Microchip Products](https://github.com/MicrochipTech/amazon-freertos/tree/v3.0.0)
* [MHC v3.3.5](https://github.com/Microchip-MPLAB-Harmony/mhc/tree/v3.3.5)

