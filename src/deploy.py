# Exportar para o Google BigQuery usando pandas_gbq
from pandas_gbq import to_gbq

# Definindo o nome do projeto e a tabela de destino
projeto_id = 'agentspace-trial-na'
nome_tabela = 'agent_space_data_1p.Aluguel_Squad3'

# Exporte o DataFrame limpo para o BigQuery
to_gbq(dataset_limpo, nome_tabela, project_id=projeto_id, if_exists='replace')