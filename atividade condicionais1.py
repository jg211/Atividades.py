idade = int(input("Digite idade: "))
salario_mensal = float(input("Digite salário mensal: R$ "))
valor_divida_atual = float(input("Digite valor da dívida atual: R$ "))
tempo_emprego_mes = int(input("Digite o tempo empregado em meses: "))
valor_solicitado = float(input("Digite o valor solicitado: R$ "))
num_parcela = int(input("Digite o número de parcelas: "))

comprometimento_atual = valor_divida_atual / salario_mensal
valor_parcela = valor_solicitado / num_parcela
comprometimento_nova_parcela = valor_parcela / salario_mensal
comprometimento_total = comprometimento_atual + comprometimento_nova_parcela

resultado = ""
motivo_reprovacao = ""

if 21 <= idade <= 65 and salario_mensal >= 2500 and tempo_emprego_mes >= 12 and comprometimento_atual <= 0.30 and comprometimento_nova_parcela <= 0.25:
    resultado = "Aprovado"

elif 21 <= idade <= 65 and salario_mensal >= 2500 and tempo_emprego_mes >= 6 and comprometimento_total <= 0.50:
    resultado = "Aprovada com restrições"

else:
    resultado = "Reprovada"

    if idade < 21 or idade > 65:
        motivo_reprovacao = "Idade fora da faixa permitida (21 a 65)."
    elif salario_mensal < 2500:
        motivo_reprovacao = "Salário inferior a R$ 2.500,00."
    elif tempo_emprego_mes < 6:
        motivo_reprovacao = "Tempo de emprego insuficiente (mínimo de 6 meses)."
    elif comprometimento_total > 0.50:
        motivo_reprovacao = "Comprometimento total da renda superior a 50%."
    else:
        motivo_reprovacao = "Perfil de risco inadequado para os critérios do banco."

print(f"\nValor da parcela: R$ {valor_parcela:.2f}")
print(f"Percentual atual do comprometimento: {comprometimento_atual * 100:.2f}%")
print(f"Percentual da nova parcela: {comprometimento_nova_parcela * 100:.2f}%")
print(f"Comprometimento total: {comprometimento_total * 100:.2f}%")
print(f"Resultado da análise: {resultado}")

if resultado == "Reprovada":
    print(f"Motivo principal: {motivo_reprovacao}")
