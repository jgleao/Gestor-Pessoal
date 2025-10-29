import pandas as pd
from datetime import datetime
import os

ARQUIVO_EXCEL = "gastos.xlsx"

def validar_data(data_str):

    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validar_valor(valor):

    try:
        valor = float(valor)
        return valor >= 0
    except ValueError:
        return False

def carregar_dados():

    if os.path.exists(ARQUIVO_EXCEL):
        return pd.read_excel(ARQUIVO_EXCEL)
    else:
        return pd.DataFrame(columns=["Data", "Categoria", "Valor"])

def salvar_dados(df):

    df.to_excel(ARQUIVO_EXCEL, index=False)

def adicionar_gasto(data, categoria, valor):

    df = carregar_dados()
    novo_gasto = {"Data": data, "Categoria": categoria, "Valor": float(valor)}
    df = pd.concat([df, pd.DataFrame([novo_gasto])], ignore_index=True)
    salvar_dados(df)
    print("Gasto adicionado com sucesso!")

def listar_gastos():

    df = carregar_dados()
    if df.empty:
        print("Vazio.")
    else:
        print("LISTA DE GASTOS")
        print(df)
        print("Total gasto: R$ {:.2f}".format(df["Valor"].sum()))
