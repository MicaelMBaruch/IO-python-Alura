content = open('dados/contatos.csv', encoding = 'latin_1')
# print(content.readlines())
for line in content:
    print(line, end= '')
