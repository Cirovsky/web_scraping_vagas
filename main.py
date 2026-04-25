import requests
import pandas as pd
import time, random
from table_format import export_xlsx
def buscar_gupy(keyword):

    df:pd.DataFrame = pd.DataFrame({})
    
    url= "https://portal.api.gupy.io/api/job"
    headers = {"User-Agent":"Mozzila/5.0"}

    offset = 0
    while True:
        params ={
            "name":keyword,
            "offset":offset
        }

        resp = requests.get(url=url, params = params, headers=headers)
        dados = resp.json()
        total = dados["pagination"]["total"]#total de vagas
        
        df_vagas:pd.DataFrame =  pd.DataFrame(dados["data"])
        df = pd.concat([df,df_vagas])
        if df.shape[0] >= total:
            break
        offset += 10
        time.sleep(random.uniform(1, 3))
        
    return df

df = (buscar_gupy("Analista"))

export_xlsx(df, "dados/analista",sheet_name="vagas_dados")