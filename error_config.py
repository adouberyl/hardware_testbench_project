class DeviceError(Exception):
    pass

class CommandInvalidError(DeviceError):
    pass

class ReturnInvalidError(DeviceError):
    pass