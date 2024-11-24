# License Validator GUI with PyQt5

This project is a GUI-based application developed using Python and PyQt5. It allows users to input a license key, validates it, and, if the key is valid, opens a specified application or file. This implementation is tailored for macOS but can be adapted for other platforms.

---

## Features

- **Intuitive GUI**: Built using PyQt5 for a modern and user-friendly interface.
- **Secure Input**: License keys are masked for security during entry.
- **License Validation**: Validates the entered key against "VALID_LICENSE_KEY" valid key.
- **Application Launcher**: Opens the specified application or file if the license is valid.
- **Error Handling**: Provides clear error messages for invalid keys.

---

## Prerequisites

### 1. Set variables 
Modify the "app_path" variable to point to the application or file you want to launch upon successful validation.
Modify "VALID_LICENSE_KEY" with your code.

### 2. Python Environment
- Python 3.6 or higher is required.

### 3. PyQt5 Installation
Install PyQt5 using pip:
```bash
pip install PyQt5
```

### 4. PyInstaller Installation
To convert the Python script into an .exe file, install PyInstaller:
```bash
pip install pyinstaller
```

### 5. Creating the Executable
Run the following command to generate the .exe file:
```bash
pyinstaller --onefile license.py
```
The generated .exe file will be located in the dist/ directory.
