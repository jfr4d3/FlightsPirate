from time import sleep
import pandas as pd
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os

# URL de la página web a analizar
url = "https://www.google.com/travel/flights/search"

# Realizar la solicitud GET a la página web
response = requests.get(url)

# Comprobar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Crear un objeto BeautifulSoup con el contenido HTML de la página
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Encontrar todos los elementos HTML que contienen información sobre los productos
    #products = soup.find_all("div", class_="product")
    
    # Iterar sobre cada elemento de producto encontrado
    #for product in products:
        # Extraer el nombre del producto
     #   name = product.find("h2", class_="product-name").text.strip()
        
        # Extraer el precio del producto
      #  price = product.find("span", class_="product-price").text.strip()
        
        # Imprimir el nombre y el precio del producto
      #  print("Nombre del producto:", name)
      #  print("Precio:", price)
      #  print("-----------------------------------")

else:
    print("Error al acceder a la página:", response.status_code)

