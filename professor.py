import SysPonto
import validacoes
from datetime import datetime

def loginProfessor(cpf, nasc):
	if cpf in SysPonto.professores and SysPonto[cpf][4] == nasc: 
		print ("Professor existente")
		return True
	else:
		return False
	
def menuProf():
	cpf = input("Digite o CPF: ")
	while validacoes.validaCPF(cpf) == False or validacoes.cpfExistenteProfessor(cpf) == False:
		print("CPF inválido.")
		cpf = input("Digite seu CPF: ")
	
	nasc =input("Digite o seu nascimento XX/XX/XXXX: ")
	validacoes.validaData(nasc)
	entrada = '0'
	if loginProfessor(cpf, nasc) == True:
		opcao = input("Digite 1 para entrada ou 2 para saida")
		if opcao == '1':
			cpfEnv = cpf
			dataAt = pegarData()
			entrada = 'Entrada'
		elif opcao == '2':
			cpfEnv = cpf
			dataAt = pegarData()
			entrada = 'Saida'
		else:
			print('Opção inválida')
			
	else:
		menuProf()	
	if entrada != '0'
	SysPonto.Histórico[cpf] = [cpfEnv,dataAt,entrada]
	else:
		menuProf()
			
	
def pegarData():
	now = datetime.now()
	return now
