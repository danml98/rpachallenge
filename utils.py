import pandas as pd


def read_excel(path) -> list:
    """
    Realiza a leitura da planilha, percorre as linhas e transforma em um dicionário para cada pessoa, em seguida adiciona este dicionário em uma lista.

    Args:
        path (str): Caminho da planilha

    Returns:
        list: Lista com os dicionários de cadastros
    """      

    dataframe = pd.read_excel(path)
    lista_cadastros = []
    
    for lista in dataframe.values:
        dict_cadastro = {}    
        for idx, chave in enumerate(dataframe.columns):
            dict_cadastro.update({chave: lista[idx]})
        
        lista_cadastros.append(dict_cadastro)

    return lista_cadastros