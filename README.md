Atividade prática — Protótipo de
cadastro de tarefa em terminal
Cenário de mercado
Uma empresa de desenvolvimento de software deseja validar o cadastro básico de tarefas
para um sistema interno. Antes de investir em interface web e banco de dados, a equipe
precisa de um protótipo de terminal que receba informações essenciais e gere um resumo
padronizado.
Você atuará como pessoa desenvolvedora back end responsável por implementar esse
primeiro experimento técnico.

# Menu de Tarefas para uma Equipe de Serviços

## Descrição

Programa desenvolvido em Python para funcionar no terminal e permitir o cadastro, consulta e atualização de tarefas de uma equipe de serviços.

O projeto foi desenvolvido como atividade prática com o objetivo de utilizar estruturas de decisão, validações e repetições em Python.

## Como executar

É necessário ter o Python instalado no computador.

No terminal, entre na pasta onde está o arquivo `menu_tarefas.py` e execute:

```bash
python menu_tarefas.py
```

Em alguns computadores com Windows, pode ser necessário utilizar:

```bash
py menu_tarefas.py
```

## Opções disponíveis

### 1 - Cadastrar tarefa

Permite cadastrar uma nova tarefa informando:

* Título
* Prioridade

As prioridades aceitas são:

* baixa
* média
* alta

Toda tarefa cadastrada recebe automaticamente a situação:

`pendente`

### 2 - Listar tarefas

Exibe todas as tarefas cadastradas, mostrando:

* Número
* Título
* Prioridade
* Situação

### 3 - Atualizar situação de uma tarefa

Permite selecionar uma tarefa pelo número e alterar sua situação para:

`concluída`

Caso o número informado não corresponda a uma tarefa existente, o programa informa:

`Tarefa inexistente.`

### 4 - Encerrar sistema

Encerra a execução do programa.

## Validações

O programa verifica:

* Título vazio;
* Prioridade diferente de baixa, média ou alta;
* Número inválido na atualização;
* Tarefa inexistente;
* Opção inválida no menu.

## Estruturas utilizadas

O projeto utiliza:

* `while` para manter o menu funcionando até o encerramento;
* `if`, `elif` e `else` para controlar as opções;
* `for` para percorrer e listar as tarefas;
* `list` para armazenar as tarefas temporariamente;
* `dict` para representar cada tarefa.

## Limitações

Os dados ficam armazenados somente na memória durante a execução do programa.

Ao escolher a opção 4 e encerrar o sistema, todas as tarefas cadastradas são perdidas.

O programa não utiliza banco de dados, servidor ou framework web.

## Exemplo

```text
===== MENU DE TAREFAS =====
1 - Cadastrar tarefa
2 - Listar tarefas
3 - Atualizar situação de uma tarefa
4 - Encerrar sistema

Escolha uma opção: 1

Digite o título da tarefa: Revisar relatório
Digite a prioridade (baixa, média ou alta): alta

Tarefa cadastrada com sucesso!
```

## Commit

Exemplo de mensagem de commit:

```bash
git add menu_tarefas.py README.md
git commit -m "feat: implementa menu de tarefas"
git push
```
