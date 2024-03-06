# Divisão 

num3 = float(input("Entre com o dividendo para divisao:"))
num4 = float(input("Entre com o divisor para divisão:"))
if num4 == 0:
    print("Erro: Divisão por zero não pode.")
else:
    div_result = num3 / num4
    print(f"Divisão: {num3} / {num4} = {div_result}")
    