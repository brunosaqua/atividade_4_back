














Gerenciador de Chamados Internos
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

Nome: Seu Nome

Dupla: Nome do integrante da dupla, se houver

:::

## 3. Como testar

Na pasta onde estão os arquivos, rode:

```bash
python gerenciador_chamados.py


O programa já testa os principais requisitos:

5 chamados cadastrados;
Listagem de todos;
Filtro por "aberto", que possui resultados;
Filtro por "cancelado", que não possui resultados;
Atualização do chamado de ID 3 para "resolvido";
Teste do ID 99, que não existe;
Uso de set() para mostrar categorias sem repetição.
Para entregar no GitHub

Sua estrutura pode ficar assim:

seu-repositorio/
│
├── gerenciador_chamados.py
└── README.md


Depois, no Git:

git add gerenciador_chamados.py README.md
git commit -m "Adiciona gerenciador de chamados"
git push


Se você estiver fazendo essa atividade em uma branch específica, posso também te passar exatamente os comandos para criar a branch, colocar esses dois arquivos e enviar para o GitHub.
