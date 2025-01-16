### README

# Projeto: Pipeline de Coleta e Armazenamento de Dados do Bitcoin

Este projeto implementa um pipeline ETL (Extração, Transformação e Carregamento) para coletar, processar e armazenar dados do preço do Bitcoin em um banco de dados PostgreSQL. Ele utiliza a API da Coinbase para obter os preços em tempo real, transforma os dados para um formato apropriado e os insere em uma tabela no banco de dados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Requests**: Biblioteca para fazer chamadas HTTP.
- **psycopg2**: Biblioteca para interagir com o banco de dados PostgreSQL.
- **dotenv**: Biblioteca para gerenciar variáveis de ambiente.
- **PostgreSQL**: Banco de dados para armazenamento dos dados coletados.
- **Coinbase API**: Fonte dos dados do preço do Bitcoin.

---

## Configuração do Ambiente

Antes de executar o projeto, certifique-se de configurar o ambiente corretamente:

1. **Instale as dependências necessárias**:  
   ```bash
   pip install requests psycopg2 python-dotenv
   ```

2. **Configure as variáveis de ambiente**:  
   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
   ```env
   DB_NAME=nome_do_banco
   DB_USER=usuario
   DB_PASSWORD=senha
   DB_HOST=host_do_banco
   DB_PORT=porta
   ```

3. **Banco de Dados**:  
   Certifique-se de que o banco de dados PostgreSQL está configurado e acessível.

---

## Estrutura do Código

### Funções Principais

- **`extract_bitcoin_data()`**  
  Extrai os dados de preço do Bitcoin usando a API da Coinbase.

- **`transform_bitcoin_data(data)`**  
  Transforma os dados recebidos da API em um formato adequado para o banco de dados, incluindo conversão de tipos e adição de timestamp.

- **`load_bitcoin_postgres(data)`**  
  Carrega os dados transformados em uma tabela do banco de dados PostgreSQL.

- **`create_table()`**  
  Cria a tabela `bitcoin_data` no banco de dados, caso ela ainda não exista.

### Execução

1. **Criação da Tabela**:  
   Ao iniciar, o código verifica ou cria a tabela necessária no banco de dados.

2. **Loop Principal**:  
   O programa executa continuamente o processo de extração, transformação e carregamento (ETL) a cada 12 segundos. Pode ser interrompido manualmente pressionando `Ctrl+C`.

---

## Uso

1. **Inicie o programa**:  
   Execute o script principal:
   ```bash
   python script.py
   ```

2. **Monitore a execução**:  
   O script exibirá logs informando sobre o progresso, como:
   - Criação/verificação da tabela.
   - Sucesso no carregamento de dados.
   - Erros em caso de falhas.

3. **Interrompa a execução**:  
   Para encerrar, pressione `Ctrl+C`.

---

## Estrutura da Tabela

A tabela no banco de dados PostgreSQL terá a seguinte estrutura:

| Coluna         | Tipo       | Descrição                |
|----------------|------------|--------------------------|
| `id`           | SERIAL     | Identificador único      |
| `valor`        | NUMERIC    | Preço do Bitcoin         |
| `criptomoeda`  | VARCHAR(10)| Código da criptomoeda    |
| `moeda`        | VARCHAR(10)| Moeda de referência      |
| `timestamp`    | TIMESTAMP  | Data e hora da coleta    |

---

## Observações

- Certifique-se de que a API da Coinbase está disponível e acessível.
- Ajuste o intervalo de tempo (`time.sleep`) conforme necessário.
- Garanta que as variáveis de ambiente estejam corretamente configuradas.

---

## Contribuição

Contribuições são bem-vindas! Para sugerir melhorias ou corrigir problemas, crie uma issue ou envie um pull request.

---

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
