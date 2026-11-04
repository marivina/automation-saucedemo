import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

def test_login_exitoso():
    driver = webdriver.Chrome()

    try:
        #Abrir pagina 
        driver.get("https://www.saucedemo.com/")

        #Localizar elementos
        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")
   
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
