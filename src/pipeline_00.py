import requests
from tinydb import TinyDB
import time

# Extração dos dados

def extract_bitcoin_data():
    url = "https://api.coinbase.com/v2/prices/spot"

    response = requests.get(url)
    data = response.json()
    return data

def transform_bitcoin_data(data):
    valor = data['data']['amount']
    criptomoeda = data['data']['base']
    moeda = data['data']['currency']

    transformed_data = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda
    }
    return transformed_data

def load_bitcoin_data(data, db_name="bitcoin_json"):
    db = TinyDB(db_name)
    db.insert(data)
    print("Carregamento foi concluído com sucesso!")


if __name__ == "__main__":
    data = extract_bitcoin_data()
    transformed_data = transform_bitcoin_data(data)
    load_bitcoin_data(transformed_data)
    time.sleep(20)
