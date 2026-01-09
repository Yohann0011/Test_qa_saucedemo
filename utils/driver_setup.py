import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

def get_driver():
    driver_path = os.path.join(os.path.dirname(__file__), '..', 'drivers', 'msedgedriver.exe')
    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"msedgedriver.exe no encontrado en: {driver_path}")

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(10)
    return driver