tipos_atendimentos = ["N = Normal", "P = Prefencial"]
print(tipos_atendimentos)
fila = ["N001", "N002", "P001"]
print(f"Painel")
print(f"Senha sendo chamada: {fila[0]}")
fila.pop(0)

print(f"Retirar nova senha")
fila.append("N003")

for posicao, senha in enumerate(fila, start=1):
    print(f"{posicao}.{senha}")
