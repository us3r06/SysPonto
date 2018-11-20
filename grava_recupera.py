import SysPonto

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
        for i in diretores:
            for k in range(len(diretores[i])):
                conteudo += str(diretores[i][k]) + '|'
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
        for i in historico:
            for k in range(len(historico[i])):
                conteudo += str(historico[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()

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
            diretores[read[2]] = read[:]

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
            historico[read[2]] = read[:]
