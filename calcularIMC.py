print("***************************************************")
print("Bem-vindo ao programa para calcular o IMC")
print("***************************************************")

#Função para Calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para classificar o status com base no IMC
def classificar_imc(imc):
    if imc < 15.9:
        return "Magreza grave"
    elif imc < 16.9:
        return "Magreza moderada"
    elif imc < 18.9:
        return "Magreza leve"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Excesso de peso"
    elif imc < 34.9:
        return "Obesidade classe I"
    elif imc < 39.9:
        return "Obesidade classe II"
    elif imc >= 40:
        return "Obesidade classe III"

#Solicitação do nome da pessoa
nome = input("Digite o seu nome: ")

#Solicitação de entrada do peso e altura
peso = float(input(f'{nome}, digite o seu peso em kg: '))
altura = float(input(f'{nome}, agora digite sua altura em metros: '))

# Calcular do IMC
imc = calcular_imc(peso, altura)

#Classificação IMC
indice = classificar_imc(imc)

# Exibição do resultado

print(f'{nome}, o seu IMC é {imc:.2f}')
print(f'Sua classificação segundo a OMS é: {indice}')

print("***************************************************")
print(f'{nome}, obrigado por usar o programa!!')
print("***************************************************")