# Cookie Clicker Golden Cookie Detector

This Python script automatically detects golden cookies in the Cookie Clicker game and alerts the user with a sound notification.

Its main purpose is to help obtaining the achievements `Neverclick`, [True Neverclick](https://cookieclicker.fandom.com/wiki/True_Neverclick) and [Hardcore](https://cookieclicker.fandom.com/wiki/Hardcore) without having to constantly monitor the screen for golden cookies to click.
The script is also useful during early game runs before unlocking the `Golden Cookie Alert Sound` upgrade.

## Description

This script captures the active window (assumed to be the Cookie Clicker game), scans for the presence of a golden cookie using image recognition, and plays a beep sound when one is detected. It's designed to run continuously in the background while you play Cookie Clicker.


## Prerequisites
- Python 3.12+
- [Poetry](https://python-poetry.org/docs/) for dependency management

## Installation

1. Clone this repository
2. Install dependencies using Poetry:

```bash
poetry install
```

## Usage

1. Run the script:

```bash
poetry run python golden_cookie_detector.py
```

2. Switch to your Cookie Clicker game window. The script will start monitoring for golden cookies and play an alert when one is found.
3. Press Ctrl+C in the terminal to stop the script.

## Notes

- This script has only been tested on Window with the Steam version of Cookie Clicker. Other operating systems and/or versions of the game might not work correctly without updating the code.

- Adjust the `confidence_threshold` in the `detect_golden_cookie` function if you're getting false positives from the standard cookies in the background.
