import validacoes
import SysPonto

def menuCadastros():
	

def cadastraProfessor():
	nome =input("Digite o seu nome: ")
	cpf = input("Digite o CPF: ")
	while validacoes.validaCPF(cpf) == False or validacoes.cpfExistenteProfessor(cpf) == False:
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
	while validacoes.validaCPF(cpf) == False or validacoes.cpfExistenteDiretor(cpf) == False:
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

