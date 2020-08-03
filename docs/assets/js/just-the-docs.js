var myVariable = `
{
  
  "0": {
    "title": "LED Shadow Client Application",
    "content": ". LED Shadow Client Application . This example application shows how to use the shadow client feature to set/get Device status using LED(s). The device turns LED ON/OFF once to indicate the Shadow state is ready following which the user may turn LED(s) ON/OFF from AWS console. The application uses ECC608 for key storage and authentication. . Development Kits . The following table provides links to documentation on how to build and run LED Shadow Client Application on different development kits . Development Kit . PIC32MZEF Curisoity Board 2.0 | . SAM E70 Xplained Ultra Evaluation Kit | . SAM E54 Xplained Pro Evaluation Kit | . SAM E54 Xplained Pro Evaluation Kit + WINC1500 | . SAM E54 Xplained Pro Evaluation Kit + WINC3400 | .",
    "url": "http://localhost:4000/aws_cloud/apps/led_shadow_client_ecc/readme.html",
    "relUrl": "/apps/led_shadow_client_ecc/readme.html"
  }
  ,"1": {
    "title": "Building and Running on PIC32MZ EF Curiosity 2.0 board.",
    "content": ". Building and Running on PIC32MZEF Curiosity 2.0 (Wired) . Downloading and building the application . To clone or download this application from Github,go to the main page of this repository and then click Clone button to clone this repo or download as zip file. This content can also be download using content manager by following these instructions . Path of the application within the repository is apps/led_shadow_client_ecc/ . To build the application, refer to the following table and open the project using its IDE. . LED Shadow Client Demo Application . Project Name Description . firmware/pic32mz_ef_curiosity_v2.X | MPLABX Project for PIC32MZEF Curiosity 2.0 board | . Provisoning the device for AWS account access. . Refer to Getting Started guide for setting up the AWS account based on your hardware configuration. | With the completion of the above steps, the user would have got aws_clientcredential.h and aws_clientcredentialkeys.h, this may be used for running the demos. | . Setting up PIC32MZEF Curiosity 2.0 board . Connect the Debug USB port on the board to the computer using a micro USB cable | Connect the ATECC608A Trust on the mikroBUS Xplained Pro adapter in EXT2. | Connect the LAN8720PHY daughter card in the PHY slot. | . Building the Application . Open the application project firmware/pic32mz_ef_curiosity_v2.X in the IDE | Use the aws_clientcredential.h and aws_clientcredentialkeys.h obtained from provisoning the device to aws account. | Build and program the application using the IDE | Running the Application . Connect an ethernet cable from an internet router to the PHY slot in PIC32MZEF Curiosity 2.0 board. | If above step is successful then the LED0 on the board would turn ON/OFF once. | Open the Terminal application (Ex.:Tera Term) on the computer | Configure the serial port settings as follows: Baud : 115200 | Data : 8 Bits | Parity : None | Stop : 1 Bit | Flow Control : None | . | Login to your AWS amazon account From the Services menu (upper left), click (or search for) IoT Core and open it. This will open the Aws IoT page as shown below. | . From the menu on the left, Click “Manage” and then Click “Things”. This will display all the things managed by your AWS account in the right pane. In the right pane, click the “Things” item, which represents your device. . | The THING Name and Shadow ARN are masked for security reasons. Click on the “Shadow” item in the right pane. This will display the device shadow page. . | Build and Program the application using the MPLAB X IDE. The device will toggle one LED and now a shadow document will be created in the Device’s Shadow page. The Shadow state document is JSON formatted file representing the device’s state, in this example the LED status is depicated as device’s status. . | The JSON variable “powerOn” indicates the LED state of the board and Shadow state depicts the current state of the device. . | The user can modify the Shadow state till the connection is alive by click on the Edit button in the Shadow Document and changing the “powerOn” state. . | Change the power On value to ‘1’ and click on the Save Button, this will turn LED0 “ON”. Changing the value to 0 will turn LED0 off. Similarly it follows below truth table. . | S.No LED2 LED1 LED0 powerOn (Value) Remarks . 1 | OFF | OFF | OFF | 0 | All LED off. | . 2. | OFF | OFF | ON | 1 | LED0 On. | . 3. | OFF | ON | OFF | 2 | LED1 On. | . 4. | OFF | ON | ON | 3 | LED0 and LED1 On. | . 5 | ON | OFF | OFF | 4 | LED2 ON. | . 6. | ON | OFF | ON | 5 | LED0 and LED2 ON | . 7 | ON | ON | OFF | 6 | LED1 and LED2 ON | . 8 | ON | ON | ON | 7 | LED 0, LED 1 and LED 2 ON. | .",
    "url": "http://localhost:4000/aws_cloud/apps/led_shadow_client_ecc/docs/readme_pic32mzef_curiosity2.html",
    "relUrl": "/apps/led_shadow_client_ecc/docs/readme_pic32mzef_curiosity2.html"
  }
  ,"2": {
    "title": "Building and Running on SAM E54 Xplained Pro Evaluation Kit",
    "content": ". Building and Running on SAM E54 Xplained Pro Evaluation Kit (Wired) . Downloading and building the application . To clone or download this application from Github,go to the main page of this repository and then click Clone button to clone this repo or download as zip file. This content can also be download using content manager by following these instructions . Path of the application within the repository is apps/led_shadow_client_ecc/ . To build the application, refer to the following table and open the project using its IDE. . LED Shadow Client Demo Application . Project Name Description . firmware/sam_e54_xpro.X | MPLABX Project for SAM E54 Xplained Pro Evaluation Kit | . Provisoning the device for AWS account access. . Refer to Getting Started guide for setting up the AWS account based on your hardware configuration. | With the completion of the above steps, the user would have got aws_clientcredential.h and aws_clientcredentialkeys.h, this may be used for running the demos. | . Setting up SAM E54 Xplained Pro Evaluation Kit . Connect the Debug USB port on the board to the computer using a micro USB cable | Connect the ATECC608A Trust on the mikroBUS Xplained Pro adapter in EXT2. | Connect the IO1 Xplained Pro in EXT3. | . Building the Application . Open the application project firmware/sam_e54_xpro.X in the IDE | Use the aws_clientcredential.h and aws_clientcredentialkeys.h obtained from provisoning the device to aws account. | Build and program the application using the IDE | Running the Application . Connect an ethernet cable from an internet router to the PHY in SAME54 Xplained Pro. | If above step is successful then the LED0 on IO1 Xplained would turn ON/OFF once. | Open the Terminal application (Ex.:Tera Term) on the computer | Configure the serial port settings as follows: Baud : 115200 | Data : 8 Bits | Parity : None | Stop : 1 Bit | Flow Control : None | . | Login to your AWS amazon account From the Services menu (upper left), click (or search for) IoT Core and open it. This will open the Aws IoT page as shown below. | . From the menu on the left, Click “Manage” and then Click “Things”. This will display all the things managed by your AWS account in the right pane. In the right pane, click the “Things” item, which represents your device. | . The THING Name and Shadow ARN are masked for security reasons. Click on the “Shadow” item in the right pane. This will display the device shadow page. | Build and Program the application using the MPLAB X IDE. The device will toggle one LED and now a shadow document will be created in the Device’s Shadow page. The Shadow state document is JSON formatted file representing the device’s state, in this example the LED status is depicated as device’s status. | The JSON variable “powerOn” indicates the LED state of the board and Shadow state depicts the current state of the device. | The user can modify the Shadow state till the connection is alive by click on the Edit button in the Shadow Document and changing the “powerOn” state. | Change the power On value to ‘1’ and click on the Save Button, this will turn LED on the EXT3, Changing the value to 0 will turn LED off. |",
    "url": "http://localhost:4000/aws_cloud/apps/led_shadow_client_ecc/docs/readme_sam_e54_xpro.html",
    "relUrl": "/apps/led_shadow_client_ecc/docs/readme_sam_e54_xpro.html"
  }
  ,"3": {
    "title": "Building and Running on SAM E54 Xplained Pro Evaluation Kit + WINC1500",
    "content": ". Building and Running on SAM E54 Xplained Pro Evaluation Kit + WINC1500 . Downloading and building the application . To clone or download this application from Github,go to the main page of this repository and then click Clone button to clone this repo or download as zip file. This content can also be download using content manager by following these instructions . Path of the application within the repository is apps/led_shadow_client_ecc/ . To build the application, refer to the following table and open the project using its IDE. . LED Shadow Client Demo Application . Project Name Description . firmware/sam_e54_xpro_winc1500.X | MPLABX Project for SAM E54 Xplained Pro Evaluation Kit | . Provisoning the device for AWS account access. . Refer to Getting Started guide for setting up the AWS account based on your hardware configuration. | With the completion of the above steps, the user would have got aws_clientcredential.h and aws_clientcredentialkeys.h, this may be used for running the demos. | . Setting up SAM E54 Xplained Pro Evaluation Kit . Connect the Debug USB port on the board to the computer using a micro USB cable | Connect the ATECC608A Trust on the mikroBUS Xplained Pro adapter in EXT2. | Connect the IO1 Xplained Pro in EXT3. | Connect the WINC1500 Xplained Pro in EXT1 | . Building the Application . Open the application project firmware/sam_e54_xpro_winc1500.X in the IDE | Use the aws_clientcredential.h and aws_clientcredentialkeys.h obtained from provisoning the device to aws account. | Build and program the application using the IDE | Running the Application . Ensure Wifi router is connected to internet before turning on the board. | If above step is successful then the LED0 on IO1 Xplained would turn ON/OFF once. | Open the Terminal application (Ex.:Tera Term) on the computer | Configure the serial port settings as follows: Baud : 115200 | Data : 8 Bits | Parity : None | Stop : 1 Bit | Flow Control : None | . | Login to your AWS amazon account From the Services menu (upper left), click (or search for) IoT Core and open it. This will open the Aws IoT page as shown below. | From the menu on the left, Click “Manage” and then Click “Things”. This will display all the things managed by your AWS account in the right pane. In the right pane, click the “Things” item, which represents your device. | The THING Name and Shadow ARN are masked for security reasons. Click on the “Shadow” item in the right pane. This will display the device shadow page. | Build and Program the application using the MPLAB X IDE. The device will toggle one LED and now a shadow document will be created in the Device’s Shadow page. The Shadow state document is JSON formatted file representing the device’s state, in this example the LED status is depicated as device’s status. | The JSON variable “powerOn” indicates the LED state of the board and Shadow state depicts the current state of the device. | The user can modify the Shadow state till the connection is alive by click on the Edit button in the Shadow Document and changing the “powerOn” state. . | Change the power On value to ‘1’ and click on the Save Button, this will turn LED on the EXT3, Changing the value to 0 will turn LED off. |",
    "url": "http://localhost:4000/aws_cloud/apps/led_shadow_client_ecc/docs/readme_sam_e54_xpro_winc1500.html",
    "relUrl": "/apps/led_shadow_client_ecc/docs/readme_sam_e54_xpro_winc1500.html"
  }
  ,"4": {
    "title": "Building and Running on SAM E54 Xplained Pro Evaluation Kit + WINC3400",
    "content": ". Building and Running on SAM E54 Xplained Pro Evaluation Kit + WINC3400 . Downloading and building the application . To clone or download this application from Github,go to the main page of this repository and then click Clone button to clone this repo or download as zip file. This content can also be download using content manager by following these instructions . Path of the application within the repository is apps/led_shadow_client_ecc/ . To build the application, refer to the following table and open the project using its IDE. . LED Shadow Client Demo Application . Project Name Description . firmware/sam_e54_xpro_winc3400.X | MPLABX Project for SAM E54 Xplained Pro Evaluation Kit | . Provisoning the device for AWS account access. . Refer to Getting Started guide for setting up the AWS account based on your hardware configuration. | With the completion of the above steps, the user would have got aws_clientcredential.h and aws_clientcredentialkeys.h, this may be used for running the demos. | . Setting up SAM E54 Xplained Pro Evaluation Kit . Connect the Debug USB port on the board to the computer using a micro USB cable | Connect the ATECC608A Trust on the mikroBUS Xplained Pro adapter in EXT2. | Connect the IO1 Xplained Pro in EXT3. | Connect the WINC3400 Xplained Pro in EXT1 | . Building the Application . Open the application project firmware/sam_e54_xpro_winc3400.X in the IDE | Use the aws_clientcredential.h and aws_clientcredentialkeys.h obtained from provisoning the device to aws account. | Build and program the application using the IDE | Running the Application . Ensure Wifi router is connected to internet before turning on the board. | If above step is successful then the LED0 on IO1 Xplained would turn ON/OFF once. | Open the Terminal application (Ex.:Tera Term) on the computer | Configure the serial port settings as follows: Baud : 115200 | Data : 8 Bits | Parity : None | Stop : 1 Bit | Flow Control : None | . | Login to your AWS amazon account From the Services menu (upper left), click (or search for) IoT Core and open it. This will open the Aws IoT page as shown below. | From the menu on the left, Click “Manage” and then Click “Things”. This will display all the things managed by your AWS account in the right pane. In the right pane, click the “Things” item, which represents your device. | The THING Name and Shadow ARN are masked for security reasons. Click on the “Shadow” item in the right pane. This will display the device shadow page. | Build and Program the application using the MPLAB X IDE. The device will toggle one LED and now a shadow document will be created in the Device’s Shadow page. The Shadow state document is JSON formatted file representing the device’s state, in this example the LED status is depicated as device’s status. | The JSON variable “powerOn” indicates the LED state of the board and Shadow state depicts the current state of the device. | The user can modify the Shadow state till the connection is alive by click on the Edit button in the Shadow Document and changing the “powerOn” state. | Change the power On value to ‘1’ and click on the Save Button, this will turn LED on the EXT3, Changing the value to 0 will turn LED off. |",
    "url": "http://localhost:4000/aws_cloud/apps/led_shadow_client_ecc/docs/readme_sam_e54_xpro_winc3400.html",
    "relUrl": "/apps/led_shadow_client_ecc/docs/readme_sam_e54_xpro_winc3400.html"
  }
  ,"5": {
    "title": "Building and Running on SAM E70 Xplained Ultra",
    "content": ". Building and Running on SAM E70 Xplained Ultra (Wired) . Downloading and building the application . To clone or download this application from Github,go to the main page of this repository and then click Clone button to clone this repo or download as zip file. This content can also be download using content manager by following these instructions . Path of the application within the repository is apps/led_shadow_client_ecc/ . To build the application, refer to the following table and open the project using its IDE. . LED Shadow Client Demo Application . Project Name Description . firmware/sam_e70_xult.X | MPLABX Project for SAM E70 Xplained Ultra | . Provisoning the device for AWS account access. . Refer to Getting Started guide for setting up the AWS account based on your hardware configuration. | With the completion of the above steps, the user would have got aws_clientcredential.h and aws_clientcredentialkeys.h, this may be used for running the demos. | . Setting up SAM E70 Xplained Pro Ultra . Connect the Debug USB port on the board to the computer using a micro USB cable | Connect the ATECC608A Trust on the mikroBUS Xplained Pro adapter in EXT2. | Connect the LAN8720PHY daughter card in the PHY slot. | . Building the Application . Open the application project firmware/sam_e70_xult.X in the IDE | Use the aws_clientcredential.h and aws_clientcredentialkeys.h obtained from provisoning the device to aws account. | Build and program the application using the IDE | Running the Application . Connect an ethernet cable from an internet router to the PHY slot in SAME70 Xplained Ultra. | If above step is successful then the LED0 on the board would turn ON/OFF once. | Open the Terminal application (Ex.:Tera Term) on the computer | Configure the serial port settings as follows: Baud : 115200 | Data : 8 Bits | Parity : None | Stop : 1 Bit | Flow Control : None | . | Login to your AWS amazon account From the Services menu (upper left), click (or search for) IoT Core and open it. This will open the Aws IoT page as shown below. | . From the menu on the left, Click “Manage” and then Click “Things”. This will display all the things managed by your AWS account in the right pane. In the right pane, click the “Things” item, which represents your device. | . The THING Name and Shadow ARN are masked for security reasons. Click on the “Shadow” item in the right pane. This will display the device shadow page. | Build and Program the application using the MPLAB X IDE. The device will toggle one LED and now a shadow document will be created in the Device’s Shadow page. The Shadow state document is JSON formatted file representing the device’s state, in this example the LED status is depicated as device’s status. | The JSON variable “powerOn” indicates the LED state of the board and Shadow state depicts the current state of the device. | The user can modify the Shadow state till the connection is alive by click on the Edit button in the Shadow Document and changing the “powerOn” state. | Change the power On value to ‘1’ and click on the Save Button, this will turn LED0 “ON”. Changing the value to 0 will turn LED0 off. Similarly it follows below truth table. | S.No LED1 LED0 powerOn (Value) Remarks . 1 | OFF | OFF | 0 | All LED off. | . 2. | OFF | ON | 1 | LED0 On. | . 3. | ON | OFF | 2 | LED1 On | . 4. | ON | ON | 3 | LED1 and LED0 On | .",
    "url": "http://localhost:4000/aws_cloud/apps/led_shadow_client_ecc/docs/readme_sam_e70_xult.html",
    "relUrl": "/apps/led_shadow_client_ecc/docs/readme_sam_e70_xult.html"
  }
  ,"6": {
    "title": "",
    "content": "IMPORTANT: READ CAREFULLY . MICROCHIP IS WILLING TO LICENSE THIS INTEGRATED SOFTWARE FRAMEWORK SOFTWARE AND ACCOMPANYING DOCUMENTATION OFFERED TO YOU ONLY ON THE CONDITION THAT YOU ACCEPT ALL OF THE FOLLOWING TERMS. TO ACCEPT THE TERMS OF THIS LICENSE, CLICK “I ACCEPT” AND PROCEED WITH THE DOWNLOAD OR INSTALL. IF YOU DO NOT ACCEPT THESE LICENSE TERMS, CLICK “I DO NOT ACCEPT,” AND DO NOT DOWNLOAD OR INSTALL THIS SOFTWARE. . NON-EXCLUSIVE SOFTWARE LICENSE AGREEMENT FOR MICROCHIP MPLAB HARMONY INTEGRATED SOFTWARE FRAMEWORK . This Nonexclusive Software License Agreement (“Agreement”) is between you, your heirs, agents, successors and assigns (“Licensee”) and Microchip Technology Incorporated, a Delaware corporation, with a principal place of business at 2355 W. Chandler Blvd., Chandler, AZ 85224-6199, and its subsidiary, Microchip Technology (Barbados) II Incorporated (collectively, “Microchip”) for Microchip’s MPLAB Harmony Integrated Software Framework (“Software”) and accompanying documentation (“Documentation”). The Software and Documentation are licensed under this Agreement and not sold. U.S. copyright laws and international copyright treaties, and other intellectual property laws and treaties protect the Software and Documentation. Microchip reserves all rights not expressly granted to Licensee in this Agreement. . License and Sublicense Grant. . (a) Definitions. As used this Agreement, the following terms shall have the meanings defined below: . (i) &quot;Licensee Products&quot; means Licensee products that use or incorporate Microchip Products. (ii) &quot;Microchip Product&quot; means Microchip 16-bit and 32-bit microcontrollers, digital signal controllers or other Microchip semiconductor products with PIC16 and PIC18 prefix and specifically excepting the CX870 and CY920, which are not covered under this Agreement, that use or implement the Software. (iii) &quot;Object Code&quot; means the Software computer programming code provided by Microchip that is in binary form (including related documentation, if any) and error corrections, improvements and updates to such code provided by Microchip in its sole discretion, if any. (iv) &quot;Source Code&quot; means the Software computer programming code provided by Microchip that may be printed out or displayed in human readable form (including related programmer comments and documentation, if any), and error corrections, improvements, updates, modifications and derivatives of such code developed by Microchip, Licensee or Third Party. (v) &quot;Third Party&quot; means Licensee&#39;s agents, representatives, consultants, clients, customers, or contract manufacturers. (vi) &quot;Third Party Products&quot; means Third Party products that use or incorporate Microchip Products. . (b) Software License Grant. Subject to the terms of this Agreement, Microchip grants strictly to Licensee a personal, worldwide, non-exclusive, non-transferable limited license to use, modify (except as limited by Section 1(f) below), copy and distribute the Software only when the Software is embedded on a Microchip Product that is integrated into Licensee Product or Third Party Product pursuant to Section 2(d) below. . Any portion of the Software (including derivatives or modifications thereof) may not be: . (i) embedded on a non-Microchip microcontroller or digital signal controller; (ii) distributed (in Source Code or Object Code), except as described in Section 2(d) below. . (c) Documentation License Grant. Subject to all of the terms and conditions of this Agreement, Microchip grants strictly to Licensee a perpetual, worldwide, non-exclusive license to use the Documentation in support of Licensee’s use of the Software. . (d) Sublicense Grants. Subject to terms of this Agreement, Licensee may grant a limited sublicense to a Third Party to use the Software as described below only if such Third Party expressly agrees to be bound by terms of confidentiality and limited use that are no broader in scope and duration than the confidentiality and limited use terms of this Agreement: . (i) Third Party may modify Source Code for Licensee, except as limited by Section 1(f) below. (ii) Third Party may program Software into Microchip Products for Licensee. (iii) Third Party may use Software to develop and/or manufacture Licensee Product. (iv) Third Party may use Software to develop and/or manufacture Third Party Products where either: (x) the sublicensed Software contains Source Code modified or otherwise optimized by Licensee for Third Party use; or (y) the sublicensed Software is programmed into Microchip Products by Licensee on behalf of such Third Party. (v) Third Party may use the Documentation in support of Third Party&#39;s authorized use of the Software in conformance with this Section 2(d). . (e) Audit. Authorized representatives of Microchip shall have the right to reasonably inspect Licensee’s premises and to audit Licensee’s records and inventory of Licensee Products, whether located on Licensee’s premises or elsewhere at any time, announced or unannounced, and in its sole and absolute discretion, in order to ensure Licensee’s adherence to the terms of this Agreement. . (f) License and Sublicense Limitation. This Section 1 does not grant Licensee or any Third Party the right to modify any dotstack™ Bluetooth® stack, profile, or iAP protocol included in the Software. . | Third Party Requirements. Licensee acknowledges that it is Licensee’s responsibility to comply with any third party license terms or requirements applicable to the use of such third party software, specifications, systems, or tools, including but not limited to SEGGER Microcontroller GmbH &amp; Co. KG’s rights in the emWin software and certain libraries included herein. Microchip is not responsible and will not be held responsible in any manner for Licensee’s failure to comply with such applicable terms or requirements. . | Open Source Components. Notwithstanding the license grants contained herein, Licensee acknowledges that certain components of the Software may be covered by so-called “open source” software licenses (“Open Source Components”). Open Source Components means any software licenses approved as open source licenses by the Open Source Initiative or any substantially similar licenses, including any license that, as a condition of distribution, requires Microchip to provide Licensee with certain notices and/or information related to such Open Source Components, or requires that the distributor make the software available in source code format. Microchip will use commercially reasonable efforts to identify such Open Source Components in a text file or “About Box” or in a file or files referenced thereby (and will include any associated license agreement, notices, and other related information therein), or the Open Source Components will contain or be accompanied by its own license agreement. To the extent required by the licenses covering Open Source Components, the terms of such licenses will apply in lieu of the terms of this Agreement, and Microchip hereby represents and warrants that the licenses granted to such Open Source Components will be no less broad than the license granted in Section 1(b). To the extent the terms of the licenses applicable to Open Source Components prohibit any of the restrictions in this Agreement with respect to such Open Source Components, such restrictions will not apply to such Open Source Components. . | Licensee’s Obligations. . (a) Licensee will ensure Third Party compliance with the terms of this Agreement. . (b) Licensee will not: (i) engage in unauthorized use, modification, disclosure or distribution of Software or Documentation, or its derivatives; (ii) use all or any portion of the Software, Documentation, or its derivatives except in conjunction with Microchip Products; or (iii) reverse engineer (by disassembly, decompilation or otherwise) Software or any portion thereof; or (iv) copy or reproduce all or any portion of Software, except as specifically allowed by this Agreement or expressly permitted by applicable law notwithstanding the foregoing limitations. . (c) Licensee must include Microchip’s copyright, trademark and other proprietary notices in all copies of the Software, Documentation, and its derivatives. Licensee may not remove or alter any Microchip copyright or other proprietary rights notice posted in any portion of the Software or Documentation. . (d) Licensee will defend, indemnify and hold Microchip and its subsidiaries harmless from and against any and all claims, costs, damages, expenses (including reasonable attorney’s fees), liabilities, and losses, including without limitation product liability claims, directly or indirectly arising from or related to: (i) the use, modification, disclosure or distribution of the Software, Documentation or any intellectual property rights related thereto; (ii) the use, sale, and distribution of Licensee Products or Third Party Products, and (iii) breach of this Agreement. THE FOREGOING STATES THE SOLE AND EXCLUSIVE LIABILITY OF THE PARTIES FOR INTELLECTUAL PROPERTY RIGHTS INFRINGEMENT. . | Confidentiality. . (a) Licensee agrees that the Software (including but not limited to the Source Code, Object Code and library files) and its derivatives, Documentation and underlying inventions, algorithms, know-how and ideas relating to the Software and the Documentation are proprietary information belonging to Microchip and its licensors (“Proprietary Information”). Except as expressly and unambiguously allowed herein, Licensee will hold in confidence and not use or disclose any Proprietary Information and shall similarly bind its employees and Third Party(ies) in writing. Proprietary Information shall not include information that: (i) is in or enters the public domain without breach of this Agreement and through no fault of the receiving party; (ii) the receiving party was legally in possession of prior to receiving it; (iii) the receiving party can demonstrate was developed by it independently and without use of or reference to the disclosing party’s Proprietary Information; or (iv) the receiving party receives from a third party without restriction on disclosure. If Licensee is required to disclose Proprietary Information by law, court order, or government agency, such disclosure shall not be deemed a breach of this Agreement provided that Licensee gives Microchip prompt notice of such requirement in order to allow Microchip to object or limit such disclosure, Licensee cooperates with Microchip to protect Proprietary Information, and Licensee complies with any protective order in place and discloses only the information required by process of law. . (b) Licensee agrees that the provisions of this Agreement regarding unauthorized use and nondisclosure of the Software, Documentation and related Proprietary Rights are necessary to protect the legitimate business interests of Microchip and its licensors and that monetary damages alone cannot adequately compensate Microchip or its licensors if such provisions are violated. Licensee, therefore, agrees that if Microchip alleges that Licensee or Third Party has breached or violated such provision then Microchip will have the right to petition for injunctive relief, without the requirement for the posting of a bond, in addition to all other remedies at law or in equity. . | Ownership of Proprietary Rights. . (a) Microchip and its licensors retain all right, title and interest in and to the Software and Documentation (“Proprietary Rights”) including, but not limited to: (i) patent, copyright, trade secret and other intellectual property rights in the Software, Documentation, and underlying technology; (ii) the Software as implemented in any device or system, all hardware and software implementations of the Software technology (expressly excluding Licensee and Third Party code developed and used in conformance with this Agreement solely to interface with the Software and Licensee Products and/or Third Party Products); and (iii) all modifications and derivative works thereof (by whomever produced). Further, modifications and derivative works shall be considered works made for hire with ownership vesting in Microchip on creation. To the extent such modifications and derivatives do not qualify as a “work for hire,” Licensee hereby irrevocably transfers, assigns and conveys the exclusive copyright thereof to Microchip, free and clear of any and all liens, claims or other encumbrances, to the fullest extent permitted by law. Licensee and Third Party use of such modifications and derivatives is limited to the license rights described in Section 1 above. . (b) Licensee shall have no right to sell, assign or otherwise transfer all or any portion of the Software, Documentation or any related intellectual property rights except as expressly set forth in this Agreement. . | Termination of Agreement. Without prejudice to any other rights, this Agreement terminates immediately, without notice by Microchip, upon a failure by License or Third Party to comply with any provision of this Agreement. Further, Microchip may also terminate this Agreement upon reasonable belief that Licensee or Third Party have failed to comply with this Agreement. Upon termination, Licensee and Third Party will immediately stop using the Software, Documentation, and derivatives thereof, and immediately destroy all such copies, remove Software from any of Licensee’s tangible media and from systems on which the Software exists, and stop using, disclosing, copying, or reproducing Software (even as may be permitted by this Agreement). Termination of this Agreement will not affect the right of any end user or consumer to use Licensee Products or Third Party Products provided that such products were purchased prior to the termination of this Agreement. . | Dangerous Applications. The Software is not fault-tolerant and is not designed, manufactured, or intended for use in hazardous environments requiring failsafe performance (“Dangerous Applications”). Dangerous Applications include the operation of nuclear facilities, aircraft navigation, aircraft communication systems, air traffic control, direct life support machines, weapons systems, or any environment or system in which the failure of the Software could lead directly or indirectly to death, personal injury, or severe physical or environmental damage. Microchip specifically disclaims (a) any express or implied warranty of fitness for use of the Software in Dangerous Applications; and (b) any and all liability for loss, damages and claims resulting from the use of the Software in Dangerous Applications. . | Warranties and Disclaimers. THE SOFTWARE AND DOCUMENTATION ARE PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE. MICROCHIP AND ITS LICENSORS ASSUME NO RESPONSIBILITY FOR THE ACCURACY, RELIABILITY OR APPLICATION OF THE SOFTWARE OR DOCUMENTATION. MICROCHIP AND ITS LICENSORS DO NOT WARRANT THAT THE SOFTWARE WILL MEET REQUIREMENTS OF LICENSEE OR THIRD PARTY, BE UNINTERRUPTED OR ERROR-FREE. MICROCHIP AND ITS LICENSORS HAVE NO OBLIGATION TO CORRECT ANY DEFECTS IN THE SOFTWARE. LICENSEE AND THIRD PARTY ASSUME THE ENTIRE RISK ARISING OUT OF USE OR PERFORMANCE OF THE SOFTWARE AND DOCUMENTATION PROVIDED UNDER THIS AGREEMENT. . | Limited Liability. IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR OTHER LEGAL OR EQUITABLE THEORY FOR ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES INCLUDING BUT NOT LIMITED TO INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES (INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS. The aggregate and cumulative liability of Microchip and its licensors for damages hereunder will in no event exceed $1000 or the amount Licensee paid Microchip for the Software and Documentation, whichever is greater. Licensee acknowledges that the foregoing limitations are reasonable and an essential part of this Agreement. . | General. . (a) Governing Law, Venue and Waiver of Trial by Jury. THIS AGREEMENT SHALL BE GOVERNED BY AND CONSTRUED UNDER THE LAWS OF THE STATE OF ARIZONA AND THE UNITED STATES WITHOUT REGARD TO CONFLICTS OF LAWS PROVISIONS. Licensee agrees that any disputes arising out of or related to this Agreement, Software or Documentation shall be brought in the courts of State of Arizona. The parties agree to waive their rights to a jury trial in actions relating to this Agreement. . (b) Attorneys’ Fees. If either Microchip or Licensee employs attorneys to enforce any rights arising out of or relating to this Agreement, the prevailing party shall be entitled to recover its reasonable attorneys’ fees, costs and other expenses. . (c) Entire Agreement. This Agreement shall constitute the entire agreement between the parties with respect to the subject matter hereof. It shall not be modified except by a written agreement signed by an authorized representative of Microchip. . (d) Severability. If any provision of this Agreement shall be held by a court of competent jurisdiction to be illegal, invalid or unenforceable, that provision shall be limited or eliminated to the minimum extent necessary so that this Agreement shall otherwise remain in full force and effect and enforceable. . (e) Waiver. No waiver of any breach of any provision of this Agreement shall constitute a waiver of any prior, concurrent or subsequent breach of the same or any other provisions hereof, and no waiver shall be effective unless made in writing and signed by an authorized representative of the waiving party. . (f) Export Regulation. Licensee agrees to comply with all export laws and restrictions and regulations of the Department of Commerce or other United States or foreign agency or authority. . (g) Survival. The indemnities, obligations of confidentiality, and limitations on liability described herein, and any right of action for breach of this Agreement prior to termination shall survive any termination of this Agreement. . (h) Assignment. Neither this Agreement nor any rights, licenses or obligations hereunder, may be assigned by Licensee without the prior written approval of Microchip except pursuant to a merger, sale of all assets of Licensee or other corporate reorganization, provided that assignee agrees in writing to be bound by the Agreement. . (i) Restricted Rights. Use, duplication or disclosure by the United States Government is subject to restrictions set forth in subparagraphs (a) through (d) of the Commercial Computer-Restricted Rights clause of FAR 52.227-19 when applicable, or in subparagraph (c)(1)(ii) of the Rights in Technical Data and Computer Software clause at DFARS 252.227-7013, and in similar clauses in the NASA FAR Supplement. Contractor/manufacturer is Microchip Technology Inc., 2355 W. Chandler Blvd., Chandler, AZ 85225-6199. . | If Licensee has any questions about this Agreement, please write to Microchip Technology Inc., 2355 W. Chandler Blvd., Chandler, AZ 85224-6199 USA, ATTN: Marketing. . Microchip MPLAB Harmony Integrated Software Framework. Copyright © 2015 Microchip Technology Inc. All rights reserved. . License Rev. 11/2015 . Copyright © 2015 Qualcomm Atheros, Inc. All Rights Reserved. . Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies. . THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. .",
    "url": "http://localhost:4000/aws_cloud/mplab_harmony_license.html",
    "relUrl": "/mplab_harmony_license.html"
  }
  ,"7": {
    "title": "",
    "content": ". Microchip MPLAB® Harmony 3 Release Notes . AWS Cloud Release Notes v3.1.0 . New Features . Supports ECC608 Integeration with FreeRTOS and Wi-Fi Support (WINC1500/WINC3400) for SAM D5x/E5x MCUs. | Updated version of FreeRTOS 202002.00 to add support for following SAM S70, SAM E70, SAM V70/V71, SAME5x, SAMD5x, PIC32MZ EF families of 32-bit microcontrollers to securely connect to the AWS Cloud. . | Development kit and demo application support - The following table provides number of demo application available for different development kits . Development kits Applications . SAM E70 Xplained Ultra Evaluation Kit | 1 | . SAM E54 Xplained Pro Evaluation Kit | 3 | . Curiosity PIC32MZ EF 2.0 Development Board | 1 | . | . Known Issues . Same as 3.0.0 | . Development Tools . MPLAB® X IDE v5.4 | MPLAB® XC32 C/C++ Compiler v2.41 | MPLAB® X IDE plug-ins: MPLAB® Harmony Configurator (MHC) v3.4.1 and above. | . | . Dependent Components . CSP v3.7.1 | CORE v3.7.2 | BSP v3.7.0 | DEV_PACKS v3.7.0 | NET v3.6.1 | Updated version of FreeRTOS 202002.00 for Microchip Products | MHC v3.4.1 | Cryptoauthlib v3.2.2 | . Microchip MPLAB® Harmony 3 Release Notes . AWS Cloud Release Notes v3.0.0 . New Features . Updated version of Amazon FreeRTOS 201908.00 to add support for SAM S70, SAM E70, SAM V70/V71, SAME5x, SAMD5x, PIC32MZ EF families of 32-bit microcontrollers to securely connect to the AWS Cloud . | Development kit and demo application support - The following table provides number of demo application available for different development kits . Development kits Applications . SAM E70 Xplained Ultra Evaluation Kit | 1 | . SAM E54 Xplained Pro Evaluation Kit | 1 | . Curiosity PIC32MZ EF 2.0 Development Board | 1 | . | . Known Issues . PIC32MZ Ethernet MAC driver does not provide configuration option to configure Unicast Hash and Multicast Hash filter. It must be enabled manually by changing the configuration macro to connect to AWS cloud. | . Development Tools . MPLAB® X IDE v5.30 | MPLAB® XC32 C/C++ Compiler v2.30 | MPLAB® X IDE plug-ins: MPLAB® Harmony Configurator (MHC) v3.3.5 and above. | . | . Dependent Components . CSP v3.6.0 | CORE v3.6.0 | BSP v3.6.0 | DEV_PACKS v3.6.0 | NET v3.5.1 | Updated version of Amazon FreeRTOS 201908.00 for Microchip Products | MHC v3.3.5 | .",
    "url": "http://localhost:4000/aws_cloud/release_notes.html",
    "relUrl": "/release_notes.html"
  }
  ,"8": {
    "title": "AWS Cloud Component and Applications",
    "content": ". MPLAB® Harmony 3 Configurations and Applications to securely connect IoT devices to the AWS cloud using FreeRTOS. . MPLAB® Harmony 3 is an extension of the MPLAB® ecosystem for creating embedded firmware solutions for Microchip 32-bit SAM and PIC® microcontroller and microprocessor devices. Refer to the following links for more information. . Microchip 32-bit MCUs | Microchip 32-bit MPUs | Microchip MPLAB X IDE | Microchip MPLAB® Harmony | Microchip MPLAB® Harmony Pages | . This repository contains the MPLAB® Harmony 3 AWS Cloud application examples . Release Notes | MPLAB® Harmony License | . Contents Summary . Folder Description . apps | Example applications for FreeRTOS | . config | FreeRTOS module configuration scripts | . doc | Image files | . docs | FreeRTOS help documentation | . templates | Configurations file templates | . Cloning AWS_Cloud repo . To clone or download the repo from Github,go to the main page of this repository and then click Clone button to clone this repo or download as zip file. This content can also be download using content manager by following these instructions . This repo contains scripts needed to represent FreeRTOS as Harmony 3 component. It requires FreeRTOS repository to be cloned for code generation. . Cloning FreeRTOS. . This repo uses Git Submodules to bring in dependent components. . Note: If you download the ZIP file provided by GitHub UI or using content-manager, you will not get the contents of the submodules. (The ZIP file is also not a valid git repository) . To clone: . git clone https://github.com/MicrochipTech/amazon-freertos --recurse-submodules . If you have downloaded the repo without using the --recurse-submodules argument, you need to run: . git submodule update --init --recursive . Getting Started . For more information on FreeRTOS, refer to the Getting Started guide of different boards. . Introduction . The FreeRTOS is abstracted as Harmony 3 component to easily configure and generate code to develop cloud connected applications using Harmony 3 framework. It uses updated version of FreeRTOS 202002.00 to support Microchip products for code generation. . Amazon FreeRTOS is now termed as FreeRTOS, but we still use the term Amazon FreeRTOS as the H3 component name to avoid confusion with existing H3 FreeRTOS (kernel) Component. . FreeRTOS is supported in the following products. . SAM E70/S70/V70/V71 Family + ECC608 (Optional) | SAM D5x/E5x Family + ECC608 (Optional) + WINC1500/WINC3400 (Optional) | PIC32MZ Embedded Connectivity with Floating Point Unit (EF) Family + ECC608 (Optional) | . This repository contains following three components for configuration and code generation. . AmazonFreeRTOS Component . Amazon FreeRTOS component is used to configure and generate FreeRTOS code, indepdent of any hardware configuration . . AmazonHWInterface component . The Hardware interface component is used to abstract device, interface and key storage configuration and code generation. . . There are three configurations supported by this component . Wired Solution Only. | . This solution is available in all platforms. . Wired + ECC608 Solution | . This solution is available in all platforms. . WIFI Solution (WINC based solution can be WINC1500/WINC3400) | . This solution is available in SAMD5x/E5x platform only. . AmazonDeviceTester component . Amazon DeviceTester component is used to configure and generate code for qualification testing. It adds required dependencies for testing the Amazon FreeRTOS solution using Amazon IDT (refer: https://docs.aws.amazon.com/freertos/latest/userguide/device-tester-for-freertos-ug.html). . . Important Licensing Information: For FreeRTOS License, please refer to the license file in the FreeRTOS repository. . AWS Cloud Examples . The following applications are provided to demonstrate the AWS Cloud H3 Component . Name Description . LED Shadow Client | This example application shows how to use the Shadow client feature to set/clear device status using LED(s) using ECC608 | . . . . . .",
    "url": "http://localhost:4000/aws_cloud/",
    "relUrl": "/"
  }
  
}`;
var data_for_search

