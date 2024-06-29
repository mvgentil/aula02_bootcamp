### Desafio - Refatorar o projeto da aula anterior evitando Bugs!
BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
try:
    nome_usuario = input('Informe seu nome: ')
    if len(nome_usuario) == 0:
        raise ValueError("O nome não pode estar vazio")
        exit()
    elif any(char.isdigit() for char in nome_usuario):
        raise ValueError("O nome não pode conter números.")
    else:
        pass
except ValueError as e:
    print(e)
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_usuario = float(input('Informe seu salario: '))
    if salario_usuario < 0:
        raise ValueError("Informe um valor válido para o salário")
except ValueError as e:
    print("Entrada inválida, digite um valor numérico")
    exit()


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_usuário = float(input('Informe seu bonus: '))
    if bonus_usuário < 0:
        raise ValueError("Informe um valor válido para o bonus")
except ValueError as e:
    print("Entrada inválida, digite um valor numérico")

# 4) Calcule o valor do bônus final
valor_bonus_calculado = BONUS + salario_usuario * bonus_usuário


# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'Olá, {nome_usuario}, seu salário com o bonus será de R${valor_bonus_calculado}')


# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?













