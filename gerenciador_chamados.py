# Gerenciador de Chamados Internos

# 1. Lista de chamados
chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 3,
        "titulo": "Erro ao acessar o e-mail",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 4,
        "titulo": "Computador muito lento",
        "prioridade": "baixa",
        "situacao": "resolvido",
        "categoria": "hardware"
    },
    {
        "id": 5,
        "titulo": "Instalação de novo software",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "software"
    }
]


# 2. Listagem de todos os chamados
print("========================================")
print("       TODOS OS CHAMADOS")
print("========================================")

for chamado in chamados:
    print(f"ID: {chamado['id']}")
    print(f"Título: {chamado['titulo']}")
    print(f"Prioridade: {chamado['prioridade']}")
    print(f"Situação: {chamado['situacao']}")
    print(f"Categoria: {chamado['categoria']}")
    print("----------------------------------------")


# 3. Filtro por situação
situacao_desejada = "aberto"

print("\n========================================")
print(f"CHAMADOS COM SITUAÇÃO: {situacao_desejada}")
print("========================================")

encontrou_chamado = False

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        encontrou_chamado = True
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Categoria: {chamado['categoria']}")
        print("----------------------------------------")

if not encontrou_chamado:
    print("Nenhum chamado encontrado nessa situação.")


# Teste de uma situação inexistente
situacao_desejada = "cancelado"

print("\n========================================")
print(f"CHAMADOS COM SITUAÇÃO: {situacao_desejada}")
print("========================================")

encontrou_chamado = False

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        encontrou_chamado = True
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print("----------------------------------------")

if not encontrou_chamado:
    print("Nenhum chamado encontrado nessa situação.")


# 4. Atualização da situação por ID
id_desejado = 3
nova_situacao = "resolvido"

print("\n========================================")
print("ATUALIZAÇÃO DE CHAMADO")
print("========================================")

chamado_encontrado = False

for chamado in chamados:
    if chamado["id"] == id_desejado:
        chamado["situacao"] = nova_situacao
        chamado_encontrado = True
        print(f"Chamado {id_desejado} atualizado com sucesso!")
        print(f"Nova situação: {nova_situacao}")
        break

if not chamado_encontrado:
    print("Chamado não encontrado.")


# Teste de ID inexistente
id_desejado = 99
nova_situacao = "em atendimento"

print("\n========================================")
print("TESTE DE ID INEXISTENTE")
print("========================================")

chamado_encontrado = False

for chamado in chamados:
    if chamado["id"] == id_desejado:
        chamado["situacao"] = nova_situacao
        chamado_encontrado = True
        print(f"Chamado {id_desejado} atualizado com sucesso!")
        break

if not chamado_encontrado:
    print("Chamado não encontrado.")


# 5. Categorias sem repetição
categorias = set()

for chamado in chamados:
    categorias.add(chamado["categoria"])

print("\n========================================")
print("       CATEGORIAS DOS CHAMADOS")
print("========================================")

for categoria in categorias:
    print(f"- {categoria}")
