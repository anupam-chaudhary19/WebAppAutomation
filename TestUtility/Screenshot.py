class screenshotss(object):
    def __init__(self,driver):
        self.driver = driver

    def Screenshot(self,path):
        directory= "C:/Users/Anupam/PycharmProjects/WebAppAutomation/TestUtility"
        self.driver.get_screenshot_as_file(directory+path)
