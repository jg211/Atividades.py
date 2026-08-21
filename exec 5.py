idade = int(input("Digite idade"))
salario_mensal = float(input("Digite salario mensal"))
valor_divida_atual = float(input("Digite valor da divida atual "))
tempo_emprego_mes = int(input("Digite o tempo empregado em meses"))
valor_solicitado = float(input("Digite o valor solicitado"))
num_parcela = int(input("Digite o número de parcelas: "))

compromentimento = valor_divida_atual / salario_mensal
valor_parcela = valor_solicitado / num_parcela

if idade >= 21 and idade <= 65 and salario_mensal >= 2500 and tempo_emprego_mes >= 12 and compromentimento <= 30 and valor_parcela <= 25:
    resultado_analise = "Aprovado"
elif idade >= 21 and idade <= 65 and salario_mensal >= 2500 and tempo_emprego_mes >= 6 and compromentimento + valor_parcela
    resultado_analise = "Aprovada com restrições"
else:
    resultado_analise = "Reprovada"

print(f"Valor da parcela: {valor_parcela}")
print(f"Percentual atual do compromentimento: {compromentimento}")
print(f"Novo percentual do compromento: {}")
print(f"Resultado da análise: {}")
print(f"Motivo principal da aprovação: {}")
