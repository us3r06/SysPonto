import smtplib
import os
import re
from datetime import datetime
from datetime import date
import sys

def cpfExistenteProfessor(cpf):
	if cpf in professores:
		print ("CPF já cadastrado")
		return False
	else:
		return True
	

def cpfExistenteDiretor(cpf):
	if cpf in Diretores:
		print ("CPF já cadastrado")
		return False
	else:
		return True

def validaUF(a):
	a = a.upper()
	estados = {'AC':[],'AL':[],'AM':[],'AP':[],'BA':[],'CE':[],'DF':[],'ES':[],'GO':[],'MA':[],'MG':[],'MS':[],'MT':[],'PA':[],'PB':[],'PE':[],'PI':[],'PR':[],'RJ':[],'RO':[],'RN':[],'RR':[],'RS':[],'SE':[],'SC':[],'SP':[],'TO':[]}
	if  a in estados:
		return True	
	else:
		return False


def validaCPF(cpf):
	if len(cpf) != 11:
		return False
	cpf = list(cpf)
	for i in range(len(cpf)):
		cpf[i] = int(cpf[i])
	mult = [10,9,8,7,6,5,4,3,2]
	mult2 = [11,10,9,8,7,6,5,4,3,2]
	soma = 0
	for i in range(len(mult)): 
		soma += cpf[i] * mult[i]
	d1 = 11 - (soma % 11)
	if d1 == 10 or d1 == 11:
		d1 = 0
	soma1 = 0
	for a in range(len(mult2)):
		soma1 += cpf[a] * mult2[a]
	d2 = 11 - (soma1 % 11)	
	if d2 == 10 or d2 == 11:
		d2 = 0
	if d1 == cpf[9] and d2 == cpf[10]:
		return True
	else:
		return False

def validafone(fone):
	if not fone.isdigit():
		return False
	if len(fone) == 9 or len(fone) == 10 or len(fone) ==11 or len(fone) == 8:
		return True
	else:
		return False

def validaemail(email):
	if len(email) <= 5:
		return False
	else:
		if not '@'  in email:
			return False
		else:
			if not email.endswith('.com') :
				return False
			else:
				return True

def validaData(d):
	while bool(re.match('(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012]/[12][0-9]{3})', d)) is False:
		d = input("Data inválida!\nDigite uma data válida no formato (xx/xx/xxxx): ") 	


def centralizar(a):
	print(" "+a.center(70)+" ")

def menuLogin():
	menu = "Login"
	escolha = "Escolha a opção de Login na qual vc está cadastrado"
	a = "1-Professor"
	b = "2-Diretor"
	c = "3-DIRED central"
	d = "4-Cadastrar Usuário"
	e = "0-Sair"
	centralizar(menu)
	centralizar(escolha)
	centralizar(a)
	centralizar(b)
	centralizar(c)
	centralizar(d)
	centralizar(e)

