import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso():
    driver = webdriver.Chrome()
    # Espera implicita 
    driver.implicitly_wait(10)

    wait = WebDriverWait(driver,10)
    
    try:
        #Abrir pagina 
        driver.get("https://www.saucedemo.com/")

        #Localizar elementos
        usuario = wait.until(EC.presence_of_element_located((By.ID,"user-name")))
        #driver.find_element(By.ID,"user-name")
        password = wait.until(EC.presence_of_element_located((By.ID,"password")))
        #driver.find_element(By.ID,"password")
        boton_login = wait.until(EC.element_to_be_clickable((By.ID,"login-button")))
        
        #driver.find_element(By.ID,"login-button")
   
        #Completar el formulario
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        # time.sleep(2)
        # Hacer login
        boton_login.click()

        # Titulo
        # titulo = driver.find_element(By.CLASS_NAME,"app_logo")
        # Ejemplo de Selector
        # titulo = driver.find_element(By.CSS_SELECTOR,".header_label >.app_logo")
        # assert titulo.text == "Swag Labs"  
        # Validar el URL despues del login
        # assert driver.current_url == "https://www.saucedemo.com/inventory.html" 
        assert "/inventory.html" in driver.current_url

        # Validacion texto
        logo =driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

        titulo = driver.find_element(By.CSS_SELECTOR,"[data-test = 'title']")
        assert titulo.text == "Products"
    finally:
        driver.quit()
