tarefas = []

while True:
    print("\n===== MENU DE TAREFAS =====")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar situação de uma tarefa")
    print("4 - Encerrar sistema")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        titulo = input("Digite o título da tarefa: ").strip()
        prioridade = input("Digite a prioridade (baixa, média ou alta): ").strip().lower()

        if titulo == "":
            print("O título não pode estar vazio.")
        elif prioridade not in ["baixa", "média", "alta"]:
            print("Prioridade inválida. Use baixa, média ou alta.")
        else:
            tarefa = {
                "titulo": titulo,
                "prioridade": prioridade,
                "situacao": "pendente"
            }

            tarefas.append(tarefa)
            print("Tarefa cadastrada com sucesso!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Não há tarefas cadastradas.")
        else:
            print("\n===== TAREFAS =====")

            for numero, tarefa in enumerate(tarefas, start=1):
                print(
                    f"{numero} - {tarefa['titulo']} | "
                    f"prioridade: {tarefa['prioridade']} | "
                    f"situação: {tarefa['situacao']}"
                )

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Não há tarefas cadastradas.")
        else:
            numero = input("Digite o número da tarefa que deseja concluir: ").strip()

            if not numero.isdigit():
                print("Digite apenas o número da tarefa.")
            else:
                numero = int(numero)
                indice = numero - 1

                if indice >= 0 and indice < len(tarefas):
                    tarefas[indice]["situacao"] = "concluída"
                    print("Tarefa concluída com sucesso!")
                else:
                    print("Tarefa inexistente.")

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 4.")
