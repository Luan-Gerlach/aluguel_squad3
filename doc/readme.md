# 🏠 Integração Agentspace com Google BigQuery para Dados de Casas para Aluguel

## 🔍 Visão Geral

Este projeto é uma aplicação em Python que integra dados de casas para aluguel, extraídos de um arquivo CSV, com o **Google BigQuery**. O código realiza o tratamento dos dados e faz o upload direto para uma tabela no BigQuery, facilitando a análise e manipulação dos dados imobiliários pelo Agentspace.

## 🎯 Caso de Uso

- 📥 Importar dados tabulares de imóveis para aluguel armazenados em CSV.  
- 🧹 Fazer o pré-processamento necessário (limpeza, formatação, validação).  
- 🚀 Enviar os dados tratados para uma tabela específica no BigQuery.  
- 🔗 Consultar esses dados no Agentspace.

## ⚙️ Como Funciona

1. 📄 O script Python lê os dados de um arquivo CSV local.  
2. 🔄 Aplica as transformações necessárias para garantir a qualidade dos dados.  
3. ☁️ Envia os dados para uma tabela no Google BigQuery usando a API oficial do Google Cloud.  
4. 🤖 O Agentspace consulta os dados no BigQuery por meio de uma conexão via datastore.

## 📋 Requisitos

- 🟦 Conta Google Cloud com permissão para acessar o BigQuery.  
- 🔑 Credenciais de autenticação.  
- 📊 Dataset.  
- 🐍 Python instalado.  
- 📚 Bibliotecas Python: `pandas`, `google-cloud-bigquery`  
- 🤝 Google Agentspace.

## 📊 Tabela do BigQuery  
![Tabela](/tabela_bigQuery.png)

## 🎉 Resultado  
![Resultado](/resultado.png)
