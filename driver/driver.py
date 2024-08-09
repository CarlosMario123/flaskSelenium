from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.firefox import GeckoDriverManager

class DriverGeko:
    def __init__(self, url):
        # Configura las opciones del navegador
        self.options = Options()
        self.options.headless = True  # Ejecuta el navegador en modo headless (sin interfaz gráfica)
        
        # Inicializa el navegador con el controlador adecuado
        self.driver = webdriver.Firefox(service=webdriver.firefox.service.Service(GeckoDriverManager().install()), options=self.options)
        self.url = url  # URL a scrapear

    def scrapearImg(self):
        self.driver.get(self.url)
        try:
            # Espera hasta que al menos una imagen esté presente en la página
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
        
            # Encuentra todas las imágenes en la página
            imagenes = self.driver.find_elements(By.TAG_NAME, 'img')
            return imagenes
        except StaleElementReferenceException:
            # Maneja la excepción y vuelve a intentar después de un breve retraso
            sleep(1)
            return self.scrapearImg()  # Reintenta la operación
        except NoSuchElementException:
            # Maneja el caso cuando no se encuentran elementos
            print("No se encontraron imágenes en la página.")
            return []
        finally:
            # Asegúrate de cerrar el navegador después de usarlo
            self.driver.quit()