salario_mensal = float(input("Digite o seu salario mensal:"))
horas_trabalhadas = float(input("Digite o total de horas que você trabalhou:"))

cal_hora = horas_trabalhadas * 4
cal_salario = salario_mensal / cal_hora

print(f"Este é o seu salario calculado por hora{cal_salario}R$")