from playwright.sync_api import sync_playwright
import re
import time
import conexao
from datetime import datetime
import os
import gerar_json

class DiarioOficial():
    def __init__(self, url, paginas, visivel):
        self.url = url
        self.paginas = paginas
        self.visivel = visivel
        self.conexao = conexao.Conexao('diario_oficial','JL-Fabiano', '', 'JL-Fabiano')
        #deletar registros já inseridos
        self.conexao.Deletar_Registro()
        self.LeituraPagina()

    def LeituraPagina(self):
        if self.visivel.upper() == 'S':
            self.visivel = False
        else:
            self.visivel = True

        print('Iniciando BOT.')
        self.chromium = sync_playwright().start().chromium
        self.browser = self.chromium.launch(headless=self.visivel, args=["--start-maximized"])
        self.context = self.browser.new_context()
        self.pagina = self.context.new_page()

        self.pagina.goto(self.url)

        # self.context.set_default_timeout(120000)  # tempo de espera máximo 2min entre cada carregamento

        ultima_publicacao = self.pagina.locator('#formConteudo .ui-panel.ui-widget.ui-widget-content.ui-corner-all').first.inner_text().split('\n')[0]
        publicacoes = re.compile('[0-9]+', flags=re.IGNORECASE)
        ultima_publicacao = publicacoes.findall(ultima_publicacao)[0]
        print(self.pagina.title())
        print('Ultima publicação encontrada:', ultima_publicacao)
        self.LeituraPublicacoes()

    def LeituraPublicacoes(self):
        index_pagina = 1
        num_publicacao_pagina = int(re.compile('[0-9]+', flags=re.IGNORECASE).findall(self.pagina.locator('#formConteudo .ui-panel.ui-widget.ui-widget-content.ui-corner-all').last.inner_text().split('\n')[0])[0])
        while (num_publicacao_pagina >= 1):

            qtd_publicacoes = self.pagina.locator('#formConteudo .ui-panel.ui-widget.ui-widget-content.ui-corner-all').count()
            for index in range(qtd_publicacoes):
                publicacao = self.pagina.locator('#formConteudo .ui-panel.ui-widget.ui-widget-content.ui-corner-all').nth(index).inner_text().split('\n')
                print(publicacao)

                data_publicacao = publicacao[4].replace('Publicado em ', '')
                data_publicacao = datetime.strptime(data_publicacao, '%d/%m/%Y').date()

                edicao = int(re.compile('[0-9]+', flags=re.IGNORECASE).findall(self.pagina.locator('#formConteudo .ui-panel.ui-widget.ui-widget-content.ui-corner-all').nth(index).inner_text().split('\n')[0])[0])

                #realizar download do arquivo:
                self.Download_Arquivo_PDF(index)
                self.conexao.Inserir(edicao, publicacao[0], publicacao[3], data_publicacao, self.nome_arquivo_download)

            index_pagina+=1
            #valida se a última pagina já foi lida e realiza um break para sair do laço de repetição
            if num_publicacao_pagina == 1:
                break

            self.pagina.locator(r"[id='formConteudo\:tb_paginator_top']").get_by_label(f'Page {index_pagina}').click()
            self.pagina.wait_for_load_state(state='domcontentloaded')
            #delay de 1 segundo
            time.sleep(2)
            num_publicacao_pagina = int(re.compile('[0-9]+', flags=re.IGNORECASE).findall(self.pagina.locator('#formConteudo .ui-panel.ui-widget.ui-widget-content.ui-corner-all').last.inner_text().split('\n')[0])[0])

        #Função para gerar o arquivo json, obs.: Se o flag estiver como N, ele vai gerar apenas os arquivos duplicados
        gerar_json.Gerar_Json(gerar_todos_arquivos='S')
        print('Documentos PDF(s) salvos em:', os.getcwd() + r'\documentos')
        self.context.close()
        self.browser.close()

    def Download_Arquivo_PDF(self, indice):
        with self.pagina.expect_download() as download_info:
            # Perform the action that initiates download
            self.pagina.locator('#formConteudo  .ui-button-icon-left.ui-icon.ui-c.fa.fa-cloud-download').nth(indice).click()
        download = download_info.value
        caminho_download = os.getcwd() + r'\documentos'
        caminho_arquivo = os.path.join(caminho_download, download.suggested_filename)
        download.save_as(caminho_arquivo)
        #salva como a sugestão já do site
        self.nome_arquivo_download = download.suggested_filename

