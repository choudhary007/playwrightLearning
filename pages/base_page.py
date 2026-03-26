from utils.logger import get_logger

class BasePage:
    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def click(self, locator):
        try:
            self.logger.info(f"Clicking on element: {locator}")
            locator.wait_for()
            locator.click()
            self.logger.info("Click successful")
        except Exception as e:
            self.logger.error(f"Error clicking on {locator}: {str(e)}")
            raise

    def fill(self, locator, value):
        print("LOGGER OBJECT:", self.logger)
        safe_value = "****" if "password" in str(locator).lower() else value
        self.logger.info(f"Filling {locator} with value: {safe_value}")
        locator.wait_for()
        locator.fill(value)

    def get_text(self, locator):
        text = locator.inner_text()
        self.logger.info(f"Getting text: {text}")
        return text

    def is_visible(self, locator):
        return locator.is_visible()

    def wait_for_element(self, locator):
        self.logger.info(f"Waiting for: {locator}")
        locator.wait_for()