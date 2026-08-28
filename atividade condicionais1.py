idade = int(input("Digite idade: "))
salario_mensal = float(input("Digite salário mensal: "))
valor_divida_atual = float(input("Digite valor da divida atual: "))
tempo_emprego_mes = int(input("Digite o tempo empregado em meses: "))
valor_solicitado = float(input("Digite o valor solicitado: "))
num_parcela = int(input("Digite o número de parcelas: "))

compromentimento = valor_divida_atual / salario_mensal
valor_parcela = valor_solicitado / num_parcela
compromentimento_nova_parcela = valor_parcela / salario_mensal
compromentimento_total = compromentimento + compromentimento_nova_parcela

resultado = ""
motivo_reprovacao = ""

if idade >= 21 and idade <= 65 and salario_mensal >= 2500 and tempo_emprego_mes >= 12 and compromentimento <= 0.30 and valor_parcela <= 0.25:
    resultado = "Aprovado"
    motivo_reprovacao = ""

elif idade >= 21 and idade <= 65 and salario_mensal >= 2500 and tempo_emprego_mes >= 6 and compromentimento + valor_parcela:
    resultado = "Aprovada com restrições"
    motivo_reprovacao = ""

else:
    resultado = "Reprovada"
    motivo_reprovacao = ""

    if idade < 21 or idade > 65:
        motivo = "Idade fora da faixa permitida (21 a 65)."
    elif salario < 2500:
        motivo_reprovacao = "Salário inferior a R$ 2.500,00."
    elif tempo_emprego_mes < 6:
         motivo  = "Tempo de emprego insuficiente (mínimo de 6 meses)."
    elif compromentimento_total > 0.50:
        motivo_reprovacao = "Compromentimento total da renda superior a 50%."
    else:
        motivo_reprovacao = "Perfil de risco inadequado para os critérios do banco."

print(f"Valor da parcela: {valor_parcela:.2f}")
print(f"Percentual atual do compromentimento: {compromentimento * 100:.2f}")
print(f"Novo percentual do compromento: {compromentimento_total * 100:.2f}")
print(f"Resultado da análise: {resultado}")

if resultado == "Reprovada":
    print(f"Motivo principal: {motivo}")
