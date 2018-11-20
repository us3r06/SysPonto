import sys
import cadastros
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

def execute():
	while True:
		menuLogin()
		opcaoLogin = input("Digite a opção desejada: ")
		if opcaoLogin.strip() == '0':
			print("Obrigado por usar o SysPonto")
			sys.exit()
		elif opcaoLogin.strip() == '1':
			menuProfessor()
		elif opcaoLogin.strip() == '2':
			menuDiretor()
		elif opcaoLogin.strip() == '3':
			menuDired()
		elif opcaoLogin.strip() == '4':
			cadastros.executeCadastros()
		else:
			print(opcaoLogin, "não é uma opção válida!\n")

