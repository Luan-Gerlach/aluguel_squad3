import pandas as pd


class DataSetLimpeza:

    def __init__(self, caminho_arquivo):

        self.caminho_arquivo = caminho_arquivo

        self.dados_brutos = None

        self.dados_processados = None



    def carregar(self):

        self.dados_brutos = pd.read_csv(self.caminho_arquivo)

        tipos_colunas = {

            'id': str,

            'descricao': str,

            'tipo': str,

            'endereco': str,

            'rua': str,

            'numero': str,

            'bairro': str,

            'cidade': str,

            'valor': float,

            'condominio': float,

            'area': float,

            'qtd_banheiros': float,

            'qtd_quartos': float,

            'qtd_vagas': float,

            'valor_total': float,

            'valor_m2': float

        }

        for coluna, tipo in tipos_colunas.items():

            if coluna in self.dados_brutos.columns:

                self.dados_brutos[coluna] = self.dados_brutos[coluna].astype(tipo)



    def processar(self):

        colunas_necessarias = [

            'id', 'descricao', 'tipo', 'endereco', 'rua', 'numero', 'bairro', 'cidade',

            'valor', 'condominio', 'area', 'qtd_banheiros', 'qtd_quartos', 'qtd_vagas',

            'valor_total', 'valor_m2'

        ]

        self.dados_brutos.columns = [col.strip().lower() for col in self.dados_brutos.columns]

        self.dados_processados = self.dados_brutos[[col for col in colunas_necessarias if col in self.dados_brutos.columns]]



    def get_dataset_limpo(self):

        return self.dados_processados



# Exemplo de uso

if __name__ == "__main__":

    dataset = DataSetLimpeza('aluguel.csv')

    dataset.carregar()

    dataset.processar()

    dataset_limpo = dataset.get_dataset_limpo()

    print(dataset_limpo.head())
 