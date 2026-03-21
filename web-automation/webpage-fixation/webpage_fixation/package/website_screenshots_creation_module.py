from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time


def take_screenshots_from_website(url, output_path, screen_resolution, progressbar, overlap_percentage=0.2):
    """
    Takes screenshots of the webpage with overlap and returns a list of image paths.
    """
    try:
        width, height = map(int, screen_resolution.split('x'))
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        # Set window size for full page screenshots
        options.add_argument(f"--window-size={width},{height}")

        driver = webdriver.Chrome(options=options)
        driver.get(url)
        progressbar["value"] += 5
        time.sleep(10)
        total_height = driver.execute_script(
            "return document.body.parentNode.scrollHeight")
        viewport_height = driver.execute_script("return window.innerHeight")
        progressbar["value"] += 5

        screenshots = []
        y_offset = 0

        while y_offset < total_height:
            timestamp = datetime.datetime.now()
            path_timestamp = timestamp.strftime(f"%d-%m-%Y_%H-%M-%S")
            screenshot_path = rf"{output_path}\screenshot_{path_timestamp}.png"
            driver.save_screenshot(screenshot_path)
            new_timestamp = timestamp.strftime(f"%d-%m-%Y %H:%M:%S")
            screenshots.append(
                [screenshot_path, new_timestamp])

            # Calculate overlap for next screenshot
            overlap_pixels = int(viewport_height * overlap_percentage)
            y_offset += viewport_height - overlap_pixels

            driver.execute_script(f"window.scrollTo(0, {y_offset})")
            time.sleep(1)
            progressbar["value"] += 3
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        driver.quit()
        return screenshots


if __name__ == "__main__":
    pass
