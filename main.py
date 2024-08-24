import cv2
import numpy as np
import pyautogui
import time


def capture_screen() -> np.ndarray:
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    return cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)


def detect_golden_cookie(
    screen: np.ndarray, template: np.ndarray, confidence_threshold=0.5
) -> float:
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    return np.any(result >= confidence_threshold)


while True:
    golden_cookie_image = cv2.imread("golden_cookie.jpg", cv2.IMREAD_UNCHANGED)
    screen = capture_screen()
    if detect_golden_cookie(screen, golden_cookie_image):
        print("Found a golden cookie")
        time.sleep(10)

    time.sleep(1)
