import os
import json
import glob

#Cria função para realizar a ação de abrir o arquivo e alterar os caracteres no arquivo.
#O arquivo precisa ficar em txt.
nome_arquivo = input (f"Informe o nome do arquivo: \n")

#Cria a função para procurar o texto de caracteres listados abaixo.
try:
    def search_str(arquivo, search_text, replace_text):
        with open(arquivo, 'r') as file:
            dados = file.read()
            dados = dados.replace(search_text,replace_text)
        
        with open(arquivo,"w") as file:
            file.write(dados)

#Aqui é alterado os caracteres em código para caracteres normais e sem acentuação
    search_str(f"{nome_arquivo}","\\u00f3","o")
    search_str(f"{nome_arquivo}","\\u00ea","e")
    search_str(f"{nome_arquivo}","\\u00ed","i")
    search_str(f"{nome_arquivo}","\\u00e7o","c")
    search_str(f"{nome_arquivo}","\\u00fa","u")
    search_str(f"{nome_arquivo}","\\u00e3","a")

    print ("Texto alterado")

#Tratamento de Exceções
except Exception as erros:
    print(f"Não funcionou porque: {erros}")