import login
import grava_recupera


professores = {} 
Diretores = {}
direds = {}
Historico={}
DiredHistorico={}
grava_recupera.recuperar_professor()
grava_recupera.recuperar_diretor()
grava_recupera.recuperar_dired()
grava_recupera.recuperar_historico()
login.execute()
