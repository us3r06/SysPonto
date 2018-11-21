import validacoes
import SysPonto
def centralizar(a):
	print(" "+a.center(70)+" ")
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
			cadastraDiretor
		elif opcaoLogin.strip() == '3':
			cadastraDired()
		else:
			print(opcaoLogin, "não é uma opção válida!\n")
def cadastraProfessor():
	nome =input("Digite o seu nome: ")
	cpf = input("Digite o CPF: ")
	while validacoes.validaCPF(cpf) == False or validacoes.pfExistente(cpf) == False:
		print("CPF inválido.")
		cpf = input("Digite seu CPF: ")
	fone =input("Digite o seu celular = xxxxxxxxxxx ")
	while validacoes.validafone(fone) == False:
		fone =input("Digite o seu celular = xxxxxxxxxxx ")
		fone.split(' ')
	validacoes.validafone(fone)
	
	email =input("Digite o seu email: ")
	while validacoes.validaemail(email) == False:
		email =input("Email inexistente \nDigite o seu email: ")
	nasc =input("Digite o seu nascimento XX/XX/XXXX: ")
	validacoes.validaData(nasc)
	cidade =input("Digite a sua cidade: ")
	estado =input("Digite o seu estado (Sigla): ")
	while validacoes.validaUF(estado) == False:
		estado = input("Estado Inválido.\nDigite o seu estado: ")
	nome= nome
	SysPonto.professores[cpf] = [nome,fone,cpf,email,nasc,cidade,estado]
	grava_clientes()
	print(clientes)
	print("Professor cadastrado com sucesso")
	os.system ("cls")
	
def cadastraDiretor():
	nome =input("Digite o seu nome: ")
	cpf = input("Digite o CPF: ")
	while validacoes.validaCPF(cpf) == False or validacoes.pfExistente(cpf) == False:
		print("CPF inválido.")
		cpf = input("Digite seu CPF: ")
	fone =input("Digite o seu celular = xxxxxxxxxxx ")
	while validacoes.validafone(fone) == False:
		fone =input("Digite o seu celular = xxxxxxxxxxx ")
		fone.split(' ')
	validacoes.validafone(fone)
	
	email =input("Digite o seu email: ")
	while validacoes.validaemail(email) == False:
		email =input("Email inexistente \nDigite o seu email: ")
	nasc =input("Digite o seu nascimento XX/XX/XXXX: ")
	validacoes.validaData(nasc)
	cidade =input("Digite a sua cidade: ")
	nmrDired = input("Digite o número da DIRED a qual sua escola pertence: ")
	nome= nome
	SysPonto.Diretores[cpf] = [nome,fone,cpf,email,nasc,cidade,nmrDired]
	grava_diretor()
	print(diretores)
	print("Diretor cadastrado com sucesso")
	os.system ("cls")
def cadastraDired():
	nome =input("Digite o Código da DIRED: ")
	while validacoes.validafone(fone) == False:
		fone =input("Digite o seu celular = xxxxxxxxxxx ")
		fone.split(' ')
	validacoes.validafone(fone)
	
	email =input("Digite o seu email: ")
	while validacoes.validaemail(email) == False:
		email =input("Email inexistente \nDigite o seu email: ")
	cidade =input("Digite a sua cidade: ")
	SysPonto.Diretores[cod] = [fone,email,cidade]
	grava_dired()
	print(diretores)
	print("DIRED cadastrada com sucesso")
	os.system ("cls")
