"""
please be aware of the following considerations:

1. Safety and Consequences: Modifying the Windows Registry can have unintended consequences and potentially cause system instability or security vulnerabilities. 
                            It's crucial to exercise extreme caution when making changes to the Registry. Incorrect changes can lead to serious issues, and testing such code on a production system is not recommended.

2. Permissions: Accessing and modifying the Windows Registry usually requires administrative privileges. 
                Ensure that the script is executed with administrative rights to avoid permission issues.
"""


import os
import subprocess
import ctypes

def disable_usb_ports_bluetooth():
    """
    Disable USB ports and Bluetooth by modifying the Windows Registry.
    """
    try:
        # Disable USB ports by modifying the USBSTOR registry key
        subprocess.run(["reg", "add", "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR",
                        "/v", "Start", "/t", "REG_DWORD", "/d", "4", "/f"])
        print("USB ports disabled.")
        
        # Disable Bluetooth by modifying the BTHPORT registry key
        subprocess.run(["reg", "add", "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\BTHPORT\\Parameters",
                        "/v", "BluetoothEnable", "/t", "REG_DWORD", "/d", "0", "/f"])
        print("Bluetooth disabled.")

    except subprocess.CalledProcessError as e:
        print("Error:", e)

def disable_command_prompt():
    """
    Block the Command Prompt by modifying the Windows Registry.
    
    This function modifies the Windows Registry to disable the Command Prompt
    by setting the appropriate registry key and value.

    """
    try:
        # Create or open the registry key for restricting the Command Prompt
        key_path = "Software\\Policies\\Microsoft\\Windows\\System"
        key_handle = ctypes.windll.advapi32.RegCreateKeyExW(ctypes.c_uint(0x80000001), ctypes.c_wchar_p(key_path), 0, None, 0, ctypes.c_uint(0xF003F), None, None, None)

        # Set the value to restrict the Command Prompt
        value_name = "DisableCMD"
        value_type = 4  # REG_DWORD
        value_data = ctypes.c_uint(2)  # Set to 2 to restrict Command Prompt
        ctypes.windll.advapi32.RegSetValueExW(key_handle, value_name, 0, value_type, ctypes.byref(value_data), ctypes.sizeof(value_data))

        print("Command Prompt restricted.")

    except Exception as e:
        print("Error:", e)


def block_website(website):
    """
    Add a website restriction to the Windows Registry.

    This function adds a website restriction to the Windows Registry by modifying
    the necessary registry keys and values.

    Parameters:
    website (str): The website domain to be restricted (e.g., "facebook.com").

    """
    try:
        # Construct the key path
        key_path = "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\" + website
        # Create or open the registry key
        key_handle = ctypes.windll.advapi32.RegCreateKeyExW(ctypes.c_uint(0x80000001), ctypes.c_wchar_p(key_path), 0, None, 0, ctypes.c_uint(0xF003F), None, None, None)
        
        # Set the value to restrict the website
        value_name = "*"
        value_type = 4
        value_data = ctypes.c_uint(4)
        ctypes.windll.advapi32.RegSetValueExW(key_handle, value_name, 0, value_type, ctypes.byref(value_data), ctypes.sizeof(value_data))
        
        print(f"Website restriction added for {website}.")

    except Exception as e:
        print("Error:", e)

def main():
    """
    Main function to block a website, disable USB ports and Bluetooth, and disable command prompt.
    """
    block_website("facebook.com")
    disable_usb_ports_bluetooth()
    disable_command_prompt()

if __name__ == "__main__":
    main()
