import SysPonto
def cpfExistenteProfessor(cpf):
	if cpf in SysPonto.professores:
		print ("CPF já cadastrado")
		return False
	else:
		return True
	

def cpfExistenteDiretor(cpf):
	if cpf in SysPonto.diretores:
		print ("CPF já cadastrado")
		return False
	else:
		return True


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
