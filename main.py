from tarefa import Tarefa
from servicos import cadastrar_tarefa, listar_tarefas, filtrar_por_situacao


tarefas = []

cadastrar_tarefa(
    tarefas,
    "Revisar chamados",
    "Verificar chamados pendentes da equipe",
    "Alta",
    Tarefa
)

cadastrar_tarefa(
    tarefas,
    "Atualizar manual interno",
    "Ajustar instruções de atendimento",
    "Média",
    Tarefa
)

cadastrar_tarefa(
    tarefas,
    "Planejar reunião",
    "Preparar pauta da reunião semanal",
    "Baixa",
    Tarefa
)

# Concluindo a primeira tarefa
tarefas[0].concluir()

print("=== TODAS AS TAREFAS ===")
listar_tarefas(tarefas)

print("\n=== TAREFAS CONCLUÍDAS ===")
tarefas_concluidas = filtrar_por_situacao(tarefas, "Concluída")
listar_tarefas(tarefas_concluidas)

print("\n=== TAREFAS PENDENTES ===")
tarefas_pendentes = filtrar_por_situacao(tarefas, "Pendente")
listar_tarefas(tarefas_pendentes)