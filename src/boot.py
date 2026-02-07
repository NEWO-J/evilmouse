import storage
import usb_cdc

# Disable the CIRCUITPY USB drive
storage.disable_usb_drive()

# Disable serial console (optional but common in production)
usb_cdc.disable()

print("USB storage and serial disabled — HID only mode")
