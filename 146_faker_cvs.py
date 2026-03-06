import csv
import random
from faker import Faker
from datetime import datetime

# Inicializa o Faker para gerar dados em português do Brasil
fake = Faker('pt_BR')

# Defina a quantidade total de pessoas e compras que deseja gerar
quantidade_pessoas = 2 # 1 milhão de pessoas
quantidade_compras_por_pessoa = (50, 300)  # Compras entre 1 e 10 por pessoa

# Nome do arquivo CSV
nome_arquivo = 'catoes.csv'

# Campos que estarão no CSV
campos = ['id_pessoa', 'nome', 'cpf', 'data_nascimento', 'produto', 'marca', 'categoria', 'valor', 'data_compra', 'loja', 'filial', 'cidade', 'supervisor']

# Lista de produtos, categorias e marcas
produtos_categorias_marcas = {
    'Eletrônicos': [
        ('Notebook', ['Dell', 'HP', 'Lenovo', 'Apple']),
        ('Smartphone', ['Samsung', 'Apple', 'Xiaomi', 'Motorola']),
        ('Monitor', ['LG', 'Samsung', 'Dell', 'AOC'])
    ],
    'Eletrodomésticos': [
        ('Geladeira', ['Brastemp', 'Electrolux', 'Consul']),
        ('Fogão', ['Brastemp', 'Fischer', 'Atlas']),
        ('Microondas', ['Philco', 'Electrolux', 'LG'])
    ],
    'Móveis': [
        ('Cadeira Gamer', ['ThunderX3', 'DXRacer', 'Pichau']),
        ('Mesa de Escritório', ['Movelnorte', 'TecnoMobili', 'Politorno'])
    ],
    'Livros': [
        ('Livro Python', ['Editora Novatec', 'Alta Books']),
        ('Livro Machine Learning', ['O\'Reilly', 'Manning'])
    ],
    'Roupas e Acessórios': [
        ('Tênis', ['Nike', 'Adidas', 'Puma']),
        ('Camisa', ['Zara', 'Hering', 'Riachuelo']),
        ('Relógio', ['Casio', 'Rolex', 'Swatch'])
    ]
}

# Estrutura das lojas, filiais e supervisores
lojas = {
    'Loja A': {
        'supervisor': fake.name(),
        'filiais': {
            'Filial 1': 'São Paulo',
            'Filial 2': 'Rio de Janeiro',
            'Filial 3': 'Curitiba'
        }
    },
    'Loja B': {
        'supervisor': fake.name(),
        'filiais': {
            'Filial 1': 'Belo Horizonte',
            'Filial 2': 'Porto Alegre',
            'Filial 3': 'Brasília'
        }
    },
    'Loja C': {
        'supervisor': fake.name(),
        'filiais': {
            'Filial 1': 'Salvador',
            'Filial 2': 'Fortaleza',
            'Filial 3': 'Recife'
        }
    },
    'Loja D': {
        'supervisor': fake.name(),
        'filiais': {
            'Filial 1': 'Manaus',
            'Filial 2': 'Belém',
            'Filial 3': 'São Luís'
        }
    }
}

# Função para gerar uma data de compra aleatória entre 01/01/2020 e a data atual
def gerar_data_compra():
    data_inicio = datetime(2024, 1, 1)  # Data de início das compras
    data_fim = datetime.now()  # Data atual
    return fake.date_between_dates(date_start=data_inicio, date_end=data_fim).strftime("%d/%m/%Y")

def gerar_data_compra_mes_aleatorio():
    """Gera uma data aleatória entre 01/01/2024 e hoje, distribuindo entre os meses."""
    data_inicio = datetime(2024, 1, 1)
    data_fim = datetime.now()
    return fake.date_between_dates(date_start=data_inicio, date_end=data_fim).strftime("%d/%m/%Y")

# Função para gerar dados de uma pessoa com suas compras
def gerar_compras_pessoa(id_pessoa):
    nome = fake.name()
    cpf = fake.cpf()
    data_nascimento = fake.date_of_birth().strftime("%d/%m/%Y")
    
    numero_compras = random.randint(quantidade_compras_por_pessoa[0], quantidade_compras_por_pessoa[1])

    compras = []
    for _ in range(numero_compras):
        categoria = random.choice(list(produtos_categorias_marcas.keys()))
        produto, marcas = random.choice(produtos_categorias_marcas[categoria])
        marca = random.choice(marcas)
        valor = round(random.uniform(50.0, 5000.0), 2)
        data_compra = gerar_data_compra_mes_aleatorio()
        
        loja_escolhida = random.choice(list(lojas.keys()))
        filial_escolhida, cidade = random.choice(list(lojas[loja_escolhida]['filiais'].items()))
        supervisor = lojas[loja_escolhida]['supervisor']
        
        compras.append({
            'id_pessoa': id_pessoa,
            'nome': nome,
            'cpf': cpf,
            'data_nascimento': data_nascimento,
            'produto': produto,
            'marca': marca,
            'categoria': categoria,
            'valor': valor,
            'data_compra': data_compra,
            'loja': loja_escolhida,
            'filial': filial_escolhida,
            'cidade': cidade,
            'supervisor': supervisor
        })
    
    return compras

# Gera o arquivo CSV em blocos para evitar consumo excessivo de memória
bloco = 100000  # Número de registros a serem processados por vez
with open(nome_arquivo, mode='w', newline='', encoding='utf-8-sig') as arquivo_csv:
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
    escritor_csv.writeheader()  # Escreve o cabeçalho

    id_pessoa = 1
    while id_pessoa <= quantidade_pessoas:
        compras_bloco = []
        for _ in range(bloco):
            if id_pessoa > quantidade_pessoas:
                break
            compras = gerar_compras_pessoa(id_pessoa)
            compras_bloco.extend(compras)
            id_pessoa += 1
        
        # Escreve o bloco de dados no arquivo
        escritor_csv.writerows(compras_bloco)

print(f'Dados de {quantidade_pessoas} pessoas e suas compras foram gerados e salvos no arquivo {nome_arquivo}.')