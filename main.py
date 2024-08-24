import cv2
import numpy as np
import pyautogui
import time
import signal
import sys
from typing import Optional


def signal_handler(sig: int, frame: Optional[object]) -> None:
    print("\nExiting gracefully...")
    sys.exit(0)


def capture_active_window() -> np.ndarray:
    window = pyautogui.getActiveWindow()
    if window is None:
        raise Exception("No active window found")

    screenshot = pyautogui.screenshot(
        region=(window.left, window.top, window.width, window.height)
    )
    screenshot_np = np.array(screenshot)
    return cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)


def detect_golden_cookie(
    screen: np.ndarray, template: np.ndarray, confidence_threshold=0.5
) -> bool:
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    return np.any(result >= confidence_threshold)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    try:
        golden_cookie_image = cv2.imread("golden_cookie.jpg", cv2.IMREAD_UNCHANGED)
        if golden_cookie_image is None:
            raise FileNotFoundError("Could not load golden cookie image")

        while True:
            try:
                screen = capture_active_window()
                if detect_golden_cookie(screen, golden_cookie_image):
                    print("Found a golden cookie")
                    time.sleep(10)
            except Exception as e:
                print(f"Error capturing active window: {e}")
            time.sleep(1)

    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)
