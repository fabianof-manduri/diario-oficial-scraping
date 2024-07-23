import sys
import pyodbc
import json
import io
import os

def Gerar_Json(gerar_todos_arquivos):
    conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                          f'Server=JL-Fabiano;'
                                          f'Database=diario_oficial;'
                                          f'Trusted_connection=yes;')

    cursor = conexao.cursor()

    if gerar_todos_arquivos=='S':
        arquivo_criacao = 'json_diario.json'
        cursor.execute("select *, FORMAT(data_publicacao, 'dd/MM/yyyy') as data from diario_informacoes")
    else:
        arquivo_criacao = 'json_diario_duplicado.json'
        cursor.execute("select *, FORMAT(data_publicacao, 'dd/MM/yyyy') as data from diario_informacoes where edicao in (select edicao from diario_informacoes group by edicao having count(edicao) > 1) order by edicao")


    estrutura_json = []

    for resultado in cursor.fetchall():
        estrutura_json.append({
            "Edicao": resultado[0],
            "Titulo": f"{resultado[1]}",
            "Conteudo": f"{resultado[2]}",
            "DataPublicacao": f"{resultado[5]}",
            "FileName": f"{resultado[4]}"}
        )

    json_resultado = json.dumps(estrutura_json, ensure_ascii=False, indent=4)
    print(json_resultado)

    print('Criação do arquivo', arquivo_criacao)
    print('Criado em:', os.getcwd() + '\\' + arquivo_criacao)
    with io.open(f'{arquivo_criacao}', 'w', encoding='utf8') as json_arquivo:
        json_arquivo.write(json_resultado)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1].upper() == 'S':
            Gerar_Json(gerar_todos_arquivos='S')
        else:
            Gerar_Json(gerar_todos_arquivos='N')

        print('Gerando arquivo json...')
    else:
        print('Não foi possível gerar o arquivo json, pois não foram informados os parâmetros corretos.')
