#FORMAS DE UTILIZAÇÃO

=====================================================================================================================
Para realizar o scraping das informações do portal da transparência de Riversul primeiro crie um ambiente virtual.
Obs.: o ambiente virtual já está criado e encontra-se em .venv/Scripts/

Após ativar o ambiente virtual, utilize a classe main.py para iniciar o scraping.
Exemplo: python main.py

Aguarde realizar o processo de coleta de informações e download dos arquivos PDF.

=====================================================================================================================

Obs.: Caso queira gerar os arquivos json de forma distintas (apenas os arquivos duplicados, ou todos os arquivos),
pode-se utilizar o comando python gerar_json.py S, ou python gerar_json.py N. O segundo parâmetro refere-se a geração
de arquivos duplicados, N para NÃO gerar arquivos duplicados e S para gerar todos os arquivos, incluindo os duplicados.