import requests
import pandas as pd
import json
#import bs4

def buscar_gupy(keyword):
    url= "https://portal.api.gupy.io/api/job"
    params ={
        "name":keyword,
        "limit":1000,
        "offset":0
    }

    headers = {"User-Agent":"Mozzila/5.0"}
    resp = requests.get(url=url, params = params, headers=headers)
    dados = resp.json()
    vagas = []
    return dados["data"]


df = pd.DataFrame(buscar_gupy("Analista"))

print(df)
print(df.columns)
print(df["description"])