vendas = [1200.0, 850.0, 2300.0, 450.0, 1800.0, 3200.0, 950.0]
total_itens = len(vendas)
total_vendas = sum(vendas)
media_vendas = total_vendas / total_itens
maior_vendas = max(vendas)
menor_vendas = min(vendas)
acima_media = []

for venda in vendas:
    if venda > media_vendas:
        acima_media.append(venda)
print(f"Quantidade: {total_itens}")
print(f"Total: {total_vendas}")
print(f"Média: {media_vendas}")
print(f"Maior: {maior_vendas}")
print(f"Menor: {menor_vendas})
print(f"Acima da média: {acima_media}")
print(acima_media)
