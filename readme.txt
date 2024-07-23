====================================================================================================================
PROBLEMÁTICA
=====================================================================================================================
Foi constatado a necessidade de realizar a importação dos arquivos e informações enviadas ao diário oficial de Riversul. No entanto ocorreu a problemática em que nossa equipe não tinha acesso ao banco de dados da empresa cedida. Devido a isso, foi necessário realizar um webscraping.
Pois bem, realizei um webscraping em Python, onde o mesmo realiza a ação de entrar no endereço www.teste.com e realizar a leitura de informações pertinentes realizando uma varredura em todas as páginas. (página a página).
Obtém o link do arquivo de cada publicação, com as informações da publicação, tais como número, título, conteúdo e data de publicação, nosso robô realiza download dos arquivos em PDF, posteriormente armazena as informações citadas acima em um banco instanciado nas dependências do SQL Server.
No momento em que é realizada a leitura/download é gerado um json com as informações coletadas.
Obs.: O robô realiza a coleta de informações (top-down), de cima a baixo em todas as páginas.
Obs2.: É possível executar o robô após a primeira execução para listar apenas as publicações que estão com o número divergente, ou seja, possuem publicações repetidas. (possivelmente são publicações extra oficiais realizadas posteriores a publicação oficial)

=====================================================================================================================
||            #FORMAS DE UTILIZAÇÃO
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
