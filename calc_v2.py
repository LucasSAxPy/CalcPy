# Calculadora em Python

# Import time para ativar um delay no tempo de execução
import time
from os import system, name

#Limpa a tela, para cada execução
def limpatela(): 
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

#Função para somar os números
def soma(n1, n2):
	resp = n1 + n2
	print(f'A soma de {n1} + {n2} é: {resp}')

#Função para subtrair os números
def subt(n1, n2):
	resp = n1 - n2
	print(f'A subtração de {n1} - {n2} é: {resp}')

#Função para dividir os números
def divisao(n1, n2):
	try:
		resp = n1 / n2
		print(f'A divisão de {n1} / {n2} é: {resp:.3f}')
	except ZeroDivisionError:
		print('Não efetua divisão por 0')

#Função para multiplicar os números
def mult(n1, n2):
	resp = n1 * n2
	print(f'A multiplicação de {n1} x {n2} é: {resp:.3f}')

#Função para pergar os resultados e realizar as operações
def calculadora():

#Limpa a tela, quando roda o programa
	limpatela()

#Exibi um layout para saber quais são as operações
	print("\n******************* Calculadora em Python *******************")
	print("\n 1 - Soma \n 2 - Subtração \n 3 - Divisão(1°número/2°número) \n 4 - Multiplicação \n")


# Armazena qual operação realizar e quais os valores que seram usados para este
# Somente válido se for digitado um número
	while True:
		try:
			x1 = int(input('Qual operação será realizada? '))
			time.sleep(0.4)
			num1 = float(input('Digite o primeiro número: '))
			time.sleep(0.4)
			num2 = float(input('Digite o segundo número: '))
		except:
			print('Não foi digitado um número!')
			continue
		else:
			break

# Condicional para escolha da operação do usuário
	if x1 == 1:
		soma(num1, num2)
	elif x1 == 2:
		subt(num1, num2)
	elif x1 == 3:
		divisao(num1, num2)
	elif x1 == 4:
		mult(num1, num2)
	else:
		print('Operação inválida!')

# Bloco main, inicia a calculadora e perguta se quer continuar
if __name__ == "__main__":
	var = 'sim'
	while var == 'sim':
		calculadora()
		time.sleep(1.1)
		var = input('Quer continuar?(sim/nao)')
	
print("\n **********Operação Finalizada**********")