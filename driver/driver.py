from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from time import sleep


class DriverGeko:
    def __init__(self, url):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options)
        self.url = url  # URL a scrapear

    def scrapearImg(self):
        self.driver.get(self.url)
        try:
            # Esperar hasta que todas las imágenes estén presentes en la página
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
        
            imagenes = self.driver.find_elements(By.TAG_NAME, 'img')
            return imagenes
        except StaleElementReferenceException:
            # Manejar la excepción y volver a intentar la operación después de un breve retraso
            sleep(1)
            return self.scrapearImg()  # Volver a intentar la operación