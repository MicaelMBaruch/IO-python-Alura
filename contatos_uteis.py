import csv, pickle, json 
from contato import Contato

contatos = []
def csv_para_contatos(caminho, encoding = 'latin_1'):
    with open(caminho, encoding = encoding) as arquivo:
        linhas_lidas = csv.reader(arquivo)

        for linha in linhas_lidas:
            id, nome, email = linha
            contato = Contato(id, nome, email)    
            contatos.append(contato)
    return contatos

def contatos_para_pickle(contatos, destino):
    with open(destino, mode= 'wb') as arquivo:
        pickle.dump(contatos, arquivo)

def pickle_para_contatos(caminho):
    with open(caminho, mode ='rb') as arquivo:
        contatos = pickle.load(arquivo)
    return contatos

def _contato_para_json(contato):
    return contato.__dict__

    
def contatos_para_json(contatos, destino):
    with open(destino, mode= 'w') as arquivo:
        json.dump(contatos, arquivo, default = _contato_para_json)

def json_para_contatos(caminho):
    contatos = list()
    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)
    for contato in contatos_json:
        contatos.append(Contato(**contato))
    return contatos