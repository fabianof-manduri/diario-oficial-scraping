import pyodbc
class Conexao():
    def __init__(self, database, usuario, senha, servidor):
        self.usuario = usuario
        self.database = database
        self.senha = senha
        self.servidor = servidor
        # self.conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
        #                       'Server=JL-Fabiano;'
        #                       'Database=diario_oficial;'
        #                       'Trusted_connection=yes;')

        self.conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                      f'Server={self.servidor};'
                                      f'Database={self.database};'
                                      f'Trusted_connection=yes;')
        self.cur = self.conexao.cursor()

    def Inserir(self, edicao, titulo, conteudo, data_publicacao, nome_arquivo_download):
        # conexao = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};'
        #                          'SERVER=localhost;'
        #                          'DATABASE=diario_oficial;'
        #                          'UID=JL-FABIANO;'
        #                          'PWD=')

        # conexao = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server Native Client 11.0}',
        #               server = 'localhost', database = 'diario_oficial')

        query = f"INSERT INTO diario_informacoes(edicao, titulo, conteudo, data_publicacao, nome_arquivo_download) VALUES (?,?,?,?,?)"

        self.cur.execute(query, (edicao, titulo, conteudo, data_publicacao, nome_arquivo_download))
        self.cur.commit()

    def Deletar_Registro(self):
        query = 'DELETE FROM diario_informacoes'
        self.cur.execute(query)
        self.cur.commit()


if __name__ == '__main__':
    Conexao('diario_oficial', 'JL-Fabiano', '', 'JL-Fabiano')