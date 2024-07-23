import diario
import sys

class Principal():
    def __init__(self, url, paginas, segundo_plano_visivel):
        self.url = url
        self.segundo_plano_visivel = segundo_plano_visivel
        self.paginas = paginas
        diario.DiarioOficial(self.url, self.paginas, self.segundo_plano_visivel)

if __name__ == '__main__':
    ultima_pagina = 106

    if len(sys.argv) == 2:
        if sys.argv[1].upper() == 'S':
            segundo_plano_visivel = 'S'
            Principal('https://diariooficialnovo.jelastic.saveincloud.net/paginas/public/diario_externo.xhtml?idCidade=69', paginas=ultima_pagina, segundo_plano_visivel=segundo_plano_visivel)

        else:
            segundo_plano_visivel = 'N'
            Principal('https://diariooficialnovo.jelastic.saveincloud.net/paginas/public/diario_externo.xhtml?idCidade=69', paginas=ultima_pagina, segundo_plano_visivel=segundo_plano_visivel)
    else:
        Principal('https://diariooficialnovo.jelastic.saveincloud.net/paginas/public/diario_externo.xhtml?idCidade=69', paginas=ultima_pagina, segundo_plano_visivel='N')
