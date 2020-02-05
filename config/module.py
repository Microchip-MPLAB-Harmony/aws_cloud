autoConnectTableDebug = [["sys_debug", "sys_debug_SYS_CONSOLE_dependency", "sys_console_0", "sys_console"]]
autoConnectTableCmd = [["sys_command", "sys_command_SYS_CONSOLE_dependency", "sys_console_0", "sys_console"]]

def loadModule():
    print("Load Module: Third Party Library - AWS Cloud")

    aws_cloud = Module.CreateComponent("AmazonFreeRTOS", "AmazonFreeRTOS", "/Third Party Libraries/Cloud/", "config/aws_freertos.py")
    aws_cloud.setDisplayType("Third Party Library")
    aws_cloud.addCapability("AmazonFreeRTOS", "RTOS", True)
    aws_cloud.addDependency("AmazonHWInterface", "AmazonHWInterface")
	
    aws_cloud_test = Module.CreateComponent("AmazonDeviceTester", "AmazonDeviceTester", "/Third Party Libraries/Cloud/", "config/aws_freertos_test.py")
    aws_cloud_test.setDisplayType("Third Party Library")
    aws_cloud_test.addCapability("AmazonDeviceTester", "RTOS", True)
    aws_cloud_test.addDependency("AmazonHWInterface", "AmazonHWInterface")

    aws_cryptp = Module.CreateComponent("AmazonHWInterface", "AmazonHWInterface", "/Third Party Libraries/Cloud/", "config/hwinterface.py")
    aws_cryptp.setDisplayType("Third Party Library")
    aws_cryptp.addCapability("AmazonHWInterface", "AmazonHWInterface", False)
    aws_cryptp.addDependency("NETCONFIG_MAC_Dependency", "MAC")
    aws_cryptp.addDependency("Core_SysTime_Dependency", "SYS_TIME", None, True, True)

    
