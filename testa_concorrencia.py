contato_andrea = '11,Andrea,andrea@andrea.com\n'
contato_pat = '12,Pat,pat@pat.com\n'
    
with open('dados/contatos-escrita.csv', mode= 'w') as abertura_de_arquivo_1:
    abertura_de_arquivo_1.write(contato_andrea)
with open('dados/contatos-escrita.csv', mode= 'a') as abertura_de_arquivo_2:
    abertura_de_arquivo_2.write(contato_pat)


print('concluido')