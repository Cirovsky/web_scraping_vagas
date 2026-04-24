import requests
import pandas as pd
#import bs4

def buscar_gupy(keyword):
    url= "https://portal.api.gupy.io/api/job"
    params ={
        "name":keyword,
        "limit":100,
        "offset":0
    }

    headers = {"User-Agent":"Mozzila/5.0"}
    resp = requests.get(url=url, params = params, headers=headers)
    dados = resp.json()
    print(dados)

buscar_gupy("Analista de Dados")