def grava_professor():
    conteudo = ''
    with open('professores.txt', 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in professores:
            for k in range(len(professores[i])):
                conteudo += str(professores[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()

def grava_diretor():
    conteudo = ''
    with open('diretores.txt', 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in Diretores:
            for k in range(len(Diretores[i])):
                conteudo += str(Diretores[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()

def grava_dired():
    conteudo = ''
    with open('direds.txt', 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in direds:
            for k in range(len(direds[i])):
                conteudo += str(direds[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()

def grava_historico():
    conteudo = ''
    with open('historico.txt', 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in Historico:
            for k in range(len(Historico[i])):
                conteudo += str(Historico[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()

def grava_historicoDired():
    conteudo = ''
    with open('historicoDired.txt', 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in historicoDired:
            for k in range(len(historicoDired[i])):
                conteudo += str(historicoDired[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()



def execute():
	while True:
		menuLogin()
		opcaoLogin = input("Digite a opção desejada: ")
		if opcaoLogin.strip() == '0':
			print("Obrigado por usar o SysPonto")
			sys.exit()
		elif opcaoLogin.strip() == '1':
			menuProf()
		elif opcaoLogin.strip() == '2':
			menuDiretor()
		elif opcaoLogin.strip() == '3':
			menuDired()
		elif opcaoLogin.strip() == '4':
			executeCadastros()
		else:
			print(opcaoLogin, "não é uma opção válida!\n")

def cadastraProfessor():
	nome =input("Digite o seu nome: ")
	cpf = input("Digite o CPF: ")
	while validaCPF(cpf) == False or cpfExistenteProfessor(cpf) == False:
		print("CPF inválido.")
		cpf = input("Digite seu CPF: ")
	fone =input("Digite o seu celular = xxxxxxxxxxx ")
	while validafone(fone) == False:
		fone =input("Digite o seu celular = xxxxxxxxxxx ")
		fone.split(' ')
		validafone(fone)
	
	email =input("Digite o seu email: ")
	while validaemail(email) == False:
		email =input("Email inexistente \nDigite o seu email: ")
	nasc =input("Digite o seu nascimento XX/XX/XXXX: ")
	validaData(nasc)
	cidade =input("Digite a sua cidade: ")
	estado =input("Digite o seu estado (Sigla): ")
	while validaUF(estado) == False:
		estado = input("Estado Inválido.\nDigite o seu estado: ")
	nome= nome
	professores[cpf] = [nome,fone,cpf,email,nasc,cidade,estado]
	grava_professor()
	print("Professor cadastrado com sucesso")
	os.system ("clear")
	
def cadastraDiretor():
	nome =input("Digite o seu nome: ")
	cpf = input("Digite o CPF: ")
	while validaCPF(cpf) == False or cpfExistenteDiretor(cpf) == False:
		print("CPF inválido.")
		cpf = input("Digite seu CPF: ")
	fone =input("Digite o seu celular = xxxxxxxxxxx ")
	while validafone(fone) == False:
		fone =input("Digite o seu celular = xxxxxxxxxxx ")
		fone.split(' ')
		validafone(fone)
	
	email =input("Digite o seu email: ")
	while validaemail(email) == False:
		email =input("Email inexistente \nDigite o seu email: ")
	nasc =input("Digite o seu nascimento XX/XX/XXXX: ")
	validaData(nasc)
	cidade =input("Digite a sua cidade: ")
	nmrDired = input("Digite o número da DIRED a qual sua escola pertence: ")
	nome= nome
	Diretores[cpf] = [nome,fone,cpf,email,nasc,cidade,nmrDired]
	grava_diretor()
	print("Diretor cadastrado com sucesso")
	os.system ("clear")

def cadastraDired():
	cod =input("Digite o Código da DIRED: ")
	fone = input("Digite o seu celular = xxxxxxxxxxx ")
	while validafone(fone) == False:
		fone = input("Digite o seu celular = xxxxxxxxxxx ")
		fone.split(' ')
		validafone(fone)
	
	email =input("Digite o seu email: ")
	while validaemail(email) == False:
		email =input("Email inexistente \nDigite o seu email: ")
	cidade =input("Digite a sua cidade: ")
	direds[cod] = [cod,fone,email,cidade]
	grava_dired()
	print("DIRED cadastrada com sucesso")
	os.system ("clear")


def menuCadastros():
	
	menu = "opções de Cadastros"
	escolha = "Escolha a opção desejada"
	a = "1-Cadastrar Professor"
	b = "2-Cadastrar Diretor"
	c = "3-Cadastrar DIRED"
	e = "0-Sair"
	centralizar(menu)
	centralizar(escolha)
	centralizar(a)
	centralizar(b)
	centralizar(c)
	centralizar(e)

def executeCadastros():
	while True:
		menuCadastros()
		opcaoLogin = input("Digite a opção desejada: ")
		if opcaoLogin.strip() == '0':
			print("Obrigado por usar o SysPonto")
			sys.exit()
		elif opcaoLogin.strip() == '1':
			cadastraProfessor()
		elif opcaoLogin.strip() == '2':
			cadastraDiretor()
		elif opcaoLogin.strip() == '3':
			cadastraDired()
		else:
			print(opcaoLogin, "não é uma opção válida!\n")


def recuperar_professor():
    with open('professores.txt', 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            professores[read[2]] = read[:]
            
def recuperar_diretor():
    with open('diretores.txt', 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            Diretores[read[2]] = read[:]

def recuperar_dired():
    with open('direds.txt', 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            direds[read[2]] = read[:]

def recuperar_historico():
    with open('historico.txt', 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            Historico[read[2]] = read[:]

def recuperar_historicoDired():
    with open('historicoDired.txt', 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            historicoDired[read[2]] = read[:]

def loginProfessor(cpf, nasc):
	if cpf in professores and professores[cpf][4] == nasc: 
		print ("Professor existente")
		return True
	else:
		return False

def loginDiretor(cpf, nasc):
	if cpf in Diretores and Diretores[cpf][4] == nasc: 
		print ("Diretor existente")
		return True
	else:
		return False
	
def menuProf():
	print("-->Cadastrar ponto<--")
	cpf = input("Digite o CPF: ")
	while validaCPF(cpf) == False or cpfExistenteProfessor(cpf) == True:
		print("CPF inválido.")
		cpf = input("Digite seu CPF: ")
	
	nasc =input("Digite o seu nascimento XX/XX/XXXX: ")
	validaData(nasc)
	entrada = '0'
	if loginProfessor(cpf, nasc) == True:
		opcao = input("Digite 1 para entrada ou 2 para saida: ")
		if opcao == '1':
			cpfEnv = cpf
			dataAt = pegarData()
			entrada = 'Entrada'
			Historico[cpf] = [cpfEnv,dataAt,entrada]
			grava_historico()
		elif opcao == '2':
			cpfEnv = cpf
			dataAt = pegarData()
			entrada = 'Saida'
			Historico[cpf] = [cpfEnv,dataAt,entrada]
			grava_historico()
		else:
			print('Opção inválida')
			
	else:
		menuProf()	

def mostraHistorico(Historico):
	for i in Historico:
		print("CPF do Professor: ", Historico[i][0], "Data: ", Historico[i][1], "Entrada: ", Historico[i][2])


def menuDiretor():
	print("-->Visualiza Histórico<--")
	cpf = input("Digite o CPF: ")
	while validaCPF(cpf) == False or cpfExistenteDiretor(cpf) == True:
		print("CPF inválido.")
		cpf = input("Digite seu CPF: ")
	
	nasc =input("Digite o seu nascimento XX/XX/XXXX: ")
	validaData(nasc)
	entrada = '0'
	if loginDiretor(cpf, nasc) == True:
		mostraHistorico(Historico)	
	opcao = input("Digite qualquer coisa para anviar o histórico para a Dired")
	if opcao != '0040943034034784':
		 HistoricoDired = Historico
		 grava_historicoDired()
	else:
		menuDired()			
	
def pegarData():
	now = datetime.now()
	return now


professores = {} 
Diretores = {}
direds = {}
Historico={}
historicoDired={}
recuperar_professor()
recuperar_diretor()
recuperar_dired()
recuperar_historico()
recuperar_historicoDired()
execute()