var repo_name = "aws_cloud";
var doc_folder_name = "docs";
var localhost_path = "http://localhost:4000/";
var home_index_string = "AWS Cloud Component and Applications";

(function (jtd, undefined) {

// Event handling

jtd.addEvent = function(el, type, handler) {
  if (el.attachEvent) el.attachEvent('on'+type, handler); else el.addEventListener(type, handler);
}
jtd.removeEvent = function(el, type, handler) {
  if (el.detachEvent) el.detachEvent('on'+type, handler); else el.removeEventListener(type, handler);
}
jtd.onReady = function(ready) {
  // in case the document is already rendered
  if (document.readyState!='loading') ready();
  // modern browsers
  else if (document.addEventListener) document.addEventListener('DOMContentLoaded', ready);
  // IE <= 8
  else document.attachEvent('onreadystatechange', function(){
      if (document.readyState=='complete') ready();
  });
}

// Show/hide mobile menu

function initNav() {
  const mainNav = document.querySelector('.js-main-nav');
  const pageHeader = document.querySelector('.js-page-header');
  const navTrigger = document.querySelector('.js-main-nav-trigger');

  jtd.addEvent(navTrigger, 'click', function(e){
    e.preventDefault();
    var text = navTrigger.innerText;
    var textToggle = navTrigger.getAttribute('data-text-toggle');

    mainNav.classList.toggle('nav-open');
    pageHeader.classList.toggle('nav-open');
    navTrigger.classList.toggle('nav-open');
    navTrigger.innerText = textToggle;
    navTrigger.setAttribute('data-text-toggle', text);
    textToggle = text;
  })
}

// Site search

function initSearch() {

    data_for_search = JSON.parse(myVariable);
    lunr.tokenizer.separator = /[\s/]+/

    var index = lunr(function () {
        this.ref('id');
        this.field('title', { boost: 200 });
        this.field('content', { boost: 2 });
        this.field('url');
        this.metadataWhitelist = ['position']

        var location = document.location.pathname;
        var path = location.substring(0, location.lastIndexOf("/"));
        var directoryName = path.substring(path.lastIndexOf("/")+1);

        var cur_path_from_repo = path.substring(path.lastIndexOf(repo_name));

        // Decrement depth by 2 as HTML files are placed in repo_name/doc_folder_name
        var cur_depth_from_doc_folder = (cur_path_from_repo.split("/").length - 2);

        var rel_path_to_doc_folder = "";

        if (cur_depth_from_doc_folder == 0) {
            rel_path_to_doc_folder = "./"
        }
        else {
            for (var i = 0; i < cur_depth_from_doc_folder; i++)
            {
                rel_path_to_doc_folder = rel_path_to_doc_folder + "../"
            }
        }

        for (var i in data_for_search) {

            data_for_search[i].url = data_for_search[i].url.replace(localhost_path + repo_name, rel_path_to_doc_folder);

            if (data_for_search[i].title == home_index_string)
            {
                data_for_search[i].url = data_for_search[i].url + "index.html"
            }

            this.add({
                id: i,
                title: data_for_search[i].title,
                content: data_for_search[i].content,
                url: data_for_search[i].url
            });
        }
    });

    searchResults(index, data_for_search);

function searchResults(index, data) {
    var index = index;
    var docs = data;
    var searchInput = document.querySelector('.js-search-input');
    var searchResults = document.querySelector('.js-search-results');

    function hideResults() {
      searchResults.innerHTML = '';
      searchResults.classList.remove('active');
    }

    jtd.addEvent(searchInput, 'keydown', function(e){
      switch (e.keyCode) {
        case 38: // arrow up
          e.preventDefault();
          var active = document.querySelector('.search-result.active');
          if (active) {
            active.classList.remove('active');
            if (active.parentElement.previousSibling) {
              var previous = active.parentElement.previousSibling.querySelector('.search-result');
              previous.classList.add('active');
            }
          }
          return;
        case 40: // arrow down
          e.preventDefault();
          var active = document.querySelector('.search-result.active');
          if (active) {
            if (active.parentElement.nextSibling) {
              var next = active.parentElement.nextSibling.querySelector('.search-result');
              active.classList.remove('active');
              next.classList.add('active');
            }
          } else {
            var next = document.querySelector('.search-result');
            if (next) {
              next.classList.add('active');
            }
          }
          return;
        case 13: // enter
          e.preventDefault();
          var active = document.querySelector('.search-result.active');
          if (active) {
            active.click();
          } else {
            var first = document.querySelector('.search-result');
            if (first) {
              first.click();
            }
          }
          return;
      }
    });

    jtd.addEvent(searchInput, 'keyup', function(e){
      switch (e.keyCode) {
        case 27: // When esc key is pressed, hide the results and clear the field
          hideResults();
          searchInput.value = '';
          return;
        case 38: // arrow up
        case 40: // arrow down
        case 13: // enter
          e.preventDefault();
          return;
      }

      hideResults();

      var input = this.value;
      if (input === '') {
        return;
      }

      var results = index.query(function (query) {
        var tokens = lunr.tokenizer(input)
        query.term(tokens, {
          boost: 10
        });
        query.term(tokens, {
          wildcard: lunr.Query.wildcard.TRAILING
        });
      });

      if (results.length > 0) {
        searchResults.classList.add('active');
        var resultsList = document.createElement('ul');
        resultsList.classList.add('search-results-list');
        searchResults.appendChild(resultsList);

        for (var i in results) {
          var result = results[i];
          var doc = docs[result.ref];

          var resultsListItem = document.createElement('li');
          resultsListItem.classList.add('search-results-list-item');
          resultsList.appendChild(resultsListItem);

          var resultLink = document.createElement('a');
          resultLink.classList.add('search-result');
          resultLink.setAttribute('href', doc.url);
          resultsListItem.appendChild(resultLink);

          var resultTitle = document.createElement('div');
          resultTitle.classList.add('search-result-title');
          resultTitle.innerText = doc.title;
          resultLink.appendChild(resultTitle);

          var resultRelUrl = document.createElement('span');
          resultRelUrl.classList.add('search-result-rel-url');
          resultRelUrl.innerText = doc.relUrl;
          resultTitle.appendChild(resultRelUrl);

          var metadata = result.matchData.metadata;
          var contentFound = false;
          for (var j in metadata) {
            if (metadata[j].title) {
              var position = metadata[j].title.position[0];
              var start = position[0];
              var end = position[0] + position[1];
              resultTitle.innerHTML = doc.title.substring(0, start) + '<span class="search-result-highlight">' + doc.title.substring(start, end) + '</span>' + doc.title.substring(end, doc.title.length)+'<span class="search-result-rel-url">'+doc.relUrl+'</span>';

            } else if (metadata[j].content && !contentFound) {
              contentFound = true;

              var position = metadata[j].content.position[0];
              var start = position[0];
              var end = position[0] + position[1];
              var previewStart = start;
              var previewEnd = end;
              var ellipsesBefore = true;
              var ellipsesAfter = true;
              for (var k = 0; k < 3; k++) {
                var nextSpace = doc.content.lastIndexOf(' ', previewStart - 2);
                var nextDot = doc.content.lastIndexOf('.', previewStart - 2);
                if ((nextDot > 0) && (nextDot > nextSpace)) {
                  previewStart = nextDot + 1;
                  ellipsesBefore = false;
                  break;
                }
                if (nextSpace < 0) {
                  previewStart = 0;
                  ellipsesBefore = false;
                  break;
                }
                previewStart = nextSpace + 1;
              }
              for (var k = 0; k < 10; k++) {
                var nextSpace = doc.content.indexOf(' ', previewEnd + 1);
                var nextDot = doc.content.indexOf('.', previewEnd + 1);
                if ((nextDot > 0) && (nextDot < nextSpace)) {
                  previewEnd = nextDot;
                  ellipsesAfter = false;
                  break;
                }
                if (nextSpace < 0) {
                  previewEnd = doc.content.length;
                  ellipsesAfter = false;
                  break;
                }
                previewEnd = nextSpace;
              }
              var preview = doc.content.substring(previewStart, start);
              if (ellipsesBefore) {
                preview = '... ' + preview;
              }
              preview += '<span class="search-result-highlight">' + doc.content.substring(start, end) + '</span>';
              preview += doc.content.substring(end, previewEnd);
              if (ellipsesAfter) {
                preview += ' ...';
              }

              var resultPreview = document.createElement('div');
              resultPreview.classList.add('search-result-preview');
              resultPreview.innerHTML = preview;
              resultLink.appendChild(resultPreview);
            }
          }
        }
      }
    });

    jtd.addEvent(searchInput, 'blur', function(){
      setTimeout(function(){ hideResults() }, 300);
    });
  }
}

function pageFocus() {
  var mainContent = document.querySelector('.js-main-content');
  mainContent.focus();
}

// Document ready

jtd.onReady(function(){
  initNav();
  pageFocus();
  if (typeof lunr !== 'undefined') {
    initSearch();
  }
});

})(window.jtd = window.jtd || {});


