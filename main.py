import cv2
import numpy as np
import pyautogui
import time
import signal
import sys
import winsound
from typing import Optional


class GoldenCookieDetector:
    def __init__(self, template_path: str, confidence_threshold=0.55):
        self.template = self._load_template(template_path)
        self.confidence_threshold = confidence_threshold

    @staticmethod
    def _load_template(path: str) -> np.ndarray:
        template = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if template is None:
            raise FileNotFoundError("Could not load golden cookie image")
        return template

    @staticmethod
    def capture_active_window() -> np.ndarray:
        window = pyautogui.getActiveWindow()
        if window is None:
            raise Exception("No active window found")

        screenshot = pyautogui.screenshot(
            region=(window.left, window.top, window.width, window.height)
        )
        screenshot_np = np.array(screenshot)
        return cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    def detect_golden_cookie(self, screen: np.ndarray) -> bool:
        result = cv2.matchTemplate(screen, self.template, cv2.TM_CCOEFF_NORMED)
        return np.any(result >= self.confidence_threshold)


def run_detector(
    detector: GoldenCookieDetector, check_interval: float = 1.0, cooldown: float = 10.0
) -> None:
    def signal_handler(sig: int, frame: Optional[object]) -> None:
        print("\nExiting gracefully...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        while True:
            try:
                screen = detector.capture_active_window()
                if detector.detect_golden_cookie(screen):
                    print("Found a golden cookie!")
                    winsound.Beep(1000, 750)
                    time.sleep(cooldown)
            except Exception as e:
                print(f"Error capturing active window: {e}")
            time.sleep(check_interval)
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)


if __name__ == "__main__":
    detector = GoldenCookieDetector("golden_cookie.jpg")
    run_detector(detector)
