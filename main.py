
contatos = ['1,Guilherme,guilherme@guilherme.com.br\n',
'2,Elias,elias@elias.com.br\n',
'3,Gabriel,gabriel@gabriel.com.br\n',
'4,Anderson,anderson@anderson.com.br\n',
'5,Alex,alex@alex.com.br\n',
'6,Vini,vini@vini.com.br\n',
'7,Letícia,leticia@leticia.com.br\n',
'8,Giulia,giulia@giulia.com.br\n',
'9,Felipe,felipe@felipe.com.br\n',
'10,Luísa,luisa@luisa\n',
]

try:
    with open('dados/contatos-escrita.csv', encoding='latin-1', mode= 'a+') as arquivo:
        for contato in contatos:
            arquivo.write(contato)
except FileNotFoundError:
    print('Arquivo inexistente. Confira se o caminho está correto')
except PermissionError:
    print('Permissão de escrita negada')