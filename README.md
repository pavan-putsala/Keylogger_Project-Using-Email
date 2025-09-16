# Keylogger_Project-Using-Email



# Keylogger

## Overview

**keylogger.py** is a Python script implementing a simple keylogger that records keyboard events and automatically sends the collected keystrokes to a Gmail address when the log length reaches 100 characters. It uses the `pynput` library for interception and `smtplib` for sending logs via email.[1]

## Features

- Monitors and logs all keyboard input (including spaces, enters, and backspaces).[1]
- Sends keystroke logs as email after accumulating 100 characters.
- Operates silently in the background without a visible window.

## Requirements

- Python 3.x
- Required Python modules:
  - `pynput`
  - `smtplib`
  - `email.mime`

Install dependencies via pip:
```bash
pip install pynput
```

## Configuration

- Update these variables in the script if needed:
  - `from_email` – sender address (Gmail)
  - `to_email` – recipient address (Gmail, can be the same)
  - `password` – Gmail app password or account password
- Make sure “Allow less secure apps” is enabled for the Gmail account, or set up an app-specific password.

## Usage

1. Download or clone the script file as `keylogger.py`.
2. Launch the script with:
   ```bash
   python keylogger.py
   ```
   - For silent execution, use:
     ```bash
     pythonw keylogger.py
     ```
3. The script will listen and log all keystrokes. When the number of characters reaches 100, it will send the log via Gmail SMTP and reset the log.

## Legal Notice

This script is provided **strictly for educational and authorized testing purposes**. Unauthorized use to record keystrokes on systems without consent is illegal. Always obtain proper permission before running or distributing this tool.

## License

MIT License

