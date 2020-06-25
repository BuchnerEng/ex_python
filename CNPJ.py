# Instrutor queria que separasse o código em funções para realizar as etapas do processo
def valida_cnpj(cnpj):
    input = cl_char(cnpj)
    resultado = ultimo(penultimo(cl_char(cnpj)))
    if input == resultado:
        print(f'CNPJ {cnpj} Válido.')
    else:
        print(f'CNPJ {cnpj} Inválido')


# Limpando os caracteres especiais comuns em CNPJ (ele mostrou um código de REGEX, mas não ensinou isso em si,
# por isso que está dessa maneira.)
def cl_char(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    return cnpj


# Faz o algoritmo básico de validação de um dos digitos finais do CNPJ
def alg_cnpj(l_1, l_2, cnpj):
    total = []
    for i, j in enumerate(l_1):
        total.append(l_1[i] * l_2[i])
    digito = 11 - (sum(total) % 11)
    if digito > 9:
        digito = 0
    cnpj = cnpj + str(digito)
    return cnpj


# Recebe os primeiros 12 caracteres e faz o processo de validação com a função alg_cnpj para gerar o 13º
def penultimo(cnpj):
    cnpj = cnpj[:-2]
    l_1 = [int(x) for x in cnpj]
    l_2 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cnpj = alg_cnpj(l_1, l_2, cnpj)
    return cnpj


# Recebe 13 caracteres e faz o processo de validação com a função alg_cnpj para gerar o 14º
def ultimo(cnpj):
    l_1 = [int(x) for x in cnpj]
    l_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cnpj = alg_cnpj(l_1, l_2, cnpj)
    return cnpj


# Teste da função com um CNPJ válido e um inválido
valida_cnpj('04.252.011/0001-10')
valida_cnpj('04.252.011/0001-15')
valida_cnpj('40.688.134/0001-61')
valida_cnpj('11.111.111/1111-11')
