# Windows System Management Script

This script demonstrates how to modify the Windows Registry to disable USB ports, Bluetooth, block websites, and restrict the Command Prompt. **Please note:** These modifications can have unintended consequences and security implications. This script is intended for **educational purposes** only and should **not** be used on production systems or systems with sensitive data.

## Prerequisites

- Windows Operating System (Windows 7 or later)
- Python 3.x installed
- Administrative privileges

## How to Run

1. Open a command prompt with **administrative privileges**:
    - Click on the Start icon in the bottom left-hand corner.
    - Type "cmd" into the search bar.
    - Right-click on "Command Prompt" and select "Run as administrator".

2. Navigate to the directory containing the script using the `cd` command:
    ```sh
    cd path\to\script\directory
    ```

3. Run the script:
    ```sh
    python script_name.py
    ```
   Replace `script_name.py` with the actual name of the script you want to run.

4. Follow the prompts and observe the script's output.

## Running in a Virtual Machine (VM)

If you want to run this script in a virtual machine, follow these additional steps:

1. Set up a virtual machine environment using software like VMware, VirtualBox, or Hyper-V.

2. Install a Windows guest operating system in the virtual machine.

3. Ensure the guest operating system has **administrative privileges**.

4. Copy the script to the virtual machine using shared folders or other methods.

5. Follow the steps mentioned above to open a command prompt with administrative privileges within the virtual machine.

6. Navigate to the directory containing the script and run it using the same commands as mentioned above.

## Disclaimer

- This script is provided for **educational purposes** only.
- Modifying the Windows Registry can have unintended consequences and security risks.
- Use this script with caution and on non-production systems only.
- **Always back up your data and system before making any changes.**

