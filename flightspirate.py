
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del servicio de GeckoDriver
service = FirefoxService('/Users/javi/geckodriver')
driver = webdriver.Firefox(service=service)
driver.get("https://www.google.com/travel/flights/search")

#driver.implicitly_wait(5)

try:
    accept_cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Rechazar Todo')]"))
    )
    accept_cookies_button.click()
    print("Cookies rechazadas.")
except:
    print("No se encontró el botón de aceptar cookies o no era necesario.")