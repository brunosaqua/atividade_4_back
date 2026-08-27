(1) Relatório — Sistema de Gestão de Tarefas
Objetivo
Criar a estrutura inicial de um projeto Python utilizando ambiente virtual e Git.

Atividades realizadas
Criada a pasta sistema-tarefas.
Criado e executado o arquivo main.py.
Criado o ambiente virtual .venv.
Instalada a dependência requests.
Criado o requirements.txt.
Criado o .gitignore para ignorar .venv/.
Criado o README.md.
Inicializado o Git.
Criado o primeiro commit.
Resultado
O projeto foi configurado e testado com sucesso, ficando pronto para futuras implementações.

(2) Relatório — Cadastro de Tarefa
Atualização

Foi desenvolvido o programa cadastro_tarefa.py para realizar o cadastro básico de uma tarefa pelo terminal.

Implementado
Entrada de título, prioridade, prazo e urgência;
Conversão de dados com int() e float();
Cálculo do esforço estimado;
Comparação da prioridade;
Identificação de tarefa prioritária;
Resumo das informações utilizando f-strings;
Testes com diferentes cenários.
Status

Atividade implementada, executada e registrada no repositório.

(3) Relatório — Menu de Tarefas
Atualização

Foi desenvolvido o programa menu_tarefas.py para gerenciamento de tarefas pelo terminal.

Implementado
Menu interativo com while;
Cadastro de tarefas;
Validação de título e prioridade;
Listagem das tarefas com for;
Atualização da situação para concluída;
Tratamento de tarefas inexistentes;
Tratamento de opções inválidas;
Opção para encerrar o sistema.
Status

Atividade atualizada e testada conforme os requisitos propostos.

(4) Gerenciador de Chamados Internos
Objetivo

O programa tem como objetivo gerenciar chamados internos de uma empresa utilizando Python.

Os chamados são armazenados em uma lista de dicionários e possuem as seguintes informações:

ID
Título
Prioridade
Situação
Categoria

O programa permite:

Listar todos os chamados;
Filtrar chamados por situação;
Informar quando não existem chamados para uma determinada situação;
Atualizar a situação de um chamado pelo ID;
Informar quando um ID não existe;
Exibir as categorias existentes sem repetição utilizando set.
Como executar

No terminal, dentro da pasta do projeto, execute:

python gerenciador_chamados.py


Caso o computador utilize python3:

python3 gerenciador_chamados.py

Exemplo de saída
========================================
       TODOS OS CHAMADOS
========================================
ID: 1
Título: Sem acesso ao sistema interno
Prioridade: alta
Situação: aberto
Categoria: acesso
----------------------------------------

========================================
CHAMADOS COM SITUAÇÃO: aberto
========================================
ID: 1
Título: Sem acesso ao sistema interno
Prioridade: alta
Categoria: acesso
----------------------------------------

========================================
ATUALIZAÇÃO DE CHAMADO
========================================
Chamado 3 atualizado com sucesso!
Nova situação: resolvido

========================================
       CATEGORIAS DOS CHAMADOS
========================================
- acesso
- hardware
- software

Autoria

Nome: Bruno Macedo da Silva


