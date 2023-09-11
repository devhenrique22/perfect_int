import requests

# Configurações da Perfect Pay
perfect_pay_api_key = 'sua_api_da_perfect_pay'
perfect_pay_url = 'https://api.perfectpay.com.br/v1/vendas'

# Configurações da Themembers
themembers_api_key = 'sua_chave_de_api_themembers'
themembers_url = 'https://api.themembers.com.br/v1/alunos'

# Dados do aluno e venda
aluno = {
    "nome": "Nome do Aluno",
    "email": "email@exemplo.com",
    # Outros dados do aluno
}

venda_perfect_pay = {
    "produto": "Produto Vendido",
    "valor": 100.00,
    # Outros dados da venda
}

# Função para adicionar aluno à Themembers
def adicionar_aluno_themembers(aluno):
    headers = {
        'Authorization': f'Bearer {themembers_api_key}',
        'Content-Type': 'application/json',
    }
    response = requests.post(themembers_url, json=aluno, headers=headers)
    if response.status_code == 201:
        print(f"Aluno {aluno['nome']} adicionado à Themembers com sucesso!")
    else:
        print(f"Erro ao adicionar aluno à Themembers. Código de status: {response.status_code}")
        print(response.text)

# Simulando uma venda na Perfect Pay (substitua por sua lógica real)
def realizar_venda_perfect_pay(venda):
    # Aqui você faria a chamada para a Perfect Pay para processar a venda
    # Substitua isso pela lógica real de integração com a Perfect Pay
    print(f"Venda do produto {venda['produto']} realizada na Perfect Pay")

# Simulando o processo de identificação da venda
def identificar_venda_perfect_pay(venda):
    # Neste exemplo, vamos considerar que a venda é identificada como sendo da Perfect Pay
    return True

if identificar_venda_perfect_pay(venda_perfect_pay):
    realizar_venda_perfect_pay(venda_perfect_pay)
    adicionar_aluno_themembers(aluno)
else:
    print("Esta venda não foi realizada através da Perfect Pay.")
