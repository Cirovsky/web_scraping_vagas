import pandas as pd
import spacy

nlp = spacy.load("pt_core_news_sm")


def quebrar_pontuacao(termo:str):
    #para o Ciro do futuro: tente implementar um regex aqui ao invés de usar .__contains__()
    lista_termos = []
    if termo.__contains__("."):
        for t in termo:
            lista_termos.append(quebrar_mais_palavras(t))
        return lista_termos
    else:
        return quebrar_mais_palavras(termo)

def quebrar_mais_palavras(termo:str):
    lista_termos = []
    lista = [c.isupper() for c in termo]
    print(sum(lista))
    tem_maiuscula = any(lista)
    if tem_maiuscula:
        indices_verdadeiros = [i for i,v in enumerate(lista) if v is True]
        if (lista[0] is True ) and (indices_verdadeiros == 1):
            return termo
        else:
            lista_termos.append(termo[:indices_verdadeiros[0]])
            lista_termos.append(termo[indices_verdadeiros[-1]:])
            print(lista_termos)
            if len(indices_verdadeiros) > 1:
                indices_verdadeiros.pop(0)
                





def limpa_insignificantes(texto:str):
    lista_termos = []
    for termo in texto.split(" "):
        lista_termos.append(quebrar_pontuacao(termo))
    exit()
    doc = nlp(texto)

    sem_insignificantes = [token.text for token in doc if token.pos_ not in {"ADP", "DET","PRON","SCONJ"}]
    return sem_insignificantes

df = pd.read_excel("dados/analista_de_dados.xlsx")
df["description"] = df["description"].map(lambda texto: limpa_insignificantes(texto))
lista = df["description"].at[0]
print(lista)